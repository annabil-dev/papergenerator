"""
Paper Generator - Backend API Server
=====================================
Flask API for AI-powered academic paper generation and DOCX export.
Supports IEEE conference paper format.
"""

import os
import re
import sys
import json
import uuid
import time
import base64
import logging
import traceback
import threading
from pathlib import Path
from datetime import datetime

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI
import httpx

from generate_docx_from_json import generate_ieee_docx
from generate_ai_josn_paper import generate_paper_json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# ─── Logging Setup ──────────────────────────────────────────────────────────
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
log.info("=" * 60)
log.info("Backend started")

# Configuration
UPLOAD_FOLDER = Path(__file__).parent / "uploads"
UPLOAD_FOLDER.mkdir(exist_ok=True)
EXPORT_FOLDER = Path(__file__).parent / "exports"
EXPORT_FOLDER.mkdir(exist_ok=True)

# OpenAI client
openai_client = None
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# ─── In-Memory Job Store ──────────────────────────────────────────────────────
# Stores background generation jobs: job_id -> { status, result, error, started_at }
_jobs: dict = {}
_jobs_lock = threading.Lock()

def _job_set(job_id: str, data: dict):
    with _jobs_lock:
        _jobs[job_id] = data

def _job_get(job_id: str) -> dict | None:
    with _jobs_lock:
        return _jobs.get(job_id)

def _job_pop(job_id: str) -> dict | None:
    with _jobs_lock:
        return _jobs.pop(job_id, None)


def get_openai_client():
    global openai_client
    if openai_client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-actual-api-key":
            raise Exception("OPENAI_API_KEY not configured. Please set it in backend/.env")
        # Use client-level timeout of 600s (rps-web pattern — same model, proven 2-3 min)
        openai_client = OpenAI(api_key=api_key, timeout=600.0)
    return openai_client


# ─── Health Check ─────────────────────────────────────────────────────────────

@app.route("/api/health", methods=["GET"])
def health():
    has_key = bool(os.getenv("OPENAI_API_KEY")) and os.getenv("OPENAI_API_KEY") != "sk-your-actual-api-key"
    return jsonify({
        "status": "ok",
        "model": OPENAI_MODEL,
        "hasApiKey": has_key,
        "timestamp": datetime.now().isoformat()
    })


# ─── AI Generate ─────────────────────────────────────────────────────────────

@app.route("/api/generate", methods=["POST"])
def generate():
    """
    Generate or edit paper content with AI.
    Expects JSON: { prompt: string, lastText: string, section: string }
    - prompt: the user's instruction
    - lastText: the current text content of the section being edited
    - section: which section is being edited (title, abstract, introduction, etc.)
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        prompt = data.get("prompt", "")
        last_text = data.get("lastText", "")
        paper_context = data.get("paperContext", {})

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        client = get_openai_client()

        section = data.get("section", "").lower()
        
        # Dynamic system prompts based on section type
        prompts_by_section = {
            "title": """You are an IEEE conference paper title writer. Generate a concise, specific paper title (max 15 words) 
that clearly indicates the research contribution. Include key technical terms and method names if relevant. Return ONLY the title.""",
            
            "abstract": """You are an IEEE conference paper writer. Generate a 150-200 word abstract following IEEE format.
Start with problem statement, then propose method, then results. Include quantitative metrics if available.
For formulas use $..$ notation. Return ONLY the abstract text.""",
            
            "introduction": """You are an IEEE conference researcher. Write an INTRODUCTION section (200-300 words) that:
1) Motivates the problem with background
2) Identifies the research gap
3) States contributions clearly
Include citations as [1], [2], etc. Use $$formula$$ for displayed equations. Write naturally, academically.""",
            
            "methodology": """You are a systems researcher. Write a METHODOLOGY/APPROACH section that describes:
1) Problem formulation (with equations if needed)
2) Proposed method/algorithm (with formulas: use $x$ for inline, $$formula$$ for display)
3) Implementation details
Use IEEE notation and cite related work as [1], [2]. Be technical and specific.""",
            
            "results": """You are a research scientist. Write EXPERIMENTAL RESULTS section:
1) Datasets/benchmarks used
2) Evaluation metrics with values (e.g., "achieves 92.5% accuracy")
3) Comparison with baselines [1][2]
4) Analysis and insights
Include numerical results. Cite properly. Be quantitative.""",
            
            "conclusion": """You are an academic writer. Write CONCLUSION section (100-150 words):
1) Summarize key contributions
2) Highlight achieved metrics
3) Mention future work
Keep it clear and formal. No markdown.""",
            
            "acknowledgment": """You are writing paper acknowledgments. Write 2-3 sentences thanking:
- Funding agencies (if any mention XXXX)
- Collaborators/advisors
- Data/resource providers
Format: "We thank X for Y support. We gratefully acknowledge Z."
Keep it professional and concise.""",
        }
        
        base_prompt = prompts_by_section.get(section, 
            """You are an expert academic writer for IEEE papers. Generate content for the specified section.
            Use LaTeX notation for formulas ($..$ inline, $$...$$ display). Cite with [1], [2], etc format.
            Write formally and technically. Return ONLY the content.""")
        
        system_prompt = base_prompt

        messages = [{"role": "system", "content": system_prompt}]

        # Build context message
        context_parts = []
        if paper_context:
            context_parts.append(f"Paper title: {paper_context.get('title', 'Untitled')}")
            if paper_context.get('authors'):
                context_parts.append(f"Authors: {json.dumps(paper_context['authors'])}")
            if paper_context.get('abstract'):
                context_parts.append(f"Abstract: {paper_context['abstract'][:500]}")

        if last_text:
            context_parts.append(f"\n--- Current content of '{section}' section ---\n{last_text}\n--- End of current content ---")

        if context_parts:
            messages.append({"role": "user", "content": "\n".join(context_parts)})
            messages.append({"role": "assistant", "content": "I understand the context. What would you like me to do?"})

        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages
        )

        result = response.choices[0].message.content
        return jsonify({
            "success": True,
            "content": result,
            "model": OPENAI_MODEL,
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# ─── Generate Full Paper ─────────────────────────────────────────────────────

def _run_generate_full_job(job_id: str, prompt: str):
    """
    Background thread: generates paper via generate_paper_json(), stores in _jobs.
    The HTTP endpoint returns immediately with job_id; frontend polls /api/job/<id>.
    """
    t_start = time.time()
    log.info("[job:%s] started, prompt=%r", job_id, prompt[:80])
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-actual-api-key":
            raise Exception("OPENAI_API_KEY not configured")

        log.info("[job:%s] calling generate_paper_json, model=%s", job_id, OPENAI_MODEL)
        paper_data = generate_paper_json(
            judul=prompt,
            custom_prompt="",
            api_key=api_key,
            model=OPENAI_MODEL,
        )

        # ── Normalise schema ─────────────────────────────────────────────────
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

        # ── Save JSON to output/ ─────────────────────────────────────────────
        try:
            output_dir = Path(__file__).parent / "output"
            output_dir.mkdir(exist_ok=True)
            safe_title = re.sub(r"[^a-zA-Z0-9_]", "_", prompt[:50]).strip("_")
            ts_str = time.strftime("%Y%m%d_%H%M%S")
            json_out = output_dir / f"{ts_str}_{safe_title}.json"
            json_out.write_text(
                json.dumps(paper_data, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            log.info("[job:%s] JSON saved → %s", job_id, json_out)
        except Exception as save_err:
            log.warning("[job:%s] Could not save JSON: %s", job_id, save_err)

        elapsed = time.time() - t_start
        log.info("[job:%s] DONE in %.1fs", job_id, elapsed)
        _job_set(job_id, {
            "status": "done",
            "result": paper_data,
            "usage": {},
            "elapsed": int(elapsed),
        })

    except Exception as e:
        elapsed = time.time() - t_start
        err_type = type(e).__name__
        err_str = str(e)
        timeout_flag = "timeout" in err_type.lower() or "timeout" in err_str.lower() or "timed out" in err_str.lower()
        log.error("[job:%s] FAILED after %.1fs (%s): %s", job_id, elapsed, err_type, e, exc_info=True)
        _job_set(job_id, {
            "status": "error",
            "error": f"Generation timed out after {int(elapsed)}s. Try a shorter topic." if timeout_flag else err_str,
            "timeout": timeout_flag,
        })



@app.route("/api/generate-full", methods=["POST"])
def generate_full():
    """
    Start full paper generation as a background job.
    Returns { job_id } immediately — poll /api/job/<job_id> for status.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        prompt = data.get("prompt", "").strip()
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Validate API key early so the user gets an instant error
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-actual-api-key":
            raise Exception("OPENAI_API_KEY not configured. Please set it in backend/.env")

        job_id = uuid.uuid4().hex[:12]
        _job_set(job_id, {"status": "pending", "started_at": time.time()})

        thread = threading.Thread(target=_run_generate_full_job, args=(job_id, prompt), daemon=True)
        thread.start()

        log.info("[generate-full] job_id=%s started for prompt=%r", job_id, prompt[:80])
        return jsonify({"success": True, "job_id": job_id})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/api/job/<job_id>", methods=["GET"])
def get_job_status(job_id):
    """
    Poll the status of a background generation job.
    Returns:
      { status: 'pending', elapsed: int }
      { status: 'done',    success: true, paper: {...}, usage: {...}, elapsed: int }
      { status: 'error',   error: str }
    """
    job = _job_get(job_id)
    if job is None:
        return jsonify({"error": "Job not found or already retrieved"}), 404

    elapsed = int(time.time() - job.get("started_at", time.time())) if "started_at" in job else job.get("elapsed", 0)

    if job["status"] == "pending":
        return jsonify({"status": "pending", "elapsed": elapsed})

    elif job["status"] == "done":
        _job_pop(job_id)   # clean up
        return jsonify({
            "status": "done",
            "success": True,
            "paper": job["result"],
            "usage": job.get("usage", {}),
            "elapsed": job.get("elapsed", elapsed),
        })

    else:  # error
        _job_pop(job_id)   # clean up
        return jsonify({
            "status": "error",
            "error": job.get("error", "Unknown error"),
            "timeout": job.get("timeout", False),
        })




# ─── Image Upload ─────────────────────────────────────────────────────────────

@app.route("/api/upload-image", methods=["POST"])
def upload_image():
    """Upload an image file for the paper."""
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        # Generate unique filename
        ext = Path(file.filename).suffix.lower()
        if ext not in [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"]:
            return jsonify({"error": "Invalid image format. Supported: png, jpg, jpeg, gif, bmp, svg"}), 400

        filename = f"{uuid.uuid4().hex}{ext}"
        filepath = UPLOAD_FOLDER / filename
        file.save(str(filepath))

        return jsonify({
            "success": True,
            "filename": filename,
            "url": f"/api/images/{filename}",
            "originalName": file.filename
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/api/images/<filename>", methods=["GET"])
def get_image(filename):
    """Serve uploaded image."""
    filepath = UPLOAD_FOLDER / filename
    if not filepath.exists():
        return jsonify({"error": "Image not found"}), 404
    return send_file(str(filepath))


# ─── Export DOCX ──────────────────────────────────────────────────────────────

@app.route("/api/export", methods=["POST"])
def export_docx():
    """
    Export paper to DOCX in IEEE conference format.
    Expects the full paper JSON structure.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No paper data provided"}), 400

        paper = data.get("paper", data)

        # Generate DOCX
        filename = f"paper_{uuid.uuid4().hex[:8]}.docx"
        filepath = EXPORT_FOLDER / filename

        generate_ieee_docx(paper, str(filepath), str(UPLOAD_FOLDER))

        return send_file(
            str(filepath),
            as_attachment=True,
            download_name=f"{paper.get('title', 'paper')[:50]}.docx",
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# ─── Save/Load Paper ─────────────────────────────────────────────────────────

@app.route("/api/papers", methods=["POST"])
def save_paper():
    """Save paper data to a JSON file."""
    try:
        data = request.get_json()
        paper_id = data.get("id", uuid.uuid4().hex[:8])
        papers_dir = Path(__file__).parent / "papers"
        papers_dir.mkdir(exist_ok=True)

        filepath = papers_dir / f"{paper_id}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return jsonify({"success": True, "id": paper_id})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/papers/<paper_id>", methods=["GET"])
def load_paper(paper_id):
    """Load paper data from JSON file."""
    try:
        filepath = Path(__file__).parent / "papers" / f"{paper_id}.json"
        if not filepath.exists():
            return jsonify({"error": "Paper not found"}), 404

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/papers", methods=["GET"])
def list_papers():
    """List all saved papers."""
    try:
        papers_dir = Path(__file__).parent / "papers"
        papers_dir.mkdir(exist_ok=True)

        papers = []
        for f in papers_dir.glob("*.json"):
            try:
                with open(f, "r", encoding="utf-8") as fp:
                    data = json.load(fp)
                    papers.append({
                        "id": f.stem,
                        "title": data.get("title", "Untitled"),
                        "modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat()
                    })
            except:
                pass

        papers.sort(key=lambda x: x["modified"], reverse=True)
        return jsonify({"papers": papers})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/papers/<paper_id>", methods=["DELETE"])
def delete_paper(paper_id):
    """Delete a saved paper."""
    try:
        filepath = Path(__file__).parent / "papers" / f"{paper_id}.json"
        if filepath.exists():
            filepath.unlink()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    print(f"🚀 Paper Generator API running on http://localhost:{port}")
    print(f"📝 Model: {OPENAI_MODEL}")
    print(f"🔑 API Key: {'configured' if os.getenv('OPENAI_API_KEY') else 'NOT SET'}")
    # use_reloader=False prevents the debug reloader from killing in-flight
    # long-running requests (e.g. OpenAI API calls) when source files change.
    app.run(host="0.0.0.0", port=port, debug=debug, use_reloader=False, threaded=True)
