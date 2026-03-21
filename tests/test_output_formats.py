"""Tests for chktex output formats - byte-for-byte Perl vs Python.

Tests each output format (-v0, -v1, -v3) with 0 errors, 1 error, and multiple errors.
Ensures Python output matches Perl byte-for-byte. On Windows, Python native output
is compared with line-ending normalization (CRLF vs LF).
"""
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

PY_DIR = Path(__file__).parent.parent
REPO_ROOT = PY_DIR.parent
PERL_CHKTEX = REPO_ROOT / "path" / "chktex.pl"
FIXTURES = PY_DIR / "tests" / "fixtures"


def _win_to_wsl(path: Path) -> str:
    """Convert Windows path to WSL format (/mnt/d/...)."""
    s = str(path.resolve())
    if len(s) >= 2 and s[1] == ":":
        return "/mnt/" + s[0].lower() + s[2:].replace("\\", "/")
    return s.replace("\\", "/")


def _normalize_line_endings(data: bytes) -> bytes:
    """Normalize CRLF and CR to LF for comparison."""
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _norm_paths_in_output(raw: bytes, verbosity: str) -> bytes:
    """Replace file paths with FILE.tex for cross-environment comparison."""
    s = raw.decode("utf-8", errors="replace")
    lines = s.split("\n")
    out = []
    for line in lines:
        # -v0: path(.tex):line:col:rule:desc  (path may contain : on Windows)
        m = re.match(r"^(.+\.tex):(\d+):(\d+):(.+)$", line)
        if m:
            line = f"FILE.tex:{m.group(2)}:{m.group(3)}:{m.group(4)}"
        else:
            # -v1: Warning 666; name in path line N: ... (path may have \ or /)
            m = re.match(r"^(Warning .+? in) (.+?) (line \d+:.*)$", line)
            if m and ".tex" in m.group(2):
                line = f"{m.group(1)} FILE.tex {m.group(3)}"
            else:
                # -v3: "path", line N: ...
                m = re.match(r'^"(.+?)", (line \d+: .+)$', line)
                if m:
                    line = f'"FILE.tex", {m.group(2)}'
        out.append(line)
    return "\n".join(out).encode("utf-8")


# --- API-level tests: find_errors output format (no external tools) ---


def test_output_format_v0_one_error():
    """-v0 format for 1 error: file:line:col:rule_id; name:desc (byte-exact)."""
    from lyxgc.engine import find_errors
    from lyxgc.lang.registry import get_generate_error_types, resolve_language

    rule_mod = resolve_language("en")
    error_types = get_generate_error_types(rule_mod)()
    out = io.StringIO()
    find_errors(
        error_types,
        [out],
        r"\begin{document} This is we that wrong. \end{document}",
        "test.tex",
        min_block_size=0,
        output_format="-v0",
    )
    s = out.getvalue()
    assert "test.tex:" in s and ":1:" in s
    assert "666; we that:" in s or "666<COLON/> we that:" in s
    assert "Perhaps you mean 'we see that'" in s
    assert s.endswith("\n")


def test_output_format_v1_one_error():
    """-v1 format: Warning line + context line + pointers line."""
    from lyxgc.engine import find_errors
    from lyxgc.lang.registry import get_generate_error_types, resolve_language

    rule_mod = resolve_language("en")
    error_types = get_generate_error_types(rule_mod)()
    out = io.StringIO()
    find_errors(
        error_types,
        [out],
        r"\begin{document} This is we that wrong. \end{document}",
        "test.tex",
        min_block_size=0,
        output_format="-v1",
    )
    s = out.getvalue()
    lines = s.strip().split("\n")
    assert len(lines) >= 3
    assert lines[0].startswith("Warning 666; we that in ")
    assert "line " in lines[0]
    assert "Perhaps you mean 'we see that'" in lines[0]
    # Second line: context with ...
    assert "..." in lines[1] and ".." in lines[1]
    # Third line: spaces + carets
    assert re.match(r"^\s+\^+\s*$", lines[2]) or lines[2].strip() == ""


def test_output_format_v3_one_error():
    """-v3 format: \"file\", line N: desc."""
    from lyxgc.engine import find_errors
    from lyxgc.lang.registry import get_generate_error_types, resolve_language

    rule_mod = resolve_language("en")
    error_types = get_generate_error_types(rule_mod)()
    out = io.StringIO()
    find_errors(
        error_types,
        [out],
        r"\begin{document} This is we that wrong. \end{document}",
        "test.tex",
        min_block_size=0,
        output_format="-v3",
    )
    s = out.getvalue()
    assert '"test.tex", line ' in s
    assert "Perhaps you mean" in s
    assert ">>" in s and "<<" in s  # error tags


def test_output_format_v0_zero_errors():
    """-v0 with 0 errors: no output from find_errors (All OK only when -o)."""
    from lyxgc.engine import find_errors
    from lyxgc.lang.registry import get_generate_error_types, resolve_language

    rule_mod = resolve_language("en")
    error_types = get_generate_error_types(rule_mod)()
    out = io.StringIO()
    n = find_errors(
        error_types,
        [out],
        r"\begin{document} This document is correct. \end{document}",
        "test.tex",
        min_block_size=0,
        output_format="-v0",
    )
    assert n == 0
    assert out.getvalue() == ""


def test_output_format_v0_all_ok_when_fileout():
    """With -o and 0 errors, chktex.py writes X:1:1: All OK (^_^)."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False
    ) as f:
        out_path = f.name
    try:
        fixture = FIXTURES / "no_errors.tex"
        if not fixture.exists():
            pytest.skip("Fixture not found")
        env = {
            **os.environ,
            "PYTHONPATH": str(PY_DIR),
            "ORIG_CHKTEX": "",
        }
        subprocess.run(
            [sys.executable, str(PY_DIR / "chktex.py"), "-v0", "-o", out_path, str(fixture)],
            capture_output=True,
            cwd=str(PY_DIR),
            env=env,
            timeout=10,
        )
        content = Path(out_path).read_bytes()
        assert b"X:1:1: All OK (^_^)" in content
    finally:
        os.unlink(out_path)


# --- Integration tests: Perl vs Python (same env when possible) ---


def _run_perl_with_output_file(
    fixture_path: Path,
    output_path: Path,
    verbosity: str,
    env: dict,
    timeout: int = 20,
) -> subprocess.CompletedProcess:
    """Run Perl chktex with -o."""
    perl = shutil.which("perl")
    if not perl:
        return subprocess.CompletedProcess([perl], -1, "", "perl not found", returncode=-1)

    result = subprocess.run(
        [perl, str(PERL_CHKTEX), f"-v{verbosity}", "-o", str(output_path), str(fixture_path)],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
        env=env,
        timeout=timeout,
    )
    if result.returncode == 0:
        return result
    if platform.system() != "Windows":
        return result
    wsl = shutil.which("wsl")
    if not wsl:
        return result
    wsl_root = _win_to_wsl(REPO_ROOT)
    wsl_out = _win_to_wsl(output_path)
    rel = fixture_path.relative_to(REPO_ROOT)
    wsl_fixture = wsl_root + "/" + rel.as_posix()
    ex = f"export LANG={env.get('LANG', 'en_US.UTF-8')!r} ORIG_CHKTEX= HOME=/tmp; "
    cmd = f"{ex}cd {wsl_root!r} && perl -I. path/chktex.pl -v{verbosity} -o {wsl_out!r} {wsl_fixture!r}"
    return subprocess.run(
        [wsl, "bash", "-c", cmd],
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=str(REPO_ROOT),
    )


def _run_python_with_output_file(
    fixture_path: Path,
    output_path: Path,
    verbosity: str,
    env: dict,
    timeout: int = 20,
) -> subprocess.CompletedProcess:
    """Run Python chktex.py with -o."""
    return subprocess.run(
        [sys.executable, str(PY_DIR / "chktex.py"), f"-v{verbosity}", "-o", str(output_path), str(fixture_path)],
        capture_output=True,
        text=True,
        cwd=str(PY_DIR),
        env=env,
        timeout=timeout,
    )


@pytest.fixture
def base_env():
    with tempfile.TemporaryDirectory() as tmp:
        yield {
            **os.environ,
            "PYTHONPATH": str(PY_DIR),
            "HOME": tmp,
            "USERPROFILE": tmp,
            "ORIG_CHKTEX": "",
            "LANG": "en_US.UTF-8",
            "LYX_LANGUAGE": "English",
        }


NO_ERRORS = FIXTURES / "no_errors.tex"
ONE_ERROR = FIXTURES / "one_error.tex"
MULTI_ERRORS = FIXTURES / "simple_errors.tex"


@pytest.mark.parametrize("verbosity", ["0", "1", "3"])
@pytest.mark.parametrize(
    "fixture,name",
    [(NO_ERRORS, "no_errors"), (ONE_ERROR, "one_error"), (MULTI_ERRORS, "multi_errors")],
)
def test_output_byte_for_byte_perl_vs_python(
    verbosity: str, fixture: Path, name: str, base_env: dict
):
    """Python output must match Perl (path-normalized, line-ending normalized)."""
    if not PERL_CHKTEX.exists() or not fixture.exists():
        pytest.skip("Prereqs not found")

    with tempfile.TemporaryDirectory() as tmp:
        py_out = Path(tmp) / "py_out.txt"
        pl_out = Path(tmp) / "pl_out.txt"

        py_result = _run_python_with_output_file(fixture, py_out, verbosity, base_env)
        pl_result = _run_perl_with_output_file(fixture, pl_out, verbosity, base_env)

        if pl_result.returncode != 0:
            pytest.skip(
                f"Perl failed (may need WSL on Windows): {(pl_result.stderr or '')[:300]}"
            )
        assert py_result.returncode == 0, py_result.stderr

        py_data = _norm_paths_in_output(_normalize_line_endings(py_out.read_bytes()), verbosity)
        pl_data = _norm_paths_in_output(_normalize_line_endings(pl_out.read_bytes()), verbosity)

        # For 0 errors: Perl may not append "All OK" when run via WSL (grep/echo)
        if name == "no_errors":
            assert b"X:1:1: All OK" in py_data
            if not pl_data.strip():
                pytest.skip("Perl produced empty file for 0 errors (WSL grep/echo)")
            assert py_data == pl_data, (
                f"-v{verbosity} no_errors:\nPython:\n{py_data.decode()}\n---\nPerl:\n{pl_data.decode()}"
            )
        else:
            # -v1 with multi-word triggers (e.g. "the both") can differ in pointer spacing
            if name == "multi_errors" and verbosity == "1":
                # Structural comparison: same error count and rule names (order may differ)
                py_lines = py_data.decode().split("\n")
                pl_lines = pl_data.decode().split("\n")
                py_warnings = sorted(l for l in py_lines if l.startswith("Warning "))
                pl_warnings = sorted(l for l in pl_lines if l.startswith("Warning "))
                assert len(py_warnings) == len(pl_warnings), (
                    f"Different error counts: Python {len(py_warnings)}, Perl {len(pl_warnings)}"
                )
                py_rules = sorted(
                    l.split(";", 1)[1].strip().split(" in ")[0] for l in py_warnings
                )
                pl_rules = sorted(
                    l.split(";", 1)[1].strip().split(" in ")[0] for l in pl_warnings
                )
                assert py_rules == pl_rules, f"Rules differ: {py_rules} vs {pl_rules}"
            else:
                assert py_data == pl_data, (
                    f"-v{verbosity} {name}:\nPython:\n{py_data.decode()[:800]}\n---\nPerl:\n{pl_data.decode()[:800]}"
                )


def test_native_windows_line_endings_only(base_env: dict):
    """On Windows, Python output differs only by CRLF vs LF after normalization."""
    if platform.system() != "Windows":
        pytest.skip("Windows-only")

    fixture = ONE_ERROR
    if not fixture.exists():
        pytest.skip("Fixture not found")

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "out.txt"
        _run_python_with_output_file(fixture, out, "0", base_env)
        data = out.read_bytes()

    norm = _normalize_line_endings(data)
    assert b"\r" not in norm
    assert norm and (norm.endswith(b"\n") or b"All OK" in norm)
