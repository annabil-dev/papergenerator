from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


def _resolve_copilot_program() -> str:
    # Prefer the real executable to avoid .bat/.cmd shims.
    try:
        exe = shutil.which("copilot.exe")
        if exe:
            return exe
    except Exception:
        pass
    return "copilot"


def _read_text_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace").strip("\n")
    except FileNotFoundError:
        return ""


def _build_prompt(system_prompt: str, user_prompt: str) -> str:
    parts: list[str] = []
    if system_prompt.strip():
        parts.append(system_prompt.strip())
    if user_prompt.strip():
        parts.append(user_prompt.strip())
    return "\n\n".join(parts)


def _create_log_file(log_dir: Path, workdir: str) -> Path:
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = f"copilot_{timestamp}"

    candidate = log_dir / f"{base}.log.txt"
    counter = 1
    while candidate.exists():
        candidate = log_dir / f"{base}_{counter}.log.txt"
        counter += 1

    header = (
        f"Timestamp: {timestamp}\n"
        f"Workdir: {workdir}\n"
        "\n"
    )
    candidate.write_text(header, encoding="utf-8", newline="\n")
    return candidate


def _start_detached_process(program: str, arguments: list[str], workdir: str, log_path: Path) -> int:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_handle = log_path.open("ab", buffering=0)
    try:
        popen_kwargs: dict[str, Any] = {
            "cwd": workdir,
            "stdin": subprocess.DEVNULL,
            "stdout": log_handle,
            "stderr": subprocess.STDOUT,
        }

        if sys.platform.startswith("win"):
            creationflags = 0
            if hasattr(subprocess, "CREATE_NEW_PROCESS_GROUP"):
                creationflags |= subprocess.CREATE_NEW_PROCESS_GROUP
            if hasattr(subprocess, "CREATE_BREAKAWAY_FROM_JOB"):
                creationflags |= subprocess.CREATE_BREAKAWAY_FROM_JOB
            if hasattr(subprocess, "CREATE_NO_WINDOW"):
                creationflags |= subprocess.CREATE_NO_WINDOW
            if creationflags:
                popen_kwargs["creationflags"] = creationflags

            # Extra: hide console window if any shim creates it.
            try:
                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                si.wShowWindow = 0  # SW_HIDE
                popen_kwargs["startupinfo"] = si
            except Exception:
                pass
        else:
            popen_kwargs["start_new_session"] = True

        p = subprocess.Popen([program, *arguments], **popen_kwargs)
        return int(p.pid)
    finally:
        try:
            log_handle.close()
        except Exception:
            pass


def main(argv: list[str] | None = None) -> int:
    script_dir = Path(__file__).resolve().parent
    default_workdir = str(script_dir)
    default_system_prompt_path = script_dir / "-copilot_systemPrompt.txt"
    default_log_dir = script_dir / "log_run"

    parser = argparse.ArgumentParser(
        prog="-copilot_run.py",
        description=(
            "Run `copilot` as a detached/background process and write logs to Tugas Akhir/log_run.\n\n"
            "System prompt is loaded automatically from -copilot_systemPrompt.txt (unless overridden).\n"
            "User prompt must be provided via --user-prompt, --user-prompt-file, or piped via stdin."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--workdir",
        default=default_workdir,
        help=f"Working directory for the Copilot process (default: {default_workdir})",
    )
    parser.add_argument(
        "--system-prompt-file",
        default=str(default_system_prompt_path),
        help=f"Path to system prompt file (default: {default_system_prompt_path})",
    )
    parser.add_argument(
        "--user-prompt",
        default=None,
        help='User prompt text. Use "-" to read from stdin.',
    )
    parser.add_argument(
        "--user-prompt-file",
        default=None,
        help="Path to a file containing the user prompt.",
    )
    parser.add_argument(
        "--model",
        default="gpt-5.2",
        help="Model name passed to copilot (default: gpt-5.2)",
    )
    parser.add_argument(
        "--reasoning-effort",
        default="xhigh",
        help="Reasoning effort passed to copilot (default: xhigh)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Do not print PID/log path to stdout (useful when you only monitor log_run).",
    )

    args = parser.parse_args(argv)

    workdir_path = Path(str(args.workdir)).expanduser()
    if not workdir_path.exists() or not workdir_path.is_dir():
        print(f"ERROR: workdir tidak valid: {workdir_path}", file=sys.stderr)
        return 2
    workdir = str(workdir_path.resolve())

    # Read prompts.
    system_prompt_path = Path(str(args.system_prompt_file)).expanduser()
    system_prompt = _read_text_file(system_prompt_path)

    if args.user_prompt is not None:
        if str(args.user_prompt).strip() == "-":
            user_prompt = sys.stdin.read()
        else:
            user_prompt = str(args.user_prompt)
    elif args.user_prompt_file:
        user_prompt = _read_text_file(Path(str(args.user_prompt_file)).expanduser())
    else:
        if sys.stdin.isatty():
            print(
                "ERROR: user prompt kosong. Pakai --user-prompt, --user-prompt-file, atau pipe stdin.",
                file=sys.stderr,
            )
            return 2
        user_prompt = sys.stdin.read()

    prompt = _build_prompt(system_prompt, user_prompt)
    if not prompt.strip():
        print("ERROR: Gabungan system+user prompt kosong.", file=sys.stderr)
        return 2

    # Create log.
    log_path = _create_log_file(default_log_dir, workdir)

    # Arguments for copilot.
    program = _resolve_copilot_program()

    # Allow dirs: workdir + repo root (parent of Tugas Akhir).
    allowed_dirs: list[str] = [workdir]
    try:
        repo_root = str(script_dir.parent)
        if repo_root and repo_root not in allowed_dirs:
            allowed_dirs.append(repo_root)
    except Exception:
        pass

    arguments = [
        "-p",
        prompt,
        "--model",
        str(args.model),
        "--reasoning-effort",
        str(args.reasoning_effort),
        "--allow-all-tools",
    ]

    for d in allowed_dirs:
        arguments.extend(["--add-dir", d])

    arguments.append("--no-color")

    # Log a command preview (without embedding the whole prompt).
    add_dir_preview = " ".join([f'--add-dir "{d}"' for d in allowed_dirs])
    cmd_preview = (
        f"CMD: {program} -p <prompt> --model {args.model} --reasoning-effort {args.reasoning_effort} "
        f"--allow-all-tools {add_dir_preview} --no-color\n"
        "---\n"
    )
    try:
        with log_path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(cmd_preview)
    except Exception:
        pass

    try:
        pid = _start_detached_process(program, arguments, workdir, log_path)
    except FileNotFoundError:
        print("ERROR: `copilot` tidak ditemukan di PATH.", file=sys.stderr)
        print(f"Log: {log_path}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"ERROR: gagal start copilot: {exc}", file=sys.stderr)
        print(f"Log: {log_path}", file=sys.stderr)
        return 1

    if not args.quiet:
        print(f"Started Copilot PID={pid}")
        print(f"Log: {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
