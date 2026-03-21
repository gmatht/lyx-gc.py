"""Afrikaans grammar rules - LaTeX structural rules with Afrikaans messages."""
from ._structural import structural_rules
from ..rules import simple_rule

_MSGS = {
    "empty_mathblock": ("Leë wiskunde-blok", ""),
    "macro_no_brace": ("Makro sonder {}", "'n {} is waarskynlik na die makro nodig."),
    "no_fullstop_after_cite": ("Geen punt na aanhaling aan paragraaf-einde", "'n Punt ontbreek moontlik."),
    "no_space_after_cite": ("Geen spasie na aanhaling", ""),
    "no_space_before_cite": ("Geen spasie voor aanhaling", ""),
    "uline_starts_early": ("Onderstreep begin te vroeg", ""),
    "uline_ends_late": ("Onderstreep eindig te laat", ""),
    "space_before_footnote": ("Spasie voor voetnoot", ""),
    "footnote_period_comma": ("Punt/komma na voetnoot", "As die voetnoot na die hele sin verwys, plaas dit na die punt."),
    "double_punct": ("Dubbele leestekens", ""),
    "implies_in_proof": ("Gebruik van \\implies in bewys", "Gebruik \\Longrightarrow vir die bewysrigting."),
    "no_space_after_ref": ("Geen spasie na verwysing", ""),
    "single_char": ("Enkele karakter", "'n Enkele karakter maak gewoonlik geen sin nie."),
    "empty_begin_end": ("Leë begin/end-blok", ""),
    "proof_not_newline": ("Bewys begin nie op nuwe reël", "Voeg paragraaf-einde in tussen stelling en bewys (Enter in LyX)."),
    "no_space_ref_left": ("Geen spasie voor verwysing", "Miskien 'n nie-breekbare spasie (~) voor die verwysing?"),
    "no_space_ref_right": ("Geen spasie na verwysing", "Miskien 'n nie-breekbare spasie (~) na die verwysing?"),
    "too_many_dots": ("Te veel punte", "Waarom meer as een '.'?"),
    "space_cite_punct": ("Spasie tussen aanhaling en leestekens", ""),
    "space_after_period_cap": ("Ontbrekende spasie tussen punt en hoofletter", ""),
    "space_after_period_word": ("Ontbrekende spasie tussen punt en woord", ""),
    "textquotedbl": ("Verkeerde gebruik van \\textquotedbl", "Gebruik `` of ''."),
    "math_punct": ("Spasie tussen wiskunde-blok en leestekens", ""),
    "cap_after_math": ("Hoofletter na wiskunde-blok", "Waarom 'n hoofletter na die wiskunde-blok?"),
    "equals_outside_math": ("Gelykteken buite wiskunde-blok", "Die '=' behoort binne die wiskunde-blok te wees."),
    "no_space_before_math": ("Geen spasie voor wiskunde-blok", ""),
    "no_space_before_cite": ("Geen spasie voor aanhaling", ""),
    "footnote_no_stop": ("Voetnoot sonder punt", ""),
    "no_space_after_math": ("Geen spasie na wiskunde-blok", ""),
    "no_space_before_macro": ("Geen spasie voor makro", ""),
    "no_space_after_macro": ("Geen spasie na makro", ""),
    "colon_in_math": (": in wiskunde-modus", "Gebruik \\colon vir funksiedefinisies."),
    "ugly_fraction": ("Lelijke breuk", r"Gebruik \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Te veel nulle sonder skeider", ""),
    "duplicated_word": ("Dubbel woord", ""),
    "para_no_stop": ("Paragraaf eindig sonder punt", ""),
    "para_no_cap": ("Paragraaf begin sonder hoofletter", ""),
    "para_starts_dot": ("Paragraaf begin met punt?", ""),
    "punct_in_math": ("Leestekens binne wiskunde-modus", "Skuif ARG1 buite wiskunde-modus."),
    "double_dot": ("Dubbele punte", "Een punt is voldoende."),
    "space_before_punct_math": ("Spasie voor einde wiskunde-blok", ""),
    "space_before_rparen": ("Spasie voor )", ""),
    "proof_no_begin": ("\\end{proof} sonder \\begin", "Verwyder paragraaf-einde voor \\end{proof}?"),
    "section_has_dot": ("Section met punt", "Sections eindig gewoonlik nie met 'n punt nie."),
    "no_stop_def": ("Geen punt voor \\end{definition}", ""),
    "no_stop_end": ("Geen punt voor \\end{...}", ""),
}


def _afrikaans_specific_rules() -> list:
    """Top 20 Afrikaans grammatical/typographical errors."""
    return [
        simple_rule("concensus", "consensus"),
        simple_rule("occurence", "occurrence"),
        simple_rule("seperately", "separately"),
        simple_rule("definately", "definitely"),
        simple_rule("accomodate", "accommodate"),
        simple_rule("refered", "referred"),
        simple_rule("occured", "occurred"),
        simple_rule("tommorow", "tomorrow"),
        simple_rule("reccomend", "recommend"),
        simple_rule("neccesary", "necessary"),
    ]


def generate_error_types() -> list:
    """Return Afrikaans rules."""
    return structural_rules(_MSGS) + _afrikaans_specific_rules()
