"""Slovak grammar rules - LaTeX structural rules with Slovak messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Prázdny matematický blok", ""),
    "macro_no_brace": ("Makro bez {}", "Za makrom je pravdepodobne potrebných {}."),
    "no_fullstop_after_cite": ("Bez bodky za odkazom na konci odseku", "Zdá sa, že chýba bodka."),
    "no_space_after_cite": ("Bez medzery za odkazom", ""),
    "no_space_before_cite": ("Bez medzery pred odkazom", ""),
    "uline_starts_early": ("Podčiarknutie začína príliš skoro", ""),
    "uline_ends_late": ("Podčiarknutie končí príliš neskoro", ""),
    "space_before_footnote": ("Medzera pred poznámkou pod čiarou", ""),
    "footnote_period_comma": ("Bodka/čiarka za poznámkou", "Ak sa poznámka vzťahuje na celú vetu, umiestnite ju za bodku."),
    "double_punct": ("Dvojité interpunkčné znamienko", ""),
    "implies_in_proof": ("Použitie \\implies v dôkaze", "Pre smer dôkazu použite \\Longrightarrow."),
    "no_space_after_ref": ("Bez medzery za odkazom", ""),
    "single_char": ("Jediný znak", "Jediný znak zvyčajne nedáva zmysel."),
    "empty_begin_end": ("Prázdny begin/end blok", ""),
    "proof_not_newline": ("Dôkaz nezačína na novom riadku", "Vložte oddeľovač odseku medzi vetu a dôkaz (Enter v LyX)."),
    "no_space_ref_left": ("Bez medzery vľavo od odkazu", "Možno nezlomiteľná medzera (~) pred odkazom?"),
    "no_space_ref_right": ("Bez medzery vpravo od odkazu", "Možno nezlomiteľná medzera (~) za odkazom?"),
    "too_many_dots": ("Príliš veľa bodiek", "Prečo viac ako jedna '.'?"),
    "space_cite_punct": ("Medzera medzi odkazom a interpunkciou", ""),
    "space_after_period_cap": ("Chýbajúca medzera medzi bodkou a veľkým písmenom", ""),
    "space_after_period_word": ("Chýbajúca medzera medzi bodkou a slovom", ""),
    "textquotedbl": ("Nesprávne použitie \\textquotedbl", "Použite `` alebo ''."),
    "math_punct": ("Medzera medzi matematickým blokom a interpunkciou", ""),
    "cap_after_math": ("Veľké písmeno za matematickým blokom", "Prečo veľké písmeno za matematickým blokom?"),
    "equals_outside_math": ("Rovnítko mimo matematický blok", "'=' by malo byť vnútri matematického bloku."),
    "no_space_before_math": ("Bez medzery pred matematickým blokom", ""),
    "no_space_before_cite": ("Bez medzery pred odkazom", ""),
    "footnote_no_stop": ("Poznámka bez bodky", ""),
    "no_space_after_math": ("Bez medzery za matematickým blokom", ""),
    "no_space_before_macro": ("Bez medzery pred makrom", ""),
    "no_space_after_macro": ("Bez medzery za makrom", ""),
    "colon_in_math": (": v matematickom režime", "Pre definíciu funkcií použite \\colon."),
    "ugly_fraction": ("Škaredý zlomok", r"Použite \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Príliš veľa núl bez oddeľovača", ""),
    "duplicated_word": ("Duplicitné slovo", ""),
    "para_no_stop": ("Odsek končí bez bodky", ""),
    "para_no_cap": ("Odsek začína bez veľkého písmena", ""),
    "para_starts_dot": ("Odsek začína bodkou?", ""),
    "punct_in_math": ("Interpunkcia vnútri matematického režimu", "Presuňte ARG1 mimo matematický režim."),
    "double_dot": ("Dvojitá bodka", "Stačí jedna bodka."),
    "space_before_punct_math": ("Medzera pred koncom matematického bloku", ""),
    "space_before_rparen": ("Medzera pred )", ""),
    "proof_no_begin": ("\\end{proof} bez \\begin", "Odstrániť oddeľovač odseku pred \\end{proof}?"),
    "section_has_dot": ("Sekcia s bodkou", "Sekcie zvyčajne nekončia bodkou."),
    "no_stop_def": ("Bez bodky pred \\end{definition}", ""),
    "no_stop_end": ("Bez bodky pred \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Slovak rules."""
    return structural_rules(_MSGS) + common_academic_rules()
