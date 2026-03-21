"""Danish grammar rules - LaTeX structural rules with Danish messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Tom matematikblok", ""),
    "macro_no_brace": ("Makro uden {}", "En {} er sandsynligvis nødvendig efter makroen."),
    "no_fullstop_after_cite": ("Manglende punktum efter henvisning ved afsnitsslutning", "Et punktum mangler muligvis."),
    "no_space_after_cite": ("Intet mellemrum efter henvisning", ""),
    "no_space_before_cite": ("Intet mellemrum før henvisning", ""),
    "uline_starts_early": ("Understregning starter for tidligt", ""),
    "uline_ends_late": ("Understregning slutter for sent", ""),
    "space_before_footnote": ("Mellemrum før fodnote", ""),
    "footnote_period_comma": ("Punktum/komma efter fodnote", "Hvis fodnoten henviser til hele sætningen, placer den efter punktum."),
    "double_punct": ("Dobbelt tegnsætning", ""),
    "implies_in_proof": ("Brug af \\implies i bevis", "Brug \\Longrightarrow til bevisretningen."),
    "no_space_after_ref": ("Intet mellemrum efter reference", ""),
    "single_char": ("Ét enkelt tegn", "Et enkelt tegn giver normalt ikke mening."),
    "empty_begin_end": ("Tom begin/end-blok", ""),
    "proof_not_newline": ("Bevis starter ikke på ny linje", "Indsæt afsnitsskille mellem sætning og bevis (Enter i LyX)."),
    "no_space_ref_left": ("Intet mellemrum til venstre for reference", "Måske et ubrudt mellemrum (~) før reference?"),
    "no_space_ref_right": ("Intet mellemrum til højre for reference", "Måske et ubrudt mellemrum (~) efter reference?"),
    "too_many_dots": ("For mange punktummer", "Hvorfor mere end ét '.'?"),
    "space_cite_punct": ("Mellemrum mellem henvisning og tegnsætning", ""),
    "space_after_period_cap": ("Manglende mellemrum mellem punktum og stort bogstav", ""),
    "space_after_period_word": ("Manglende mellemrum mellem punktum og ord", ""),
    "textquotedbl": ("Forkert brug af \\textquotedbl", "Brug `` eller ''."),
    "math_punct": ("Mellemrum mellem matematikblok og tegnsætning", ""),
    "cap_after_math": ("Stort bogstav efter matematikblok", "Hvorfor stort bogstav efter matematikblokken?"),
    "equals_outside_math": ("Lighedstegn uden for matematikblok", "'=' bør være inde i matematikblokken."),
    "no_space_before_math": ("Intet mellemrum før matematikblok", ""),
    "no_space_before_cite": ("Intet mellemrum før henvisning", ""),
    "footnote_no_stop": ("Fodnote uden punktum", ""),
    "no_space_after_math": ("Intet mellemrum efter matematikblok", ""),
    "no_space_before_macro": ("Intet mellemrum før makro", ""),
    "no_space_after_macro": ("Intet mellemrum efter makro", ""),
    "colon_in_math": (": i matematiktilstand", "Brug \\colon til at definere funktioner."),
    "ugly_fraction": ("Grim brøk", r"Brug \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("For mange nuller uden separator", ""),
    "duplicated_word": ("Gentaget ord", ""),
    "para_no_stop": ("Afsnit slutter uden punktum", ""),
    "para_no_cap": ("Afsnit starter uden stort bogstav", ""),
    "para_starts_dot": ("Afsnit starter med punktum?", ""),
    "punct_in_math": ("Tegnsætning inde i matematiktilstand", "Flyt ARG1 ud af matematiktilstand."),
    "double_dot": ("Dobbelt punktum", "Ét punktum er nok."),
    "space_before_punct_math": ("Mellemrum før slutningen af matematikblok", ""),
    "space_before_rparen": ("Mellemrum før )", ""),
    "proof_no_begin": ("\\end{proof} uden \\begin", "Fjern afsnitsskille før \\end{proof}?"),
    "section_has_dot": ("Afsnit med punktum", "Afsnit slutter normalt ikke med punktum."),
    "no_stop_def": ("Intet punktum før \\end{definition}", ""),
    "no_stop_end": ("Intet punktum før \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Danish rules."""
    return structural_rules(_MSGS) + common_academic_rules()
