#!/usr/bin/env python3
"""
Launch LyX with lyx-gc environment: our chktex in PATH, LANGUAGETOOL_PATH, ORIG_CHKTEX, etc.
Use this instead of LyX directly so Tools -> Check Text uses the Python grammar checker.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

# Add py dir for imports
_SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPT_DIR))

from lyxgc.detect import (
    find_java,
    find_languagetool,
    find_lyx,
    find_system_chktex,
)


def get_bin_dir() -> Path:
    """Path to py/bin (contains chktex stub for LyX to find)."""
    return _SCRIPT_DIR / "bin"


def setup_env() -> dict[str, str]:
    """Build env dict with lyx-gc paths. Caller merges with os.environ."""
    env = dict(os.environ)
    bin_dir = get_bin_dir()

    # Prepend our bin (with chktex stub) to PATH so LyX finds it first
    path_sep = ";" if sys.platform == "win32" else ":"
    env["PATH"] = str(bin_dir) + path_sep + env.get("PATH", "")

    # ORIG_CHKTEX: system chktex (exclude our bin to avoid recursion)
    found, orig = find_system_chktex(bin_dir)
    if found:
        env["ORIG_CHKTEX"] = orig

    # LANGUAGETOOL_PATH: required for LanguageTool integration
    found, lt_path = find_languagetool()
    if found:
        env["LANGUAGETOOL_PATH"] = lt_path

    # Windows: ensure LyX and Java (for LanguageTool) are in PATH if found
    if sys.platform == "win32":
        found_lyx, lyx_path = find_lyx()
        if found_lyx:
            lyx_bin = str(Path(lyx_path).parent)
            env["PATH"] = lyx_bin + path_sep + env["PATH"]
        found_java, java_path = find_java()
        if found_java:
            java_bin = str(Path(java_path).parent)
            if java_bin not in env["PATH"]:
                env["PATH"] = java_bin + path_sep + env["PATH"]

    return env


def main() -> int:
    found, lyx_path = find_lyx()
    if not found:
        print("LyX not found. Run: python check_deps.py", file=sys.stderr)
        return 1

    bin_dir = get_bin_dir()
    has_stub = (bin_dir / "chktex").exists() or (bin_dir / "chktex.bat").exists()
    if not has_stub:
        print(f"chktex stub missing in {bin_dir}", file=sys.stderr)
        return 1

    env = setup_env()
    args = [lyx_path] + sys.argv[1:]
    return subprocess.run(args, env=env).returncode


if __name__ == "__main__":
    sys.exit(main())
