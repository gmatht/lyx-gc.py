"""Croatian grammar rules - LaTeX structural rules with Croatian messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Prazan matematički blok", ""),
    "macro_no_brace": ("Makro bez {}", "Vjerojatno je potrebno {} nakon makra."),
    "no_fullstop_after_cite": ("Bez točke nakon citata na kraju odlomka", "Čini se da nedostaje točka."),
    "no_space_after_cite": ("Bez razmaka nakon citata", ""),
    "no_space_before_cite": ("Bez razmaka prije citata", ""),
    "uline_starts_early": ("Podcrtavanje počinje prerano", ""),
    "uline_ends_late": ("Podcrtavanje završava prekasno", ""),
    "space_before_footnote": ("Razmak prije fusnote", ""),
    "footnote_period_comma": ("Točka/zarez nakon fusnote", "Ako se fusnota odnosi na cijelu rečenicu, stavite je nakon točke."),
    "double_punct": ("Dvostruko interpunkcijsko obilježje", ""),
    "implies_in_proof": ("Upotreba \\implies u dokazu", "Koristite \\Longrightarrow za smjer dokaza."),
    "no_space_after_ref": ("Bez razmaka nakon reference", ""),
    "single_char": ("Jedan znak", "Jedan znak obično nema smisla."),
    "empty_begin_end": ("Prazan begin/end blok", ""),
    "proof_not_newline": ("Dokaz ne počinje u novom retku", "Unesite prekid odlomka između teorema i dokaza (Enter u LyX-u)."),
    "no_space_ref_left": ("Bez razmaka lijevo od reference", "Možda nerazdjelný razmak (~) prije reference?"),
    "no_space_ref_right": ("Bez razmaka desno od reference", "Možda nerazdjelný razmak (~) nakon reference?"),
    "too_many_dots": ("Previše točaka", "Zašto više od jedne '.'?"),
    "space_cite_punct": ("Razmak između citata i interpunkcije", ""),
    "space_after_period_cap": ("Nedostaje razmak između točke i velikog slova", ""),
    "space_after_period_word": ("Nedostaje razmak između točke i riječi", ""),
    "textquotedbl": ("Pogrešna upotreba \\textquotedbl", "Koristite `` ili ''."),
    "math_punct": ("Razmak između matematičkog bloka i interpunkcije", ""),
    "cap_after_math": ("Veliko slovo nakon matematičkog bloka", "Zašto veliko slovo nakon matematičkog bloka?"),
    "equals_outside_math": ("Znak jednakosti izvan matematičkog bloka", "'=' bi trebao biti unutar matematičkog bloka."),
    "no_space_before_math": ("Bez razmaka prije matematičkog bloka", ""),
    "no_space_before_cite": ("Bez razmaka prije citata", ""),
    "footnote_no_stop": ("Fusnota bez točke", ""),
    "no_space_after_math": ("Bez razmaka nakon matematičkog bloka", ""),
    "no_space_before_macro": ("Bez razmaka prije makra", ""),
    "no_space_after_macro": ("Bez razmaka nakon makra", ""),
    "colon_in_math": (": u matematičkom načinu", "Koristite \\colon za definiranje funkcija."),
    "ugly_fraction": ("Neugodan razlomak", r"Koristite \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Previše nula bez separatora", ""),
    "duplicated_word": ("Duplicirana riječ", ""),
    "para_no_stop": ("Odlomak završava bez točke", ""),
    "para_no_cap": ("Odlomak počinje bez velikog slova", ""),
    "para_starts_dot": ("Odlomak počinje točkom?", ""),
    "punct_in_math": ("Interpunkcija unutar matematičkog načina", "Premjestite ARG1 izvan matematičkog načina."),
    "double_dot": ("Dvostruka točka", "Jedna točka je dovoljna."),
    "space_before_punct_math": ("Razmak prije kraja matematičkog bloka", ""),
    "space_before_rparen": ("Razmak prije )", ""),
    "proof_no_begin": ("\\end{proof} bez \\begin", "Ukloniti prekid odlomka prije \\end{proof}?"),
    "section_has_dot": ("Odjeljak s točkom", "Odjeljci obično ne završavaju točkom."),
    "no_stop_def": ("Bez točke prije \\end{definition}", ""),
    "no_stop_end": ("Bez točke prije \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Croatian rules."""
    return structural_rules(_MSGS) + common_academic_rules()
