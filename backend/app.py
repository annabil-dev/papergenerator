"""
Paper Generator - Backend API Server
=====================================
Flask API for AI-powered academic paper generation and DOCX export.
Supports IEEE conference paper format, Google OAuth login, PostgreSQL storage.
"""

import os
import re
import sys
import json
import uuid
import time
import logging
import traceback
import threading
import importlib
from pathlib import Path
from datetime import datetime

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, get_jwt, verify_jwt_in_request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv
from openai import OpenAI

from models import db, User, Paper, PaperImage, ApiUsageLog, AiJob
from auth import auth_bp, init_oauth
from admin import admin_bp

from generate_ai_josn_paper import generate_paper_json
from template.IEEEgen import build_document as build_ieee_docx

# Load environment variables
load_dotenv(Path(__file__).parent.parent / ".env")
load_dotenv(Path(__file__).parent / ".env", override=True)

app = Flask(__name__)

# Trust nginx reverse proxy headers (X-Forwarded-For, X-Forwarded-Proto, etc.)
# This ensures url_for(..., _external=True) generates https:// URLs correctly
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# ─── Config ───────────────────────────────────────────────────────────────────
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://papergenerator:papergenerator123@localhost:5432/papergenerator'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ── Connection pool: 5 workers × 8 threads, pool_size=12, max_overflow=28 → max 200 PG conns
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 12,
    'max_overflow': 28,
    'pool_timeout': 30,
    'pool_recycle': 1800,    # recycle connections every 30 min
    'pool_pre_ping': True,   # test connection before use (handles dropped conns)
}
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'change-me-in-production')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'flask-secret-key')

# ─── Extensions ───────────────────────────────────────────────────────────────
CORS(app, supports_credentials=True, origins=[
    "http://localhost:1000",
    "http://localhost:5173",
    "https://paperfull.app",
    "https://www.paperfull.app",
])
db.init_app(app)
jwt = JWTManager(app)
init_oauth(app)

# Rate limiter — stored in-memory per worker (acceptable for 5 workers)
# For strict global limiting across workers, set RATELIMIT_STORAGE_URI=redis://...
# NOTE: nginx already handles burst rate limiting for external IPs.
# Flask-Limiter is a fallback safety net at the application level.
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["1000 per minute"],    # 1000 req/min per IP (~16/s, enough for one real user)
    storage_uri="memory://",
    strategy="fixed-window",
)

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

# ─── Logging Setup ────────────────────────────────────────────────────────────
LOG_FILE = Path(__file__).parent / "app.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ]
)
log = logging.getLogger(__name__)

UPLOAD_FOLDER = Path(__file__).parent / "uploads"
UPLOAD_FOLDER.mkdir(exist_ok=True)
EXPORT_FOLDER = Path(__file__).parent / "exports"
EXPORT_FOLDER.mkdir(exist_ok=True)

TEMPLATE_FOLDER = Path(__file__).parent / "template"


def _available_journals():
    """Return canonical journal/template codes based on template/*.docx + *gen.py."""
    codes = []
    try:
        for docx_path in TEMPLATE_FOLDER.glob("*.docx"):
            code = docx_path.stem
            gen_path = TEMPLATE_FOLDER / f"{code}gen.py"
            if gen_path.exists():
                codes.append(code)
    except Exception:
        return []
    return sorted(set(codes), key=str.lower)


def _resolve_journal_code(raw: str | None) -> str:
    available = _available_journals()
    if not raw:
        return "IEEE" if "IEEE" in available else (available[0] if available else "IEEE")
    raw_norm = str(raw).strip()
    if not raw_norm:
        return "IEEE" if "IEEE" in available else (available[0] if available else "IEEE")

    # Case-insensitive match to avoid client-side casing bugs
    m = {c.lower(): c for c in available}
    return m.get(raw_norm.lower(), raw_norm)


def _get_builder_for_journal(journal_code: str):
    """Return the build_document callable for a known template code."""
    available = _available_journals()
    m = {c.lower(): c for c in available}
    canonical = m.get(journal_code.lower())
    if not canonical:
        raise ValueError(f"Unknown journal template: {journal_code}")
    mod = importlib.import_module(f"template.{canonical}gen")
    builder = getattr(mod, "build_document", None)
    if not callable(builder):
        raise ValueError(f"Template generator missing build_document: {canonical}gen")
    return canonical, builder

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
openai_client = None

# ─── AI Job Store (DB-backed; safe across multi-worker gunicorn) ─────────────
def _job_create(job_id: str, user_id: int, prompt: str):
    job = AiJob(id=job_id, user_id=user_id, status="pending", prompt=prompt)
    db.session.add(job)
    db.session.commit()
    return job


def _job_get(job_id: str, user_id: int):
    return AiJob.query.filter_by(id=job_id, user_id=user_id).first()


def _job_set_done(job_id: str, user_id: int, paper_data: dict, elapsed_s: int):
    job = _job_get(job_id, user_id)
    if not job:
        return
    job.status = "done"
    job.result = paper_data
    job.error = None
    job.timeout = False
    db.session.commit()


def _job_set_error(job_id: str, user_id: int, error_msg: str, timeout_flag: bool = False):
    job = _job_get(job_id, user_id)
    if not job:
        return
    job.status = "error"
    job.error = error_msg
    job.timeout = bool(timeout_flag)
    db.session.commit()

def get_openai_client():
    global openai_client
    if openai_client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-actual-api-key":
            raise Exception("OPENAI_API_KEY not configured. Please set it in .env")
        openai_client = OpenAI(api_key=api_key, timeout=1200.0)
    return openai_client

def _get_current_user_id():
    try:
        verify_jwt_in_request(optional=True)
        identity = get_jwt_identity()
        return int(identity) if identity else None
    except Exception:
        return None

def _log_api_usage(endpoint, usage, user_id=None):
    try:
        with app.app_context():
            log_entry = ApiUsageLog(
                user_id=user_id,
                endpoint=endpoint,
                prompt_tokens=usage.get('prompt_tokens', 0),
                completion_tokens=usage.get('completion_tokens', 0),
                total_tokens=usage.get('total_tokens', 0),
                model=OPENAI_MODEL,
            )
            db.session.add(log_entry)
            db.session.commit()
    except Exception as e:
        log.warning("Failed to log API usage: %s", e)

# ─── DB Init ──────────────────────────────────────────────────────────────────
with app.app_context():
    db.create_all()
    log.info("Database tables created/verified")

# ─── Health Check ────────────────────────────────────────────────────────────

@app.route("/api/health", methods=["GET"])
@limiter.exempt
def health():
    has_key = bool(os.getenv("OPENAI_API_KEY")) and os.getenv("OPENAI_API_KEY") != "sk-your-actual-api-key"
    return jsonify({
        "status": "ok",
        "model": OPENAI_MODEL,
        "hasApiKey": has_key,
        "timestamp": datetime.now().isoformat()
    })

# ─── AI Generate (Section) ───────────────────────────────────────────────────

@app.route("/api/generate", methods=["POST"])
@limiter.limit("20 per minute")   # AI calls are expensive; 20/min per IP
@jwt_required()
def generate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        prompt = data.get("prompt", "")
        last_text = data.get("lastText", "")
        paper_context = data.get("paperContext", {})
        section = data.get("section", "").lower()

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        client = get_openai_client()

        prompts_by_section = {
            "title": "You are an IEEE conference paper title writer. Generate a concise, specific paper title (max 15 words). Return ONLY the title.",
            "abstract": "You are an IEEE conference paper writer. Generate a 150-200 word abstract. Start with problem statement, then method, then results. Return ONLY the abstract text.",
            "introduction": "You are an IEEE conference researcher. Write an INTRODUCTION section (200-300 words): 1) Motivate the problem 2) Identify research gap 3) State contributions. Include citations as [1], [2].",
            "methodology": "You are a systems researcher. Write a METHODOLOGY section describing: 1) Problem formulation 2) Proposed method/algorithm 3) Implementation details. Use IEEE notation.",
            "results": "You are a research scientist. Write EXPERIMENTAL RESULTS: 1) Datasets used 2) Metrics with values 3) Comparison with baselines 4) Analysis.",
            "conclusion": "You are an academic writer. Write CONCLUSION (100-150 words): 1) Summarize contributions 2) Highlight metrics 3) Future work.",
            "acknowledgment": "Write 2-3 sentences of paper acknowledgments thanking funding agencies, collaborators. Professional and concise.",
        }

        system_prompt = prompts_by_section.get(section,
            "You are an expert academic writer for IEEE papers. Generate content for the specified section. Use LaTeX notation for formulas. Return ONLY the content.")

        messages = [{"role": "system", "content": system_prompt}]
        context_parts = []
        if paper_context:
            context_parts.append(f"Paper title: {paper_context.get('title', 'Untitled')}")
            if paper_context.get('abstract'):
                context_parts.append(f"Abstract: {paper_context['abstract'][:500]}")
        if last_text:
            context_parts.append(f"\n--- Current content ---\n{last_text}\n--- End ---")
        if context_parts:
            messages.append({"role": "user", "content": "\n".join(context_parts)})
            messages.append({"role": "assistant", "content": "I understand the context. What would you like me to do?"})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(model=OPENAI_MODEL, messages=messages)
        result = response.choices[0].message.content
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }
        user_id = _get_current_user_id()
        threading.Thread(target=_log_api_usage, args=("generate", usage, user_id), daemon=True).start()
        return jsonify({"success": True, "content": result, "model": OPENAI_MODEL, "usage": usage})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# ─── Generate Full Paper ─────────────────────────────────────────────────────

def _run_generate_full_job(job_id, prompt, user_id=None, topic=None, style=None, pdf_texts=None):
    t_start = time.time()
    log.info("[job:%s] started, prompt=%r", job_id, prompt[:80])
    uid = None
    try:
        uid = int(user_id) if user_id is not None else None
    except Exception:
        uid = None
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-actual-api-key":
            raise Exception("OPENAI_API_KEY not configured")

        extra = ""
        if pdf_texts:
            combined = "\n\n".join(pdf_texts[:5])
            extra = f"\n\n[REFERENCE DOCUMENTS]\n{combined}"
        paper_data = generate_paper_json(
            judul=prompt,
            custom_prompt=extra,
            api_key=api_key,
            model=OPENAI_MODEL,
            topic=topic,
            style=style,
        )

        paper_data.setdefault("authors", [{"name": "Author Name", "affiliation": "Department, University", "location": "City, Country", "email": "author@example.com"}])
        paper_data.setdefault("keywords", [])
        paper_data.setdefault("sections", [])
        paper_data.setdefault("acknowledgment", "")
        paper_data.setdefault("references", [])
        paper_data.setdefault("figures", [])
        paper_data.setdefault("tables", [])
        paper_data.setdefault("equations", [])

        for auth in paper_data["authors"]:
            auth.setdefault("name", ""); auth.setdefault("affiliation", "")
            auth.setdefault("location", ""); auth.setdefault("email", "")

        for i, sec in enumerate(paper_data["sections"]):
            sec.setdefault("id", f"id-sec{i+1}"); sec.setdefault("number", "")
            sec.setdefault("title", ""); sec.setdefault("content", "")
            sec.setdefault("subsections", [])
            for j, sub in enumerate(sec["subsections"]):
                sub.setdefault("id", f"id-sub{i+1}{chr(97+j)}")
                sub.setdefault("letter", chr(65 + j))
                sub.setdefault("title", ""); sub.setdefault("content", "")
                sub.setdefault("numberedItems", [])

        for i, fig in enumerate(paper_data["figures"]):
            fig.setdefault("id", f"figure-{i+1}"); fig.setdefault("caption", f"Fig. {i+1}. ")
            fig.setdefault("filename", ""); fig.setdefault("url", "")

        for i, tbl in enumerate(paper_data["tables"]):
            tbl.setdefault("id", f"table-{i+1}"); tbl.setdefault("caption", f"TABLE {i+1}. ")
            tbl.setdefault("headers", []); tbl.setdefault("rows", [])

        for i, eq in enumerate(paper_data["equations"]):
            eq.setdefault("id", f"eq-{i+1}"); eq.setdefault("latex", ""); eq.setdefault("number", i + 1)

        try:
            output_dir = Path(__file__).parent / "output"
            output_dir.mkdir(exist_ok=True)
            safe_title = re.sub(r"[^a-zA-Z0-9_]", "_", prompt[:50]).strip("_")
            ts_str = time.strftime("%Y%m%d_%H%M%S")
            json_out = output_dir / f"{ts_str}_{safe_title}.json"
            json_out.write_text(json.dumps(paper_data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as save_err:
            log.warning("[job:%s] Could not save JSON: %s", job_id, save_err)

        elapsed = time.time() - t_start
        _log_api_usage("generate-full", {"total_tokens": 0, "prompt_tokens": 0, "completion_tokens": 0}, user_id)
        with app.app_context():
            if uid is not None:
                _job_set_done(job_id, uid, paper_data, int(elapsed))
        log.info("[job:%s] DONE in %.1fs", job_id, elapsed)

    except Exception as e:
        elapsed = time.time() - t_start
        err_str = str(e)
        timeout_flag = "timeout" in type(e).__name__.lower() or "timeout" in err_str.lower() or "timed out" in err_str.lower()
        log.error("[job:%s] FAILED after %.1fs: %s", job_id, elapsed, e, exc_info=True)
        with app.app_context():
            if uid is not None:
                _job_set_error(
                    job_id,
                    uid,
                    f"Generation timed out after {int(elapsed)}s. Try a shorter topic." if timeout_flag else err_str,
                    timeout_flag=timeout_flag,
                )


@app.route("/api/generate-full", methods=["POST"])
@limiter.limit("10 per minute")   # Full paper generation: heavier, stricter limit
@jwt_required()
def generate_full():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        prompt = data.get("prompt", "").strip()
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        topic = data.get("topic") or None
        style = data.get("style") or None
        pdf_texts = data.get("pdf_texts") or []

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-actual-api-key":
            raise Exception("OPENAI_API_KEY not configured")

        user_id = _get_current_user_id()
        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401
        job_id = uuid.uuid4().hex[:12]
        _job_create(job_id, int(user_id), prompt)
        threading.Thread(
            target=_run_generate_full_job,
            args=(job_id, prompt, user_id),
            kwargs={"topic": topic, "style": style, "pdf_texts": pdf_texts},
            daemon=True,
        ).start()
        return jsonify({"success": True, "job_id": job_id})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/api/job/<job_id>", methods=["GET"])
@jwt_required()
def get_job_status(job_id):
    user_id = int(get_jwt_identity())
    job = _job_get(job_id, user_id)
    if job is None:
        return jsonify({"error": "Job not found or already retrieved"}), 404

    elapsed = int((datetime.utcnow() - (job.started_at or datetime.utcnow())).total_seconds())
    if job.status == "pending":
        return jsonify({"status": "pending", "elapsed": elapsed})
    if job.status == "done":
        paper = job.result or {}
        try:
            db.session.delete(job)
            db.session.commit()
        except Exception:
            db.session.rollback()
        return jsonify({"status": "done", "success": True, "paper": paper, "usage": {}, "elapsed": elapsed})

    err = job.error or "Unknown error"
    timeout_flag = bool(job.timeout)
    try:
        db.session.delete(job)
        db.session.commit()
    except Exception:
        db.session.rollback()
    return jsonify({"status": "error", "error": err, "timeout": timeout_flag})

# ─── Topics / Styles / PDF Upload ─────────────────────────────────────────────

@app.route("/api/topics", methods=["GET"])
def list_topics():
    """Return sorted list of available topic slugs."""
    topic_dir = Path(__file__).parent / "prompt" / "topic"
    topics = sorted(
        p.stem for p in topic_dir.glob("*.txt") if not p.stem.startswith("_")
    )
    return jsonify({"topics": topics})


@app.route("/api/styles", methods=["GET"])
def list_styles():
    """Return sorted list of available citation style slugs."""
    style_dir = Path(__file__).parent / "prompt" / "style"
    styles = sorted(p.stem for p in style_dir.glob("*.txt"))
    return jsonify({"styles": styles})


MAX_PDF_FILES = 5
MAX_WORDS_PER_FILE = 5000

@app.route("/api/upload-pdfs", methods=["POST"])
@limiter.limit("20 per minute")
@jwt_required()
def upload_pdfs():
    """Extract text from up to 5 uploaded PDF/DOCX files (max 5000 words each)."""
    from extract_pdfs import extract_text_from_pdf  # noqa: PLC0415
    from docx import Document  # noqa: PLC0415

    files = request.files.getlist("files")
    if not files:
        return jsonify({"error": "No files uploaded"}), 400
    if len(files) > MAX_PDF_FILES:
        return jsonify({"error": f"Max {MAX_PDF_FILES} files allowed"}), 400

    results = []
    warnings = []
    for f in files:
        try:
            # Check file extension to determine extraction method
            filename = f.filename.lower()
            if filename.endswith('.pdf'):
                text = extract_text_from_pdf(f.stream)
            elif filename.endswith('.docx'):
                # Extract text from DOCX
                doc = Document(f.stream)
                text = "\n".join([para.text for para in doc.paragraphs])
            else:
                warnings.append(f"{f.filename}: format tidak didukung (hanya PDF dan DOCX)")
                continue

            words = text.split()
            if len(words) > MAX_WORDS_PER_FILE:
                warnings.append(f"{f.filename}: file terlalu besar, dibatasi ke {MAX_WORDS_PER_FILE} kata")
                text = " ".join(words[:MAX_WORDS_PER_FILE])
            results.append(text)
        except Exception as e:
            warnings.append(f"{f.filename}: gagal mengekstrak ({e})")

    return jsonify({"pdf_texts": results, "warnings": warnings})


# ─── Paper-specific Image Upload ─────────────────────────────────────────────

@app.route("/api/papers/<paper_id>/images", methods=["POST"])
@jwt_required()
def upload_paper_image(paper_id):
    try:
        user_id = int(get_jwt_identity())
        paper = Paper.query.filter_by(id=paper_id, user_id=user_id).first()
        if not paper:
            return jsonify({"error": "Paper not found"}), 404

        if "file" not in request.files:
            return jsonify({"error": "No file provided"}), 400
        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        ext = Path(file.filename).suffix.lower()
        if ext not in [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"]:
            return jsonify({"error": "Invalid image format"}), 400

        paper_upload_dir = UPLOAD_FOLDER / paper_id
        paper_upload_dir.mkdir(exist_ok=True)
        filename = f"{uuid.uuid4().hex}{ext}"
        filepath = paper_upload_dir / filename
        file.save(str(filepath))

        img = PaperImage(
            paper_id=paper_id, user_id=user_id,
            filename=filename, original_name=file.filename,
            file_path=f"{paper_id}/{filename}",
        )
        db.session.add(img)
        db.session.commit()
        return jsonify({"success": True, "image": img.to_dict()})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/api/papers/<paper_id>/images", methods=["GET"])
@jwt_required()
def list_paper_images(paper_id):
    try:
        user_id = int(get_jwt_identity())
        paper = Paper.query.filter_by(id=paper_id, user_id=user_id).first()
        if not paper:
            return jsonify({"error": "Paper not found"}), 404
        images = PaperImage.query.filter_by(paper_id=paper_id).order_by(PaperImage.created_at).all()
        return jsonify({"images": [img.to_dict() for img in images]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/papers/<paper_id>/images/<int:image_id>", methods=["DELETE"])
@jwt_required()
def delete_paper_image(paper_id, image_id):
    try:
        user_id = int(get_jwt_identity())
        img = PaperImage.query.filter_by(id=image_id, paper_id=paper_id, user_id=user_id).first()
        if not img:
            return jsonify({"error": "Image not found"}), 404
        filepath = UPLOAD_FOLDER / img.file_path
        if filepath.exists():
            filepath.unlink()
        db.session.delete(img)
        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/images/<paper_id>/<filename>", methods=["GET"])
def get_paper_image(paper_id, filename):
    safe_filename = Path(filename).name
    filepath = UPLOAD_FOLDER / paper_id / safe_filename
    if not filepath.exists():
        return jsonify({"error": "Image not found"}), 404
    return send_file(str(filepath))


@app.route("/api/journals", methods=["GET"])
@jwt_required()
def list_journals():
    try:
        return jsonify({"journals": _available_journals()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─── Legacy Image Upload ──────────────────────────────────────────────────────

@app.route("/api/upload-image", methods=["POST"])
@jwt_required()
def upload_image_legacy():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file provided"}), 400
        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400
        ext = Path(file.filename).suffix.lower()
        if ext not in [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"]:
            return jsonify({"error": "Invalid image format"}), 400
        legacy_dir = UPLOAD_FOLDER / "legacy"
        legacy_dir.mkdir(exist_ok=True)
        filename = f"{uuid.uuid4().hex}{ext}"
        filepath = legacy_dir / filename
        file.save(str(filepath))
        return jsonify({"success": True, "filename": filename, "url": f"/api/images/legacy/{filename}", "originalName": file.filename})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# ─── Export DOCX ──────────────────────────────────────────────────────────────

@app.route("/api/export", methods=["POST"])
@jwt_required()
def export_docx():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No paper data provided"}), 400
        paper = data.get("paper", data)

        journal_raw = data.get("journal")
        if isinstance(paper, dict) and not journal_raw:
            journal_raw = paper.get("journal")
        journal_code = _resolve_journal_code(journal_raw)
        try:
            canonical_journal, builder = _get_builder_for_journal(journal_code)
        except Exception as e:
            return jsonify({"error": str(e), "available": _available_journals()}), 400

        json_filename = f"_tmp_{uuid.uuid4().hex[:8]}.json"
        json_filepath = EXPORT_FOLDER / json_filename
        json_filepath.write_text(json.dumps(paper, ensure_ascii=False, indent=2), encoding="utf-8")
        try:
            output_path = EXPORT_FOLDER / f"{canonical_journal}_{uuid.uuid4().hex[:8]}.docx"
            builder(json_filepath, output_path)

            safe_title = re.sub(r'[^a-zA-Z0-9_\-]+', '_', str(paper.get('title', 'paper'))).strip('_')
            if not safe_title:
                safe_title = 'paper'
            download_name = f"{canonical_journal}_{safe_title[:60]}.docx"
            return send_file(
                str(output_path), as_attachment=True,
                download_name=download_name,
                mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        finally:
            json_filepath.unlink(missing_ok=True)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# ─── Paper CRUD ───────────────────────────────────────────────────────────────

@app.route("/api/papers", methods=["GET"])
@jwt_required()
def list_papers():
    try:
        user_id = int(get_jwt_identity())
        papers = Paper.query.filter_by(user_id=user_id).order_by(Paper.updated_at.desc()).all()
        return jsonify({"papers": [p.to_dict() for p in papers]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/papers", methods=["POST"])
@jwt_required()
def save_paper():
    try:
        user_id = int(get_jwt_identity())
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        paper_id = data.get("id") or uuid.uuid4().hex[:12]
        title = data.get("title") or (data.get("data") or {}).get("title") or "Untitled"

        paper = Paper.query.filter_by(id=paper_id, user_id=user_id).first()
        if paper:
            paper.title = title
            paper.data = data
            paper.updated_at = datetime.utcnow()
        else:
            paper = Paper(id=paper_id, user_id=user_id, title=title, data=data)
            db.session.add(paper)

        db.session.commit()
        return jsonify({"success": True, "id": paper_id, "paper": paper.to_dict()})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/api/papers/<paper_id>", methods=["GET"])
@jwt_required()
def load_paper(paper_id):
    try:
        user_id = int(get_jwt_identity())
        paper = Paper.query.filter_by(id=paper_id, user_id=user_id).first()
        if not paper:
            return jsonify({"error": "Paper not found"}), 404
        return jsonify({**(paper.data or {}), "id": paper.id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/papers/<paper_id>", methods=["PUT"])
@jwt_required()
def update_paper(paper_id):
    try:
        user_id = int(get_jwt_identity())
        paper = Paper.query.filter_by(id=paper_id, user_id=user_id).first()
        if not paper:
            return jsonify({"error": "Paper not found"}), 404
        data = request.get_json()
        title = data.get("title") or (data.get("data") or {}).get("title") or "Untitled"
        paper.title = title
        paper.data = data
        paper.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"success": True, "paper": paper.to_dict()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/papers/<paper_id>", methods=["DELETE"])
@jwt_required()
def delete_paper(paper_id):
    try:
        user_id = int(get_jwt_identity())
        paper = Paper.query.filter_by(id=paper_id, user_id=user_id).first()
        if not paper:
            return jsonify({"error": "Paper not found"}), 404
        paper_img_dir = UPLOAD_FOLDER / paper_id
        if paper_img_dir.exists():
            import shutil
            shutil.rmtree(str(paper_img_dir))
        db.session.delete(paper)
        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", os.getenv("BACKEND_PORT", 1001)))
    debug = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    log.info("=" * 60)
    log.info("Paper Generator API starting on port %d", port)
    print(f"🚀 Paper Generator API running on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=debug, use_reloader=False, threaded=True)
