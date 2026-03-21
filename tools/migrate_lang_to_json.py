#!/usr/bin/env python3
"""One-time migration: convert language .py modules to JSON data files."""
import json
import re
import sys
from pathlib import Path

# Add py to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Build placeholder map (same as loader) - values to replace with placeholders
from lyxgc.tokenizer import (
    START_MATH_CHAR,
    END_MATH_CHAR,
    RECURSIVE_BRACE,
    MATHBLOCK,
    NOTINMATH,
    PAR,
    MACROBLOCK,
    LATEX_BS,
)
from lyxgc.rules import set_diff, generate_vowel_regex


def _build_reverse_placeholders():
    endnumber = r"(?=[^0-9]|$)"
    funnynumber = r"(?:11|18)(?:[0-9]{2})?(?:[0-9]{3})*" + endnumber
    vowelnumber = r"\b(?:8[0-9]*" + endnumber + "|" + funnynumber + ")"
    consonantnumber = r"\b(?!" + funnynumber + r")[012345679][0-9]*" + endnumber
    SetOfVowels = {
        "l": "aeiou", "U": "FHILMANXAEIOS", "d": "8",
        "number": vowelnumber,
        "includewords": r"(?:MF|NP|NL|LP|MPC|RTL|RMS|heir|RME|ME|heirloom|honest|honor|honorable|honorarium|honorary|honorific|honour|hour|hourglass|hourly|HTML|XML|FBI|SGML|SDL|HAA|LTL|SAA|S5|FSA|SSPM)",
        "excludewords": r"(?:US[a-zA-Z]*|Eur[a-zA-Z]*|Unix|eurhythmic|eurhythmy|euripus|one|unary|US|usage|useful|user|UK|unanimous|utrees?|uni[a-zA-Z]*|util[a-zA-Z]*|usual)",
        "s": "=", "isvowelset": True,
    }
    SetOfConsonants = {
        "l": set_diff("abcdefghijklmnopqrstuvwxyz", SetOfVowels["l"]),
        "U": set_diff("ABCDEFGHIJKLMNOPQRSTUVWXYZ", SetOfVowels["U"]),
        "d": set_diff("0123456789", SetOfVowels["d"]),
        "number": consonantnumber,
        "includewords": SetOfVowels["excludewords"],
        "excludewords": SetOfVowels["includewords"],
        "s": "+-<>#", "isvowelset": False,
    }
    return [
        (generate_vowel_regex(SetOfVowels), "{{VOWEL_SOUND_EN}}"),
        (generate_vowel_regex(SetOfConsonants), "{{CONSONANT_SOUND_EN}}"),
        (RECURSIVE_BRACE, "{{RECURSIVE_BRACE}}"),
        (MATHBLOCK, "{{MATHBLOCK}}"),
        (NOTINMATH, "{{NOTINMATH}}"),
        (PAR, "{{PAR}}"),
        (MACROBLOCK, "{{MACROBLOCK}}"),
        (END_MATH_CHAR, "{{END_MATH_CHAR}}"),
        (START_MATH_CHAR, "{{START_MATH_CHAR}}"),
        (LATEX_BS, "{{LBS}}"),
    ]


_REVERSE_PLACEHOLDERS = _build_reverse_placeholders()


def to_placeholder_form(s: str) -> str:
    """Replace computed values with placeholders for JSON storage."""
    result = s
    for value, placeholder in _REVERSE_PLACEHOLDERS:
        result = result.replace(value, placeholder)
    return result


def simple_rule_to_pair(rule: list) -> tuple[str, str | None] | None:
    """Extract (bad, good) from simple_rule output if possible."""
    if len(rule) < 2:
        return None
    name, regex, special, desc = rule[0], rule[1], rule[2] if len(rule) > 2 else "", rule[3] if len(rule) > 3 else ""
    if special != "":
        return None
    m = re.search(r"Perhaps you mean '([^']*)'\?", desc)
    good = m.group(1) if m else (None if desc else None)
    # simple_rule uses bad as name for simple bad->good rules
    return (name, good)


def migrate_module(module_id: str) -> dict | None:
    """Import module and convert to JSON-serializable dict."""
    import importlib
    import inspect
    try:
        mod = importlib.import_module(f"lyxgc.lang.{module_id}")
    except Exception as e:
        print(f"  Skip {module_id}: {e}")
        return None

    if not hasattr(mod, "generate_error_types"):
        return None

    gen = getattr(mod, "generate_error_types")
    rules = gen()

    # Check if it has _MSGS (structural)
    if hasattr(mod, "_MSGS"):
        msgs = getattr(mod, "_MSGS")
        msgs_out = {}
        for k, v in msgs.items():
            msgs_out[k] = [v[0], v[1]] if isinstance(v, (tuple, list)) else [str(v[0]), str(v[1])]

        # Structural rules have fixed count; remainder are simple/common
        from lyxgc.lang.generic import _MSGS as generic_msgs
        from lyxgc.lang._structural import structural_rules
        n_structural = len(structural_rules({k: (v[0], v[1]) for k, v in generic_msgs.items()}))

        extra_rules = rules[n_structural:]
        simple_rules = []
        common_rules = False
        for r in extra_rules:
            pair = simple_rule_to_pair(r)
            if pair:
                simple_rules.append([pair[0], pair[1] if pair[1] else ""])

        # Check if module uses common_academic_rules (no language-specific simple rules)
        try:
            src = inspect.getsource(mod.generate_error_types)
            common_rules = "common_academic_rules" in src and "simple_rules" not in src
        except Exception:
            common_rules = False
        if common_rules:
            simple_rules = []

        out = {"msgs": msgs_out}
        if simple_rules:
            out["simple_rules"] = simple_rules
        if common_rules:
            out["common_rules"] = True
        return out

    # custom_rules (en, fr)
    custom_rules = []
    for r in rules:
        name = r[0]
        regex = to_placeholder_form(r[1])
        special = to_placeholder_form(r[2]) if len(r) > 2 else ""
        desc = r[3] if len(r) > 3 else ""
        custom_rules.append([name, regex, special, desc])
    return {"custom_rules": custom_rules}


def main():
    data_dir = Path(__file__).resolve().parent.parent / "lyxgc" / "lang" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    module_ids = [
        "af", "sq", "ar", "hy", "eu", "be", "br", "bg", "ca", "zh", "hr", "cs", "da",
        "dv", "eo", "et", "fa", "fi", "gl", "el", "he", "hi", "hu", "is", "id", "ia", "ga",
        "ja", "kk", "ko", "ku", "lo", "la", "lv", "lt", "dsb", "ms", "mr", "mn",
        "nb", "nn", "oc", "pl", "ro", "ru", "se", "sa", "gd", "sr", "sk", "sl",
        "sv", "ta", "te", "th", "tr", "tk", "uk", "hsb", "ur", "vi", "cop", "syc",
        "en", "fr", "de", "es", "it", "pt", "nl", "generic",
    ]
    for mid in module_ids:
        print(f"Migrating {mid}...")
        data = migrate_module(mid)
        if data:
            path = data_dir / f"{mid}.json"
            with path.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  -> {path}")
        else:
            print(f"  (skipped)")


if __name__ == "__main__":
    main()
