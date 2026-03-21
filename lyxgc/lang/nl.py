"""Dutch grammar rules - LaTeX structural rules with Dutch messages."""
from ._structural import structural_rules
from ..rules import simple_rule

_MSGS = {
    "empty_mathblock": ("Leeg math-blok", ""),
    "macro_no_brace": ("Macro zonder {}", "Waarschijnlijk is {} nodig na de macro."),
    "no_fullstop_after_cite": ("Geen punt na citaat aan eind alinea", "Er lijkt een punt te ontbreken."),
    "no_space_after_cite": ("Geen spatie na citaat", ""),
    "no_space_before_cite": ("Geen spatie voor citaat", ""),
    "uline_starts_early": ("Onderstreping begint te vroeg", ""),
    "uline_ends_late": ("Onderstreping eindigt te laat", ""),
    "space_before_footnote": ("Spatie voor voetnoot", ""),
    "footnote_period_comma": ("Punt/komma na voetnoot", "Als de voetnoot de hele zin betreft, hoort deze na de punt."),
    "double_punct": ("Dubbele interpunctie", ""),
    "implies_in_proof": ("Gebruik van \\implies in bewijs", "Gebruik \\Longrightarrow voor de bewijsrichting."),
    "no_space_after_ref": ("Geen spatie na referentie", ""),
    "single_char": ("Enkel teken", "Een enkel teken heeft geen zin."),
    "empty_begin_end": ("Leeg begin/end-blok", ""),
    "proof_not_newline": ("Bewijs begint niet op nieuwe regel", "Voeg alinea-einde in tussen stelling en bewijs (Enter in LyX)."),
    "no_space_ref_left": ("Geen spatie voor referentie", "Misschien een vast spatie (~) voor de referentie?"),
    "no_space_ref_right": ("Geen spatie na referentie", "Misschien een vast spatie (~) na de referentie?"),
    "too_many_dots": ("Te veel punten", "Waarom meerdere '.'?"),
    "space_cite_punct": ("Spatie tussen citaat en interpunctie", ""),
    "space_after_period_cap": ("Ontbrekende spatie tussen punt en hoofdletter", ""),
    "space_after_period_word": ("Ontbrekende spatie tussen punt en woord", ""),
    "textquotedbl": ("Onjuist gebruik van \\textquotedbl", "Gebruik `` of ''."),
    "math_punct": ("Spatie tussen math-blok en interpunctie", ""),
    "cap_after_math": ("Hoofdletter na math-blok", "Waarom een hoofdletter na het math-blok?"),
    "equals_outside_math": ("Gelijkteken buiten math-blok", "Het '=' hoort in het math-blok."),
    "no_space_before_math": ("Geen spatie voor math-blok", ""),
    "no_space_before_cite": ("Geen spatie voor citaat", ""),
    "footnote_no_stop": ("Voetnoot zonder punt", ""),
    "no_space_after_math": ("Geen spatie na math-blok", ""),
    "no_space_before_macro": ("Geen spatie voor macro", ""),
    "no_space_after_macro": ("Geen spatie na macro", ""),
    "colon_in_math": (": in math-modus", "Gebruik \\colon voor functiedefinities."),
    "ugly_fraction": ("Lelijke breuk", r"Gebruik \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Te veel nullen zonder scheidingsteken", ""),
    "duplicated_word": ("Dubbel woord", ""),
    "para_no_stop": ("Alinea eindigt zonder punt", ""),
    "para_no_cap": ("Alinea begint zonder hoofdletter", ""),
    "para_starts_dot": ("Alinea begint met punt?", ""),
    "punct_in_math": ("Interpunctie in math-modus", "Verplaats ARG1 buiten de math-modus."),
    "double_dot": ("Dubbele punten", "Eén punt volstaat."),
    "space_before_punct_math": ("Spatie voor einde math-blok", ""),
    "space_before_rparen": ("Spatie voor )", ""),
    "proof_no_begin": ("\\end{proof} zonder \\begin", "Alinea-einde vóór \\end{proof} verwijderen?"),
    "section_has_dot": ("Section met punt", "Sections eindigen meestal niet met een punt."),
    "no_stop_def": ("Geen punt vóór \\end{definition}", ""),
    "no_stop_end": ("Geen punt vóór \\end{...}", ""),
}


def _dutch_specific_rules() -> list:
    """Top 20 Dutch grammatical/typographical errors."""
    return [
        simple_rule("hij word", "hij wordt"),
        simple_rule("hun hebben", "zij hebben"),
        simple_rule("hun doen", "zij doen"),
        simple_rule("me moeder", "mijn moeder"),
        simple_rule("dat boek van ik", "dat boek van mij"),
        simple_rule("te grootste", "de grootste"),
        simple_rule("groter als", "groter dan"),
        simple_rule("anders als", "anders dan"),
        simple_rule("in iedergeval", "in ieder geval"),
        simple_rule("perongeluk", "per ongeluk"),
        simple_rule("totemet", "tot en met"),
        simple_rule("teneerst", "ten eerste"),
        simple_rule("desniettegenstaande", "desniettemin"),
    ]


def generate_error_types() -> list:
    """Return Dutch rules."""
    return structural_rules(_MSGS) + _dutch_specific_rules()
