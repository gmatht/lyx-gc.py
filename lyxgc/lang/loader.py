"""Load language rules from JSON data files. No executable code in data."""
import json
from pathlib import Path

from ._structural import structural_rules
from ..rules import simple_rule, set_diff, generate_vowel_regex
from ..tokenizer import (
    START_MATH_CHAR,
    END_MATH_CHAR,
    RECURSIVE_BRACE,
    MATHBLOCK,
    NOTINMATH,
    PAR,
    MACROBLOCK,
    LATEX_BS,
)


# Placeholders mapped to tokenizer/rules values
def _build_placeholder_map() -> dict[str, str]:
    endnumber = r"(?=[^0-9]|$)"
    funnynumber = r"(?:11|18)(?:[0-9]{2})?(?:[0-9]{3})*" + endnumber
    vowelnumber = r"\b(?:8[0-9]*" + endnumber + "|" + funnynumber + ")"
    consonantnumber = r"\b(?!" + funnynumber + r")[012345679][0-9]*" + endnumber

    SetOfVowels = {
        "l": "aeiou",
        "U": "FHILMANXAEIOS",
        "d": "8",
        "number": vowelnumber,
        "includewords": r"(?:MF|NP|NL|LP|MPC|RTL|RMS|heir|RME|ME|heirloom|honest|honor|honorable|honorarium|honorary|honorific|honour|hour|hourglass|hourly|HTML|XML|FBI|SGML|SDL|HAA|LTL|SAA|S5|FSA|SSPM)",
        "excludewords": r"(?:US[a-zA-Z]*|Eur[a-zA-Z]*|Unix|eurhythmic|eurhythmy|euripus|one|unary|US|usage|useful|user|UK|unanimous|utrees?|uni[a-zA-Z]*|util[a-zA-Z]*|usual)",
        "s": "=",
        "isvowelset": True,
    }
    SetOfConsonants = {
        "l": set_diff("abcdefghijklmnopqrstuvwxyz", SetOfVowels["l"]),
        "U": set_diff("ABCDEFGHIJKLMNOPQRSTUVWXYZ", SetOfVowels["U"]),
        "d": set_diff("0123456789", SetOfVowels["d"]),
        "number": consonantnumber,
        "includewords": SetOfVowels["excludewords"],
        "excludewords": SetOfVowels["includewords"],
        "s": "+-<>#",
        "isvowelset": False,
    }

    return {
        "{{LBS}}": LATEX_BS,
        "{{START_MATH_CHAR}}": START_MATH_CHAR,
        "{{END_MATH_CHAR}}": END_MATH_CHAR,
        "{{MATHBLOCK}}": MATHBLOCK,
        "{{PAR}}": PAR,
        "{{RECURSIVE_BRACE}}": RECURSIVE_BRACE,
        "{{MACROBLOCK}}": MACROBLOCK,
        "{{NOTINMATH}}": NOTINMATH,
        "{{VOWEL_SOUND_EN}}": generate_vowel_regex(SetOfVowels),
        "{{CONSONANT_SOUND_EN}}": generate_vowel_regex(SetOfConsonants),
    }


_PLACEHOLDERS = _build_placeholder_map()

# Common academic misspellings (from _common.py) for languages with common_rules
_COMMON_ACADEMIC_SIMPLE_RULES = [
    ["concensus", "consensus"],
    ["occurence", "occurrence"],
    ["seperately", "separately"],
    ["definately", "definitely"],
    ["accomodate", "accommodate"],
    ["refered", "referred"],
    ["occured", "occurred"],
    ["tommorow", "tomorrow"],
    ["reccomend", "recommend"],
    ["neccesary", "necessary"],
    ["acheive", "achieve"],
    ["occuring", "occurring"],
    ["seperate", "separate"],
    ["independant", "independent"],
    ["recieve", "receive"],
    ["beleive", "believe"],
    ["wierd", "weird"],
    ["thier", "their"],
    ["teh", "the"],
    ["taht", "that"],
]


def _substitute_placeholders(s: str) -> str:
    """Replace {{PLACEHOLDER}} with actual values."""
    result = s
    for placeholder, value in _PLACEHOLDERS.items():
        result = result.replace(placeholder, value)
    return result


def _get_data_path(rule_module: str) -> Path:
    """Resolve path to lang/data/{rule_module}.json."""
    return Path(__file__).parent / "data" / f"{rule_module}.json"


def load_language(rule_module: str) -> list:
    """Load rules from lang/data/{rule_module}.json.

    Supports:
    - msgs + optional simple_rules: structural rules + language-specific simple rules
    - msgs + optional common_rules: structural rules + common academic misspellings
    - custom_rules: full [name, regex, special, desc] list with placeholder substitution
    """
    path = _get_data_path(rule_module)
    if not path.exists():
        return []

    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    rules: list = []

    if "msgs" in data:
        msgs = data["msgs"]
        # Convert list values to tuples for structural_rules
        msgs_dict = {k: (v[0], v[1]) if isinstance(v, list) else v for k, v in msgs.items()}
        rules.extend(structural_rules(msgs_dict))

        for pair in data.get("simple_rules", []):
            bad, good = pair[0], pair[1] if len(pair) > 1 else None
            rules.append(simple_rule(bad, good))

        if data.get("common_rules"):
            for bad, good in _COMMON_ACADEMIC_SIMPLE_RULES:
                rules.append(simple_rule(bad, good))

    if "custom_rules" in data:
        for rule in data["custom_rules"]:
            name = rule[0]
            regex = _substitute_placeholders(rule[1])
            special = _substitute_placeholders(rule[2]) if len(rule) > 2 else ""
            desc = rule[3] if len(rule) > 3 else ""
            rules.append([name, regex, special, desc])

    return rules
