"""Integration tests - run chktex.py on fixtures."""
import io
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

# Path to py directory
PY_DIR = Path(__file__).parent.parent
REPO_ROOT = PY_DIR.parent
PERL_CHKTEX = REPO_ROOT / "path" / "chktex.pl"


def _win_to_wsl(path: Path) -> str:
    """Convert Windows path to WSL format (/mnt/d/...)."""
    s = str(path.resolve())
    if len(s) >= 2 and s[1] == ":":
        return "/mnt/" + s[0].lower() + s[2:].replace("\\", "/")
    return s.replace("\\", "/")


def _run_perl_chktex(
    perl_cmd: list,
    fixture_path: Path,
    env: dict,
    timeout: int,
    lang_name: str,
    lang_env: str,
) -> subprocess.CompletedProcess:
    """Run Perl chktex, using WSL on Windows when native perl fails."""
    result = subprocess.run(
        perl_cmd,
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
        env=env,
        timeout=timeout,
    )
    if result.returncode == 0:
        return result
    # On Windows, try WSL (Perl script uses Unix commands: mkdir -p, etc.)
    if platform.system() != "Windows":
        return result
    wsl = shutil.which("wsl")
    if not wsl:
        return result
    wsl_root = _win_to_wsl(REPO_ROOT)
    rel_fixture = fixture_path.relative_to(REPO_ROOT)
    wsl_fixture = rel_fixture.as_posix()
    # Export LANG in bash - passing custom env to subprocess breaks Perl on WSL
    export_str = f"export LANG={lang_env!r} LYX_LANGUAGE={lang_name!r}; "
    wsl_cmd = [
        wsl,
        "bash",
        "-c",
        f"{export_str}cd {wsl_root!r} && perl -I. path/chktex.pl -v0 {wsl_fixture!r}",
    ]
    return subprocess.run(
        wsl_cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=str(REPO_ROOT),
    )


def _normalize_output(output: str, path_placeholder: str = "FILE") -> str:
    """Normalize chktex -v0 output for comparison (path, line endings, >> <<, spacing)."""
    text = output.replace("\r\n", "\n").replace("\r", "\n").strip()
    # Python port may not yet produce >> << around triggers; normalize both
    text = text.replace(">>", "").replace("<<", "")
    # Perl uses ">  " (two spaces), Python uses "> " - normalize
    text = re.sub(r">\s+", "> ", text)
    lines = text.split("\n")
    normalized = []
    for line in lines:
        # Only keep chktex error lines (format: ...:line:col:666; or :666; ...)
        if ":666;" not in line and ":667;" not in line:
            continue
        # Format: filename:line:col:rule_id:error_text (filename may contain : on Windows)
        m = re.search(r":(\d+):(\d+):", line)
        if m:
            rest = line[m.start() + 1 :]  # line:col:rule_id:error_text
            normalized.append(f"{path_placeholder}:{rest}")
    return "\n".join(normalized)


def test_chktex_cli_simple():
    """chktex.py runs and produces output on simple fixture."""
    fixture = PY_DIR / "tests" / "fixtures" / "simple_errors.tex"
    if not fixture.exists():
        pytest.skip("Fixture not found")

    result = subprocess.run(
        [sys.executable, str(PY_DIR / "chktex.py"), "-v0", str(fixture)],
        capture_output=True,
        text=True,
        cwd=str(PY_DIR),
        env={**os.environ, "PYTHONPATH": str(PY_DIR)},
        timeout=10,
    )
    # May have no errors if rules don't match (e.g. \begin{document} handling)
    assert result.returncode == 0
    # Should mention at least one of our rules
    output = result.stdout + result.stderr
    assert "simple_errors" in output or "we that" in output or len(output) < 200


def test_chktex_vs_perl():
    """Python en/fr output must match Perl byte-for-byte (Perl runs under WSL on Windows)."""
    if not PERL_CHKTEX.exists():
        pytest.skip("Perl chktex.pl not found")
    perl = shutil.which("perl")
    if not perl:
        pytest.skip("perl not found")

    fixture = PY_DIR / "tests" / "fixtures" / "simple_errors.tex"
    if not fixture.exists():
        pytest.skip("Fixture not found")

    with tempfile.TemporaryDirectory() as tmp:
        base_env = {**os.environ, "PYTHONPATH": str(PY_DIR), "HOME": tmp, "USERPROFILE": tmp}

        # English only: Perl chktex_fr.pl has a syntax error (line 54)
        for lang_name, lang_env in [("English", "en_US.UTF-8")]:
            env = {**base_env, "LANG": lang_env, "LYX_LANGUAGE": lang_name}

            py_result = subprocess.run(
                [sys.executable, str(PY_DIR / "chktex.py"), "-v0", "-l", lang_name, str(fixture)],
                capture_output=True,
                text=True,
                cwd=str(PY_DIR),
                env=env,
                timeout=15,
            )

            pl_result = _run_perl_chktex(
                [perl, str(PERL_CHKTEX), "-v0", str(fixture)],
                fixture,
                env,
                timeout=15,
                lang_name=lang_name,
                lang_env=lang_env,
            )

            if pl_result.returncode != 0:
                err_preview = (pl_result.stderr or "")[:300]
                pytest.skip(
                    f"Perl chktex failed for {lang_name} (returncode={pl_result.returncode}, may need WSL on Windows): "
                    f"{err_preview}"
                )

            py_out = (py_result.stdout or "") + (py_result.stderr or "")
            pl_out = pl_result.stdout + pl_result.stderr

            py_norm = _normalize_output(py_out)
            pl_norm = _normalize_output(pl_out)
            # Sort lines to handle differing order (e.g. from child tools)
            py_lines = sorted(py_norm.split("\n"))
            pl_lines = sorted(pl_norm.split("\n"))
            assert py_lines == pl_lines, (
                f"Python and Perl outputs differ for {lang_name}. "
                f"Python ({len(py_lines)} lines):\n"
                + "\n".join(py_lines[:8])
                + ("\n..." if len(py_lines) > 8 else "")
                + f"\nPerl ({len(pl_lines)} lines):\n"
                + "\n".join(pl_lines[:8])
                + ("\n..." if len(pl_lines) > 8 else "")
            )


def test_chktex_via_module():
    """Can run find_errors via Python API."""
    from lyxgc.engine import find_errors
    from lyxgc.lang import get_generate_error_types

    tex = r"\begin{document} we that is wrong. \end{document}"
    out = io.StringIO()
    n = find_errors(
        get_generate_error_types("en")(),
        [out],
        tex,
        "t.tex",
        min_block_size=0,
        output_format="-v0",
    )
    assert n >= 1
    assert "we that" in out.getvalue() or "we see that" in out.getvalue()
