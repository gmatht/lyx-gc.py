"""Norwegian Bokmål grammar rules - LaTeX structural rules with Norwegian Bokmål messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Tom matematisk blokk", ""),
    "macro_no_brace": ("Makro uten {}", "En {} trengs sannsynligvis etter makroen."),
    "no_fullstop_after_cite": ("Mangler punktum etter sitat ved avsnittsslutt", "Et punktum mangler kanskje."),
    "no_space_after_cite": ("Ingen mellomrom etter sitat", ""),
    "no_space_before_cite": ("Ingen mellomrom før sitat", ""),
    "uline_starts_early": ("Understreking starter for tidlig", ""),
    "uline_ends_late": ("Understreking slutter for sent", ""),
    "space_before_footnote": ("Mellomrom før fotnote", ""),
    "footnote_period_comma": ("Punktum/komma etter fotnote", "Hvis fotnoten refererer til hele setningen, plasser den etter punktum."),
    "double_punct": ("Dobbel tegnsetting", ""),
    "implies_in_proof": ("Bruk av \\implies i bevis", "Bruk \\Longrightarrow for bevisretningen."),
    "no_space_after_ref": ("Ingen mellomrom etter referanse", ""),
    "single_char": ("Enkelt tegn", "Ett enkelt tegn gir vanligvis ikke mening."),
    "empty_begin_end": ("Tom begin/end-blokk", ""),
    "proof_not_newline": ("Bevis starter ikke på ny linje", "Sett inn avsnittsskiller mellom setning og bevis (Enter i LyX)."),
    "no_space_ref_left": ("Ingen mellomrom til venstre for referanse", "Kanskje et ikke-brytende mellomrom (~) før referansen?"),
    "no_space_ref_right": ("Ingen mellomrom til høyre for referanse", "Kanskje et ikke-brytende mellomrom (~) etter referansen?"),
    "too_many_dots": ("For mange punkter", "Hvorfor mer enn ett '.'?"),
    "space_cite_punct": ("Mellomrom mellom sitat og tegnsetting", ""),
    "space_after_period_cap": ("Manglende mellomrom mellom punktum og stor bokstav", ""),
    "space_after_period_word": ("Manglende mellomrom mellom punktum og ord", ""),
    "textquotedbl": ("Feil bruk av \\textquotedbl", "Bruk `` eller ''."),
    "math_punct": ("Mellomrom mellom matematisk blokk og tegnsetting", ""),
    "cap_after_math": ("Stor bokstav etter matematisk blokk", "Hvorfor stor bokstav etter den matematiske blokken?"),
    "equals_outside_math": ("Likhetstegn utenfor matematisk blokk", "'=' bør være inne i den matematiske blokken."),
    "no_space_before_math": ("Ingen mellomrom før matematisk blokk", ""),
    "no_space_before_cite": ("Ingen mellomrom før sitat", ""),
    "footnote_no_stop": ("Fotnote uten punktum", ""),
    "no_space_after_math": ("Ingen mellomrom etter matematisk blokk", ""),
    "no_space_before_macro": ("Ingen mellomrom før makro", ""),
    "no_space_after_macro": ("Ingen mellomrom etter makro", ""),
    "colon_in_math": (": i matematisk modus", "Bruk \\colon for å definere funksjoner."),
    "ugly_fraction": ("Stygg brøk", r"Bruk \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("For mange nuller uten skilletegn", ""),
    "duplicated_word": ("Dobbel ord", ""),
    "para_no_stop": ("Avsnitt slutter uten punktum", ""),
    "para_no_cap": ("Avsnitt starter uten stor bokstav", ""),
    "para_starts_dot": ("Avsnitt starter med punktum?", ""),
    "punct_in_math": ("Tegnsetting inni matematisk modus", "Flytt ARG1 ut av matematisk modus."),
    "double_dot": ("Dobbel punktum", "Ett punktum er nok."),
    "space_before_punct_math": ("Mellomrom før slutten av matematisk blokk", ""),
    "space_before_rparen": ("Mellomrom før )", ""),
    "proof_no_begin": ("\\end{proof} uten \\begin", "Fjern avsnittsskiller før \\end{proof}?"),
    "section_has_dot": ("Seksjon med punktum", "Seksjoner slutter vanligvis ikke med punktum."),
    "no_stop_def": ("Ingen punktum før \\end{definition}", ""),
    "no_stop_end": ("Ingen punktum før \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Norwegian Bokmål rules."""
    return structural_rules(_MSGS) + common_academic_rules()
