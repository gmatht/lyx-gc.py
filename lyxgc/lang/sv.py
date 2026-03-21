"""Swedish grammar rules - LaTeX structural rules with Swedish messages."""
from ._structural import structural_rules
from ..rules import simple_rule

_MSGS = {
    "empty_mathblock": ("Tomt matematikblock", ""),
    "macro_no_brace": ("Makro utan {}", "Ett {} behövs troligen efter makrot."),
    "no_fullstop_after_cite": ("Ingen punkt efter citat vid styckeslut", "En punkt kan saknas."),
    "no_space_after_cite": ("Inget mellanslag efter citat", ""),
    "no_space_before_cite": ("Inget mellanslag före citat", ""),
    "uline_starts_early": ("Understrukna raden börjar för tidigt", ""),
    "uline_ends_late": ("Understrukna raden slutar för sent", ""),
    "space_before_footnote": ("Mellanslag före fotnot", ""),
    "footnote_period_comma": ("Punkt/komma efter fotnot", "Om fotnoten avser hela meningen, placera den efter punkten."),
    "double_punct": ("Dubbel interpunktion", ""),
    "implies_in_proof": ("Användning av \\implies i bevis", "Använd \\Longrightarrow för bevisriktningen."),
    "no_space_after_ref": ("Inget mellanslag efter referens", ""),
    "single_char": ("Ett enskilt tecken", "Ett enskilt tecken har vanligtvis ingen mening."),
    "empty_begin_end": ("Tomt begin/end-block", ""),
    "proof_not_newline": ("Beviset börjar inte på ny rad", "Infoga styckeavbrott mellan sats och bevis (Enter i LyX)."),
    "no_space_ref_left": ("Inget mellanslag till vänster om referensen", "Kanske ett icke-brytande mellanslag (~) före referensen?"),
    "no_space_ref_right": ("Inget mellanslag till höger om referensen", "Kanske ett icke-brytande mellanslag (~) efter referensen?"),
    "too_many_dots": ("För många punkter", "Varför mer än en '.'?"),
    "space_cite_punct": ("Mellanslag mellan citat och interpunktion", ""),
    "space_after_period_cap": ("Manglade mellanslag mellan punkt och stor bokstav", ""),
    "space_after_period_word": ("Manglade mellanslag mellan punkt och ord", ""),
    "textquotedbl": ("Felaktig användning av \\textquotedbl", "Använd `` eller ''."),
    "math_punct": ("Mellanslag mellan matematikblock och interpunktion", ""),
    "cap_after_math": ("Stor bokstav efter matematikblock", "Varför stor bokstav efter matematikblocket?"),
    "equals_outside_math": ("Likhetstecken utanför matematikblock", "'=' bör vara inom matematikblocket."),
    "no_space_before_math": ("Inget mellanslag före matematikblock", ""),
    "no_space_before_cite": ("Inget mellanslag före citat", ""),
    "footnote_no_stop": ("Fotnot utan punkt", ""),
    "no_space_after_math": ("Inget mellanslag efter matematikblock", ""),
    "no_space_before_macro": ("Inget mellanslag före makro", ""),
    "no_space_after_macro": ("Inget mellanslag efter makro", ""),
    "colon_in_math": (": i matematikläge", "Använd \\colon för att definiera funktioner."),
    "ugly_fraction": ("Ful bråkdel", r"Använd \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("För många nollor utan avgränsare", ""),
    "duplicated_word": ("Dubblerat ord", ""),
    "para_no_stop": ("Stycket slutar utan punkt", ""),
    "para_no_cap": ("Stycket börjar utan stor bokstav", ""),
    "para_starts_dot": ("Stycket börjar med punkt?", ""),
    "punct_in_math": ("Interpunktion inom matematikläge", "Flytta ARG1 utanför matematikläge."),
    "double_dot": ("Dubbel punkt", "En punkt räcker."),
    "space_before_punct_math": ("Mellanslag före matematikblockets slut", ""),
    "space_before_rparen": ("Mellanslag före )", ""),
    "proof_no_begin": ("\\end{proof} utan \\begin", "Ta bort styckeavbrott före \\end{proof}?"),
    "section_has_dot": ("Avsnitt med punkt", "Avsnitt slutar vanligtvis inte med punkt."),
    "no_stop_def": ("Ingen punkt före \\end{definition}", ""),
    "no_stop_end": ("Ingen punkt före \\end{...}", ""),
}


def _swedish_specific_rules() -> list:
    """Top 20 Swedish grammatical/typographical errors."""
    return [
        simple_rule("tillochmed", "till och med"),
        simple_rule("iställetför", "i stället för"),
        simple_rule("aldrig inte", "aldrig"),
        simple_rule("nån", "någon"),
        simple_rule("framförallt", "framför allt"),
        simple_rule("sjuk sköterska", "sjuksköterska"),
        simple_rule("läder bälte", "läderbälte"),
        simple_rule("såvida", "så vida"),
        simple_rule("definera", "definiera"),
        simple_rule("seperat", "separat"),
        simple_rule("accomodera", "ackommodera"),
        simple_rule("minimisera", "minimera"),
        simple_rule("maximisera", "maximera"),
        simple_rule("tehnik", "teknik"),
        simple_rule("kommittera", "committera"),
        simple_rule("imlementera", "implementera"),
    ]


def generate_error_types() -> list:
    """Return Swedish rules."""
    return structural_rules(_MSGS) + _swedish_specific_rules()
