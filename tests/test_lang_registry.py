"""Tests for language registry - LyX language names and locale resolution."""
import os
import subprocess
import sys
from pathlib import Path

import pytest

from lyxgc.lang.registry import (
    LYX_LANGUAGE_TO_MODULE,
    resolve_language,
    get_generate_error_types,
)


def test_registry_has_all_requested_languages():
    """Registry covers the requested LyX languages without duplication."""
    requested = [
        "Afrikaans", "Albanian", "English (USA)", "Greek (ancient)",
        "Arabic (ArabTeX)", "Arabic (Arabi)", "Armenian",
        "English (Australia)", "German (Austria, old spelling)",
        "German (Austria)", "Indonesian", "Malay", "Basque",
        "Belarusian", "Portuguese (Brazil)", "Breton", "English (UK)",
        "Bulgarian", "English (Canada)", "French (Canada)", "Catalan",
        "Chinese (simplified)", "Chinese (traditional)", "Coptic",
        "Croatian", "Czech", "Danish", "Divehi (Maldivian)", "Dutch",
        "English", "Esperanto", "Estonian", "Farsi", "Finnish", "French",
        "Galician", "German (old spelling)", "German", "German (Switzerland)",
        "Greek", "Greek (polytonic)", "Hebrew", "Hindi", "Hungarian",
        "Icelandic", "Interlingua", "Irish", "Italian", "Japanese",
        "Japanese (CJK)", "Kazakh", "Korean", "Kurmanji", "Lao", "Latin",
        "Latvian", "Lithuanian", "Lower Sorbian", "Marathi", "Mongolian",
        "English (New Zealand)", "Norwegian (Bokmaal)", "Norwegian (Nynorsk)",
        "Occitan", "Russian (Petrine orthography)", "Polish", "Portuguese",
        "Romanian", "Russian", "North Sami", "Sanskrit", "Scottish",
        "Serbian", "Serbian (Latin)", "Slovak", "Slovene", "Spanish",
        "Spanish (Mexico)", "Swedish", "Syriac", "Tamil", "Telugu",
        "Thai", "Turkish", "Turkmen", "Ukrainian", "Upper Sorbian",
        "Urdu", "Vietnamese",
    ]
    for name in requested:
        assert name in LYX_LANGUAGE_TO_MODULE, f"Missing language: {name!r}"


def test_english_variants_use_en():
    """All English variants map to en (no duplication)."""
    for name in ["English", "English (USA)", "English (UK)", "English (Australia)",
                 "English (Canada)", "English (New Zealand)"]:
        assert resolve_language(name) == "en", name


def test_french_variants_use_fr():
    """French variants map to fr."""
    assert resolve_language("French") == "fr"
    assert resolve_language("French (Canada)") == "fr"


def test_locale_codes():
    """LANG locale codes resolve to rule modules."""
    assert resolve_language("en_US.UTF-8") == "en"
    assert resolve_language("en_AU.UTF-8") == "en"
    assert resolve_language("en_GB") == "en"
    assert resolve_language("fr_FR.UTF-8") == "fr"
    assert resolve_language("fr_CA") == "fr"
    assert resolve_language("de_DE.UTF-8") == "de"
    assert resolve_language("es_ES") == "es"
    assert resolve_language("it_IT") == "it"
    assert resolve_language("pt_BR") == "pt"
    assert resolve_language("nl_NL") == "nl"
    assert resolve_language("ja_JP") == "ja"
    assert resolve_language("pl_PL") == "pl"
    assert resolve_language("nb_NO") == "nb"
    assert resolve_language("nn_NO") == "nn"
    assert resolve_language("dsb_DE") == "dsb"
    assert resolve_language("hsb_DE") == "hsb"


def test_dedicated_languages_have_rules():
    """Dedicated language modules return non-empty rules."""
    assert resolve_language("Polish") == "pl"
    assert resolve_language("Catalan") == "ca"
    pl_gen = get_generate_error_types("pl")
    ca_gen = get_generate_error_types("ca")
    assert len(pl_gen()) > 0
    assert len(ca_gen()) > 0
    gen = get_generate_error_types("generic")
    assert len(gen()) > 0


def test_none_returns_empty_rules():
    """resolve_language returning None yields empty rules."""
    gen = get_generate_error_types(None)
    assert callable(gen)
    rules = gen()
    assert rules == []


def test_en_fr_same_as_perl():
    """en and fr produce non-empty rules (Perl chktex_en/chktex_fr behavior)."""
    en_gen = get_generate_error_types("en")
    fr_gen = get_generate_error_types("fr")
    assert len(en_gen()) > 0
    assert len(fr_gen()) > 0


def test_german_has_rules():
    """German module returns non-empty rules."""
    from lyxgc.lang.registry import get_generate_error_types
    gen = get_generate_error_types("de")
    rules = gen()
    assert len(rules) > 0


def test_new_language_modules_smoke():
    """New dedicated modules resolve and return non-empty rules."""
    samples = [
        ("Afrikaans", "af"),
        ("Japanese", "ja"),
        ("Polish", "pl"),
        ("Norwegian (Bokmaal)", "nb"),
        ("Lower Sorbian", "dsb"),
        ("Upper Sorbian", "hsb"),
        ("Chinese (simplified)", "zh"),
        ("Coptic", "cop"),
        ("Syriac", "syc"),
    ]
    for lyx_name, expected_module in samples:
        assert resolve_language(lyx_name) == expected_module, lyx_name
        gen = get_generate_error_types(expected_module)
        rules = gen()
        assert len(rules) > 0, f"{expected_module} returned no rules"


def test_chktex_cli_lang_override():
    """chktex.py -l/--lang overrides LANG."""
    py_dir = Path(__file__).parent.parent
    fixture = py_dir / "tests" / "fixtures" / "simple_errors.tex"
    if not fixture.exists():
        pytest.skip("Fixture not found")

    # French via --lang
    result = subprocess.run(
        [sys.executable, str(py_dir / "chktex.py"), "-v0", "-l", "French", str(fixture)],
        capture_output=True,
        text=True,
        cwd=str(py_dir),
        env={**os.environ, "LANG": "en_US.UTF-8", "PYTHONPATH": str(py_dir)},
        timeout=10,
    )
    assert result.returncode == 0

    # German via --lang -> empty rules, no crash
    result2 = subprocess.run(
        [sys.executable, str(py_dir / "chktex.py"), "-v0", "-l", "German", str(fixture)],
        capture_output=True,
        text=True,
        cwd=str(py_dir),
        env={**os.environ, "PYTHONPATH": str(py_dir)},
        timeout=10,
    )
    assert result2.returncode == 0
