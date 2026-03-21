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
    """Return generate_error_types callable for the given rule module."""
    if rule_module is None:
        return _empty_error_types

    # Lazy imports for all language modules
    _MODULE_IMPORTS = {
        "af": ("lyxgc.lang.af", "generate_error_types"),
        "sq": ("lyxgc.lang.sq", "generate_error_types"),
        "ar": ("lyxgc.lang.ar", "generate_error_types"),
        "hy": ("lyxgc.lang.hy", "generate_error_types"),
        "eu": ("lyxgc.lang.eu", "generate_error_types"),
        "be": ("lyxgc.lang.be", "generate_error_types"),
        "br": ("lyxgc.lang.br", "generate_error_types"),
        "bg": ("lyxgc.lang.bg", "generate_error_types"),
        "ca": ("lyxgc.lang.ca", "generate_error_types"),
        "zh": ("lyxgc.lang.zh", "generate_error_types"),
        "hr": ("lyxgc.lang.hr", "generate_error_types"),
        "cs": ("lyxgc.lang.cs", "generate_error_types"),
        "da": ("lyxgc.lang.da", "generate_error_types"),
        "dv": ("lyxgc.lang.dv", "generate_error_types"),
        "eo": ("lyxgc.lang.eo", "generate_error_types"),
        "et": ("lyxgc.lang.et", "generate_error_types"),
        "fa": ("lyxgc.lang.fa", "generate_error_types"),
        "fi": ("lyxgc.lang.fi", "generate_error_types"),
        "gl": ("lyxgc.lang.gl", "generate_error_types"),
        "el": ("lyxgc.lang.el", "generate_error_types"),
        "he": ("lyxgc.lang.he", "generate_error_types"),
        "hi": ("lyxgc.lang.hi", "generate_error_types"),
        "hu": ("lyxgc.lang.hu", "generate_error_types"),
        "is": ("lyxgc.lang.is", "generate_error_types"),
        "id": ("lyxgc.lang.id", "generate_error_types"),
        "ia": ("lyxgc.lang.ia", "generate_error_types"),
        "ga": ("lyxgc.lang.ga", "generate_error_types"),
        "ja": ("lyxgc.lang.ja", "generate_error_types"),
        "kk": ("lyxgc.lang.kk", "generate_error_types"),
        "ko": ("lyxgc.lang.ko", "generate_error_types"),
        "ku": ("lyxgc.lang.ku", "generate_error_types"),
        "lo": ("lyxgc.lang.lo", "generate_error_types"),
        "la": ("lyxgc.lang.la", "generate_error_types"),
        "lv": ("lyxgc.lang.lv", "generate_error_types"),
        "lt": ("lyxgc.lang.lt", "generate_error_types"),
        "dsb": ("lyxgc.lang.dsb", "generate_error_types"),
        "ms": ("lyxgc.lang.ms", "generate_error_types"),
        "mr": ("lyxgc.lang.mr", "generate_error_types"),
        "mn": ("lyxgc.lang.mn", "generate_error_types"),
        "nb": ("lyxgc.lang.nb", "generate_error_types"),
        "nn": ("lyxgc.lang.nn", "generate_error_types"),
        "oc": ("lyxgc.lang.oc", "generate_error_types"),
        "pl": ("lyxgc.lang.pl", "generate_error_types"),
        "ro": ("lyxgc.lang.ro", "generate_error_types"),
        "ru": ("lyxgc.lang.ru", "generate_error_types"),
        "se": ("lyxgc.lang.se", "generate_error_types"),
        "sa": ("lyxgc.lang.sa", "generate_error_types"),
        "gd": ("lyxgc.lang.gd", "generate_error_types"),
        "sr": ("lyxgc.lang.sr", "generate_error_types"),
        "sk": ("lyxgc.lang.sk", "generate_error_types"),
        "sl": ("lyxgc.lang.sl", "generate_error_types"),
        "sv": ("lyxgc.lang.sv", "generate_error_types"),
        "ta": ("lyxgc.lang.ta", "generate_error_types"),
        "te": ("lyxgc.lang.te", "generate_error_types"),
        "th": ("lyxgc.lang.th", "generate_error_types"),
        "tr": ("lyxgc.lang.tr", "generate_error_types"),
        "tk": ("lyxgc.lang.tk", "generate_error_types"),
        "uk": ("lyxgc.lang.uk", "generate_error_types"),
        "hsb": ("lyxgc.lang.hsb", "generate_error_types"),
        "ur": ("lyxgc.lang.ur", "generate_error_types"),
        "vi": ("lyxgc.lang.vi", "generate_error_types"),
        "cop": ("lyxgc.lang.cop", "generate_error_types"),
        "syc": ("lyxgc.lang.syc", "generate_error_types"),
        "en": ("lyxgc.lang.en", "generate_error_types"),
        "fr": ("lyxgc.lang.fr", "generate_error_types"),
        "de": ("lyxgc.lang.de", "generate_error_types"),
        "es": ("lyxgc.lang.es", "generate_error_types"),
        "it": ("lyxgc.lang.it", "generate_error_types"),
        "pt": ("lyxgc.lang.pt", "generate_error_types"),
        "nl": ("lyxgc.lang.nl", "generate_error_types"),
        "generic": ("lyxgc.lang.generic", "generate_error_types"),
    }

    if rule_module in _MODULE_IMPORTS:
        mod_path, attr = _MODULE_IMPORTS[rule_module]
        import importlib
        mod = importlib.import_module(mod_path)
        return getattr(mod, attr)
    return _empty_error_types
