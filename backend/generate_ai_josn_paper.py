"""
IEEE Paper Generator
- System prompt & user template di-embed langsung dalam kode
- .env               → OPENAI_API_KEY, OPENAI_MODEL
- Input: JUDUL dan CUSTOM PROMPT dari user
- Record waktu + token
- Simpan hasil JSON ke output/
"""

import os
import re
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from json_repair import repair_json

# ── Config ────────────────────────────────────────────────────────────────────
BASE_DIR   = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

load_dotenv(BASE_DIR.parent / ".env")
load_dotenv(BASE_DIR / ".env", override=True)
MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini-2025-08-07")

# ── Prompt file path (loaded dynamically on each call) ───────────────────────
PROMPT_FILE = BASE_DIR / "prompt.txt"


USER_TEMPLATE = """Topic description: {judul}

Based on the topic description above:
1. Generate a professional, publication-ready IEEE-style academic title in English that best represents this topic.
2. Write a complete IEEE paper about this exact topic, incorporating all specific details mentioned (location, institution, system name, etc.).
3. All sections, equations, figures, tables, and references must be directly relevant to this topic.
4. If the topic description (and additional instructions) does NOT include numeric data (dataset size, accuracy, latency, voltage, etc.), you MUST generate estimated/simulation-based numeric values that fit the topic and keep them consistent across the abstract, tables, figures, Results, and Section V.
5. The output must include all sections through Section V (CONCLUSION); do not stop early.

Additional instructions: {custom_prompt}
"""


# ── Callable API ─────────────────────────────────────────────────────────────
def generate_paper_json(
    judul: str,
    custom_prompt: str = "",
    api_key: str = None,
    model: str = None,
    progress_cb=None,
) -> dict:
    """
    Generate a complete IEEE conference paper JSON from a title.
    
    Args:
        judul: Paper title / topic.
        custom_prompt: Additional instructions for the AI.
        api_key: OpenAI API key (falls back to OPENAI_API_KEY env var).
        model: Model name (falls back to OPENAI_MODEL env var).
        progress_cb: Optional callable(chars_done: int) for progress feedback.
    
    Returns:
        Parsed paper dict.
    
    Raises:
        ValueError: If the API key is missing or JSON cannot be parsed.
    """
    _api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not _api_key:
        raise ValueError("OPENAI_API_KEY tidak ditemukan di environment")
    _model = model or os.getenv("OPENAI_MODEL", MODEL)

    # Full-paper generation can exceed 7 minutes for long prompts; allow more headroom.
    _client = OpenAI(api_key=_api_key, timeout=1200.0)

    # ── Load system prompt fresh from disk on every call ────────────────────
    if PROMPT_FILE.exists():
        system_prompt = PROMPT_FILE.read_text(encoding="utf-8")
    else:
        raise ValueError("prompt.txt not found")

    user_message = (
        USER_TEMPLATE
        .replace("{judul}", judul)
        .replace("{prompt}", judul)
        .replace("{custom_prompt}", custom_prompt if custom_prompt else "(no additional instructions)")
    )

    stream = _client.chat.completions.create(
        model=_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        stream=True,
        stream_options={"include_usage": True},
    )

    raw_content = ""
    usage = None
    for chunk in stream:
        if hasattr(chunk, "usage") and chunk.usage:
            usage = chunk.usage
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta
        if delta and delta.content:
            raw_content += delta.content
            if progress_cb:
                progress_cb(len(raw_content))

    # Strip markdown fences if present
    clean = re.sub(r"^```(?:json)?\s*", "", raw_content.strip(), flags=re.IGNORECASE)
    clean = re.sub(r"\s*```$", "", clean)

    # Parse JSON with json_repair fallback
    paper_json = None
    try:
        paper_json = json.loads(clean)
    except json.JSONDecodeError as e1:
        try:
            repaired = repair_json(clean, return_objects=True)
            if isinstance(repaired, dict) and repaired:
                paper_json = repaired
            else:
                raise ValueError(f"json_repair did not return a dict: {type(repaired)}")
        except Exception as e2:
            raise ValueError(f"JSON parse failed: {e1} | repair: {e2}")

    if not isinstance(paper_json, dict):
        raise ValueError(f"Expected dict, got {type(paper_json)}")

    return paper_json


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        sys.exit("ERROR: OPENAI_API_KEY tidak ditemukan di .env")

    print("=" * 65)
    print("  IEEE Paper Generator — powered by OpenAI")
    print(f"  Model : {MODEL}")
    print("=" * 65)

    # ── Input dari user ───────────────────────────────────────────────────────
    print("\nMasukkan JUDUL paper IEEE:")
    judul = input("JUDUL  : ").strip()
    if not judul:
        sys.exit("ERROR: Judul tidak boleh kosong.")

    print("\nMasukkan CUSTOM PROMPT tambahan (opsional, tekan Enter untuk skip):")
    print("(contoh: Focus on real-time performance, use YOLO-based architecture)\n")
    custom_prompt = input("CUSTOM : ").strip()

    print(f"\n{'─'*65}")
    print(f"[JUDUL]  {judul}")
    print(f"[CUSTOM] {custom_prompt if custom_prompt else '(kosong)'}")
    print(f"{'─'*65}")
    print("Mengirim ke OpenAI dan streaming response...\n")

    t_start    = time.perf_counter()
    char_count = [0]

    def _progress(n: int):
        if n - char_count[0] >= 200:
            char_count[0] = n
            elapsed_so_far = time.perf_counter() - t_start
            print(f"  [{elapsed_so_far:5.1f}s] {n:,} karakter...", flush=True)

    paper_json = None
    json_valid = False
    json_err   = ""

    try:
        paper_json = generate_paper_json(
            judul=judul,
            custom_prompt=custom_prompt,
            api_key=api_key,
            model=MODEL,
            progress_cb=_progress,
        )
        json_valid = True
    except Exception as e:
        json_err = str(e)

    elapsed = time.perf_counter() - t_start
    print(f"\n  [DONE] {elapsed:.1f}s")

    # ── Simpan output ─────────────────────────────────────────────────────────
    safe_topic = re.sub(r'[^a-zA-Z0-9_]', '_', judul[:50])
    timestamp  = time.strftime("%Y%m%d_%H%M%S")
    out_stem   = f"{timestamp}_{safe_topic}"

    json_path = None
    if json_valid and paper_json:
        json_path = OUTPUT_DIR / f"{out_stem}.json"
        json_path.write_text(
            json.dumps(paper_json, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # ── Laporan ───────────────────────────────────────────────────────────────
    print("=" * 65)
    print("  HASIL")
    print("=" * 65)
    print(f"  Elapsed time : {elapsed:.2f} s  ({elapsed/60:.1f} menit)")
    print(f"  JSON valid   : {'✓ YA' if json_valid else '✗ TIDAK — ' + json_err}")
    if json_path:
        print(f"  JSON saved   : {json_path}")
    print("=" * 65)

    if json_valid and paper_json:
        title = paper_json.get("title", "(no title)")
        print(f"\n[JUDUL] {title}\n")

    return paper_json


if __name__ == "__main__":
    main()
