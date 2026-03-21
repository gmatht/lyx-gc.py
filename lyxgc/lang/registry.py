"""Language registry: map LyX language names and locale codes to rule modules.

LyX document languages and LANG locale codes map to:
- "en" -> English rules (chktex_en)
- "fr" -> French rules (chktex_fr)
- "de", "es", "it", "pt", "nl" -> respective rule modules
- "af", "sq", "ar", ... -> dedicated language modules with native messages
- "generic" -> structural rules with English messages (fallback for unknown locales)
"""

# LyX document language names -> rule module
# From LyX Document > Settings > Language
# Avoid duplication: all English variants -> "en", French variants -> "fr"
LYX_LANGUAGE_TO_MODULE: dict[str, str | None] = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Arabic (ArabTeX)": "ar",
    "Arabic (Arabi)": "ar",
    "Armenian": "hy",
    "Basque": "eu",
    "Belarusian": "be",
    "Breton": "br",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Chinese (simplified)": "zh",
    "Chinese (traditional)": "zh",
    "Coptic": "cop",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Divehi (Maldivian)": "dv",
    "Dutch": "nl",
    "English": "en",
    "English (USA)": "en",
    "English (UK)": "en",
    "English (Australia)": "en",
    "English (Canada)": "en",
    "English (New Zealand)": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Farsi": "fa",
    "Finnish": "fi",
    "French": "fr",
    "French (Canada)": "fr",
    "Galician": "gl",
    "German": "de",
    "German (Austria)": "de",
    "German (Austria, old spelling)": "de",
    "German (old spelling)": "de",
    "German (Switzerland)": "de",
    "Greek": "el",
    "Greek (ancient)": "el",
    "Greek (polytonic)": "el",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Interlingua": "ia",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Japanese (CJK)": "ja",
    "Kazakh": "kk",
    "Korean": "ko",
    "Kurmanji": "ku",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Lower Sorbian": "dsb",
    "Malay": "ms",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Norwegian (Bokmål)": "nb",
    "Norwegian (Bokmaal)": "nb",
    "Norwegian (Nynorsk)": "nn",
    "Occitan": "oc",
    "Polish": "pl",
    "Portuguese": "pt",
    "Portuguese (Brazil)": "pt",
    "Romanian": "ro",
    "Russian": "ru",
    "Russian (Petrine orthography)": "ru",
    "North Sami": "se",
    "Sanskrit": "sa",
    "Scottish": "gd",
    "Serbian": "sr",
    "Serbian (Latin)": "sr",
    "Slovak": "sk",
    "Slovene": "sl",
    "Spanish": "es",
    "Spanish (Mexico)": "es",
    "Swedish": "sv",
    "Syriac": "syc",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Ukrainian": "uk",
    "Upper Sorbian": "hsb",
    "Urdu": "ur",
    "Vietnamese": "vi",
}

# All module codes that have dedicated rule files (for locale resolution)
_LOCALE_MODULES = frozenset({
    "af", "sq", "ar", "hy", "eu", "be", "br", "bg", "ca", "zh", "hr", "cs", "da",
    "dv", "eo", "et", "fa", "fi", "gl", "el", "he", "hi", "hu", "is", "id", "ia", "ga",
    "ja", "kk", "ko", "ku", "lo", "la", "lv", "lt", "dsb", "ms", "mr", "mn",
    "nb", "nn", "oc", "pl", "ro", "ru", "se", "sa", "gd", "sr", "sk", "sl",
    "sv", "ta", "te", "th", "tr", "tk", "uk", "hsb", "ur", "vi", "cop", "syc",
    "en", "fr", "de", "es", "it", "pt", "nl",
})


def _empty_error_types() -> list:
    """Return empty rule list for languages without custom lyx-gc rules."""
    return []


def resolve_language(lang: str) -> str | None:
    """Resolve language to rule module key or None.

    Accepts:
    - LANG locale: "en_US.UTF-8", "fr_FR", "de_DE.UTF-8", "pl_PL", "nb_NO", etc.
    - Short code: "en", "fr", "de", "pl", "nb", "dsb", etc.
    - LyX language name: "English (USA)", "French (Canada)", "Polish"
    """
    if not lang or not isinstance(lang, str):
        return None
    lang = lang.strip()
    if not lang:
        return None

    # Direct LyX name lookup
    if lang in LYX_LANGUAGE_TO_MODULE:
        return LYX_LANGUAGE_TO_MODULE[lang]

    lang_lower = lang.lower()

    # 3-letter locale codes (must be checked before lang[:2])
    for prefix in ("dsb", "hsb", "syc", "cop"):
        if lang_lower.startswith(prefix):
            return prefix if prefix in _LOCALE_MODULES else "generic"

    # 2-letter codes: nb, nn (Norwegian variants)
    if lang_lower.startswith("nb"):
        return "nb"
    if lang_lower.startswith("nn"):
        return "nn"

    # LANG locale: en_US.UTF-8 -> en, fr_CA -> fr, pl_PL -> pl, etc.
    short = lang_lower[:2]
    if short in _LOCALE_MODULES:
        return short
    if len(short) == 2 and short.isalpha():
        return "generic"
    return None


def get_generate_error_types(rule_module: str | None):
    """Return generate_error_types callable for the given rule module.

    Loads rules from JSON data files via the loader (no executable code).
    """
    if rule_module is None:
        return _empty_error_types

    from .loader import load_language

    def _generate_error_types() -> list:
        return load_language(rule_module)

    return _generate_error_types
