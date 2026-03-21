"""Detect lyx-gc dependencies (LyX, chktex, lacheck, LanguageTool, Java)."""
from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


def which_all(*names: str) -> str | None:
    """Return first found executable path, or None."""
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


def find_lyx() -> tuple[bool, str]:
    """Check if LyX is installed. Returns (found, path_or_message)."""
    candidates = [
        "lyx",
        "lyx-qt",
        "lyx-xforms",
        "i686-pc-linux-gnu-lyx",
    ]
    path = which_all(*candidates)
    if path:
        return True, path

    # Windows: common install locations
    if sys.platform == "win32":
        for base in (
            os.environ.get("ProgramFiles", "C:\\Program Files"),
            os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)"),
        ):
            for sub in ("LyX 2.4", "LyX 2.3", "LyX 2.2", "LyX 2.1"):
                exe = Path(base) / sub / "bin" / "lyx.exe"
                if exe.is_file():
                    return True, str(exe)

    # macOS: Application bundle
    if sys.platform == "darwin":
        for app in Path("/Applications").glob("LyX*.app"):
            exe = app / "Contents/MacOS/lyx"
            if exe.is_file():
                return True, str(exe)

    return False, "not found in PATH or common locations"


def find_lacheck() -> tuple[bool, str]:
    """Check if lacheck is installed."""
    path = shutil.which("lacheck")
    if path:
        return True, path
    return False, "not found in PATH"


def find_chktex() -> tuple[bool, str]:
    """Check if chktex is installed."""
    path = shutil.which("chktex")
    if path:
        return True, path
    return False, "not found in PATH"


def find_system_chktex(*exclude_dirs: str | Path) -> tuple[bool, str]:
    """Find system ChkTeX binary, excluding our lyx-gc bin to avoid recursion.
    Use when our chktex needs to invoke the real ChkTeX for additional checks.
    """
    path_sep = ";" if sys.platform == "win32" else ":"
    excl = {Path(d).resolve() for d in exclude_dirs if d}
    path_env = os.environ.get("PATH", "")
    parts = [p.strip() for p in path_env.split(path_sep) if p.strip()]
    for p in parts:
        try:
            if Path(p).resolve() in excl:
                continue
        except (OSError, RuntimeError):
            continue
        chktex = Path(p) / ("chktex.exe" if sys.platform == "win32" else "chktex")
        if chktex.is_file() and os.access(chktex, os.X_OK):
            return True, str(chktex)
    # Fallback: standard locations
    for loc in ("/usr/bin/chktex", "/usr/local/bin/chktex"):
        p = Path(loc)
        if p.is_file() and os.access(p, os.X_OK):
            return True, str(p)
    return False, "not found"


def find_languagetool() -> tuple[bool, str]:
    """Check if LanguageTool (languagetool-commandline.jar) is installed."""
    jar_name = "languagetool-commandline.jar"
    env_path = os.environ.get("LANGUAGETOOL_PATH")
    if env_path:
        jar = Path(env_path).expanduser() / jar_name
        if jar.is_file():
            return True, str(jar.parent)
        return False, f"LANGUAGETOOL_PATH set but {jar_name} not found"
    candidates = [
        Path.home() / ".data" / "LanguageTool-stable",
        Path.home() / ".data" / "LanguageTool-2.1",
        Path.home() / ".data" / "LanguageTool-6.2",
        Path.home() / ".local" / "LanguageTool",
    ]
    for base in (Path.home() / ".data", Path.home() / ".local"):
        if base.is_dir():
            for d in base.iterdir():
                if d.is_dir() and "LanguageTool" in d.name:
                    candidates.append(d)
    for d in candidates:
        jar = d / jar_name
        if jar.is_file():
            return True, str(d)
    return False, "not found"


def find_java() -> tuple[bool, str]:
    """Check if Java is installed (required for LanguageTool)."""
    path = shutil.which("java")
    if path:
        return True, path
    # Windows: common Java install locations (Adoptium, Microsoft, etc.)
    if sys.platform == "win32":
        for base in (
            Path(os.environ.get("ProgramFiles", "C:\\Program Files")),
            Path(os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")),
        ):
            if not base.is_dir():
                continue
            for pat in ("Eclipse Adoptium/*/bin/java.exe", "*jdk*/bin/java.exe", "Java/*/bin/java.exe"):
                for exe in base.glob(pat):
                    if exe.is_file():
                        return True, str(exe.parent)
    return False, "not found in PATH"
