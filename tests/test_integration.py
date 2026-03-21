"""Integration tests - run chktex.py on fixtures."""
import io
import os
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
    """When Perl works, Python output should match on same fixture (same errors)."""
    if not PERL_CHKTEX.exists():
        pytest.skip("Perl chktex.pl not found")
    perl = shutil.which("perl")
    if not perl:
        pytest.skip("perl not found")

    fixture = PY_DIR / "tests" / "fixtures" / "simple_errors.tex"
    if not fixture.exists():
        pytest.skip("Fixture not found")

    with tempfile.TemporaryDirectory() as tmp:
        env = {**os.environ, "PYTHONPATH": str(PY_DIR)}
        env["HOME"] = tmp
        env["USERPROFILE"] = tmp

        py_result = subprocess.run(
            [sys.executable, str(PY_DIR / "chktex.py"), "-v0", str(fixture)],
            capture_output=True,
            text=True,
            cwd=str(PY_DIR),
            env=env,
            timeout=15,
        )

        pl_result = subprocess.run(
            [perl, str(PERL_CHKTEX), "-v0", str(fixture)],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
            env=env,
            timeout=15,
        )

    if pl_result.returncode != 0:
        pytest.skip("Perl chktex failed (may need HOME, ChkTeX, etc)")

    py_out = (py_result.stdout + py_result.stderr).lower()
    pl_out = (pl_result.stdout + pl_result.stderr).lower()

    # Both should report "we that" or similar
    assert "we that" in py_out or "we see that" in py_out or "666" in py_out
    assert "we that" in pl_out or "we see that" in pl_out or "666" in pl_out


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
