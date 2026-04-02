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

from models import db, User, Paper, PaperImage, ApiUsageLog
from auth import auth_bp, init_oauth
from admin import admin_bp

from generate_ai_josn_paper import generate_paper_json
from genIEEE import build_document as build_ieee_docx

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
    "https://paper.otomasi.app",
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

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
openai_client = None

# ─── In-Memory Job Store ──────────────────────────────────────────────────────
_jobs: dict = {}
_jobs_lock = threading.Lock()

def _job_set(job_id, data):
    with _jobs_lock:
        _jobs[job_id] = data

def _job_get(job_id):
    with _jobs_lock:
        return _jobs.get(job_id)

def _job_pop(job_id):
    with _jobs_lock:
        return _jobs.pop(job_id, None)

def get_openai_client():
    global openai_client
    if openai_client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-actual-api-key":
            raise Exception("OPENAI_API_KEY not configured. Please set it in .env")
        openai_client = OpenAI(api_key=api_key, timeout=600.0)
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

def _run_generate_full_job(job_id, prompt, user_id=None):
    t_start = time.time()
    log.info("[job:%s] started, prompt=%r", job_id, prompt[:80])
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-actual-api-key":
            raise Exception("OPENAI_API_KEY not configured")

        paper_data = generate_paper_json(judul=prompt, custom_prompt="", api_key=api_key, model=OPENAI_MODEL)

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
        _job_set(job_id, {"status": "done", "result": paper_data, "usage": {}, "elapsed": int(elapsed)})
        log.info("[job:%s] DONE in %.1fs", job_id, elapsed)

    except Exception as e:
        elapsed = time.time() - t_start
        err_str = str(e)
        timeout_flag = "timeout" in type(e).__name__.lower() or "timeout" in err_str.lower() or "timed out" in err_str.lower()
        log.error("[job:%s] FAILED after %.1fs: %s", job_id, elapsed, e, exc_info=True)
        _job_set(job_id, {
            "status": "error",
            "error": f"Generation timed out after {int(elapsed)}s. Try a shorter topic." if timeout_flag else err_str,
            "timeout": timeout_flag,
        })


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

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-actual-api-key":
            raise Exception("OPENAI_API_KEY not configured")

        user_id = _get_current_user_id()
        job_id = uuid.uuid4().hex[:12]
        _job_set(job_id, {"status": "pending", "started_at": time.time()})
        threading.Thread(target=_run_generate_full_job, args=(job_id, prompt, user_id), daemon=True).start()
        return jsonify({"success": True, "job_id": job_id})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/api/job/<job_id>", methods=["GET"])
@jwt_required()
def get_job_status(job_id):
    job = _job_get(job_id)
    if job is None:
        return jsonify({"error": "Job not found or already retrieved"}), 404
    elapsed = int(time.time() - job.get("started_at", time.time())) if "started_at" in job else job.get("elapsed", 0)
    if job["status"] == "pending":
        return jsonify({"status": "pending", "elapsed": elapsed})
    elif job["status"] == "done":
        _job_pop(job_id)
        return jsonify({"status": "done", "success": True, "paper": job["result"], "usage": job.get("usage", {}), "elapsed": job.get("elapsed", elapsed)})
    else:
        _job_pop(job_id)
        return jsonify({"status": "error", "error": job.get("error", "Unknown error"), "timeout": job.get("timeout", False)})

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
        json_filename = f"_tmp_{uuid.uuid4().hex[:8]}.json"
        json_filepath = EXPORT_FOLDER / json_filename
        json_filepath.write_text(json.dumps(paper, ensure_ascii=False, indent=2), encoding="utf-8")
        try:
            output_path = EXPORT_FOLDER / f"paper_{uuid.uuid4().hex[:8]}.docx"
            build_ieee_docx(json_filepath, output_path)
            return send_file(
                str(output_path), as_attachment=True,
                download_name=f"{paper.get('title', 'paper')[:50]}.docx",
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
