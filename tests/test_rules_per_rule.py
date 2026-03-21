"""Test each Perl rule fires when given triggering text.

Every rule from chktex_en.pl and chktex_fr.pl has at least one test that verifies
the rule matches when appropriate trigger text is present in the document.

Structural-only languages (de, generic, af, pl, ...) share the same LaTeX rules
from _structural.py; each has a parametrized test per rule.
"""
import io
import re

import pytest

from lyxgc.engine import find_errors
from lyxgc.lang import get_generate_error_types

generate_en = get_generate_error_types("en")
generate_fr = get_generate_error_types("fr")
from tests.rule_triggers import TRIGGERS_EN, TRIGGERS_FR
from tests.rule_triggers_structural import TRIGGERS_STRUCTURAL

# Rules with no reliable single trigger (regex overlap with other rules, or very picky patterns).
SKIP_TRIGGER_EN = frozenset()
SKIP_TRIGGER_FR = frozenset()


def _run_find_errors(error_types, trigger: str) -> tuple[int, str]:
    """Run find_errors with trigger text, return (n_errors, output)."""
    doc = r"\documentclass{article}\begin{document} " + trigger + r" \end{document}"
    out = io.StringIO()
    n = find_errors(
        error_types,
        [out],
        doc,
        "test.tex",
        min_block_size=0,
        output_format="-v0",
    )
    return n, out.getvalue()


def _rule_names_from_output(output: str) -> set[str]:
    """Extract rule names from find_errors -v0 output.

    -v0 replaces ':' in rule_id_str with '<COLON/>' (no ':' in that token), so we
    split on the first ':' after '666; ' to separate name from error text.
    """
    names: set[str] = set()
    for line in output.splitlines():
        m = re.search(r":666; (.+)$", line)
        if not m:
            continue
        rest = m.group(1)
        i = rest.find(":")
        if i < 0:
            continue
        names.add(rest[:i].replace("<COLON/>", ":"))
    return names


def _pick_trigger(rule_name: str, explicit_triggers: dict, skip: frozenset) -> str | None:
    """Return trigger for rule. Prefer explicit, else use name if it looks like plain text."""
    if rule_name in skip:
        return None
    if rule_name in explicit_triggers:
        return explicit_triggers[rule_name]
    # For simple_rule, name is often the bad phrase (trigger)
    if len(rule_name) < 55 and not any(c in rule_name for c in r"[]{}()*+?^$\.|"):
        return rule_name
    return None


def _collect_test_cases_en():
    """Yield (id, rule_name, trigger_or_none) for each EN rule."""
    rules = generate_en()
    for i, rule in enumerate(rules):
        name = rule[0]
        trigger = _pick_trigger(name, TRIGGERS_EN, SKIP_TRIGGER_EN)
        yield (f"en_{i}_{_slug(name)}", name, trigger)


def _collect_test_cases_fr():
    """Yield (id, rule_name, trigger_or_none) for each FR rule."""
    rules = generate_fr()
    for i, rule in enumerate(rules):
        name = rule[0]
        trigger = _pick_trigger(name, TRIGGERS_FR, SKIP_TRIGGER_FR)
        yield (f"fr_{i}_{_slug(name)}", name, trigger)


def _slug(s: str) -> str:
    """Short safe id from rule name."""
    return re.sub(r"[^\w]", "_", s)[:40]


# Build parametrize lists
_EN_CASES = list(_collect_test_cases_en())
_FR_CASES = list(_collect_test_cases_fr())


@pytest.mark.parametrize("rule_id,rule_name,trigger", _EN_CASES, ids=[c[0] for c in _EN_CASES])
def test_each_english_rule_fires(rule_id: str, rule_name: str, trigger: str | None) -> None:
    """Each English rule fires when given its trigger text."""
    if trigger is None:
        pytest.skip(f"No trigger for rule {rule_name!r}")
    error_types = generate_en()
    n, output = _run_find_errors(error_types, trigger)
    fired = _rule_names_from_output(output)
    assert rule_name in fired, (
        f"Rule {rule_name!r} did not fire on trigger {trigger!r}. "
        f"Fired: {fired}. Output: {output[:500]}"
    )


@pytest.mark.parametrize("rule_id,rule_name,trigger", _FR_CASES, ids=[c[0] for c in _FR_CASES])
def test_each_french_rule_fires(rule_id: str, rule_name: str, trigger: str | None) -> None:
    """Each French rule fires when given its trigger text."""
    if trigger is None:
        pytest.skip(f"No trigger for rule {rule_name!r}")
    error_types = generate_fr()
    n, output = _run_find_errors(error_types, trigger)
    fired = _rule_names_from_output(output)
    assert rule_name in fired, (
        f"Rule {rule_name!r} did not fire on trigger {trigger!r}. "
        f"Fired: {fired}. Output: {output[:500]}"
    )


# Structural-only languages: same _structural.py rules, different messages per language.
# Excludes en and fr which have custom rule implementations.
_STRUCTURAL_MODULES = [
    "de", "es", "it", "pt", "nl",
    "generic",
    "af", "sq", "ar", "hy", "eu", "be", "br", "bg", "ca", "zh", "hr", "cs", "da",
    "dv", "eo", "et", "fa", "fi", "gl", "el", "he", "hi", "hu", "is", "id", "ia", "ga",
    "ja", "kk", "ko", "ku", "lo", "la", "lv", "lt", "dsb", "ms", "mr", "mn",
    "nb", "nn", "oc", "pl", "ro", "ru", "se", "sa", "gd", "sr", "sk", "sl",
    "sv", "ta", "te", "th", "tr", "tk", "uk", "hsb", "ur", "vi", "cop", "syc",
]


def _collect_structural_test_cases():
    """Yield (module, rule_index, rule_name, trigger) for each structural rule."""
    for module in _STRUCTURAL_MODULES:
        gen = get_generate_error_types(module)
        if gen is None or gen == []:
            continue
        rules = gen()
        for i, rule in enumerate(rules):
            if i >= len(TRIGGERS_STRUCTURAL):
                break
            name = rule[0]
            trigger = TRIGGERS_STRUCTURAL[i]
            yield (f"{module}_{i}_{_slug(name)}", module, i, name, trigger)


_STRUCTURAL_CASES = list(_collect_structural_test_cases())


@pytest.mark.parametrize(
    "rule_id,module,rule_index,rule_name,trigger",
    _STRUCTURAL_CASES,
    ids=[c[0] for c in _STRUCTURAL_CASES],
)
def test_each_structural_rule_fires(
    rule_id: str, module: str, rule_index: int, rule_name: str, trigger: str
) -> None:
    """Each structural rule fires when given its trigger text (all new languages)."""
    gen = get_generate_error_types(module)
    assert gen is not None, f"No generator for {module}"
    error_types = gen()
    n, output = _run_find_errors(error_types, trigger)
    fired = _rule_names_from_output(output)
    assert rule_name in fired, (
        f"Rule {rule_name!r} (module={module}, index={rule_index}) did not fire on trigger {trigger!r}. "
        f"Fired: {fired}. Output: {output[:500]}"
    )
