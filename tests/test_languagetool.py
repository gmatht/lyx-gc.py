"""Tests for LanguageTool integration."""
import os
import tempfile
import pytest
from lyxgc.languagetool import (
    find_java,
    get_languagetool_path,
    run_languagetool,
    parse_languagetool_output,
)


def test_find_java():
    """Java detection."""
    j = find_java()
    assert j is not None
    assert "java" in j.lower() or j == "java"


def test_get_languagetool_path():
    """LT path from env or default."""
    p = get_languagetool_path()
    assert isinstance(p, str)
    assert len(p) > 0


def test_parse_languagetool_output_empty_file():
    """Parse non-existent .languagetool returns 0."""
    import io
    n = parse_languagetool_output("/nonexistent/file.tex", [io.StringIO()])
    assert n == 0


def test_parse_languagetool_output_sample():
    """Parse sample LT output format."""
    import io
    with tempfile.NamedTemporaryFile(mode="w", suffix=".tex", delete=False) as f:
        tex_path = f.name
    try:
        lt_path = tex_path + ".languagetool"
        sample = """1.) Line 5, column 1, Rule ID: UPPERCASE_SENTENCE_START
Message: This sentence does not start with an uppercase letter.
this is a test.
    ^^^^
"""
        with open(lt_path, "w", encoding="utf-8") as f:
            f.write(sample)
        out = io.StringIO()
        n = parse_languagetool_output(tex_path, [out])
        assert n >= 1
        assert "UPPERCASE" in out.getvalue() or "uppercase" in out.getvalue()
    finally:
        if os.path.isfile(lt_path):
            os.remove(lt_path)
        if os.path.isfile(tex_path):
            os.remove(tex_path)
