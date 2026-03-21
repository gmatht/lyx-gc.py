"""Breton grammar rules - LaTeX structural rules with Breton messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Bloc matematik goullo", ""),
    "macro_no_brace": ("Makro hep {}", "Ur {} a c'hall bezañ ezhomm goude ar makro."),
    "no_fullstop_after_cite": ("Ebet poent goude ar meneg er penn ar paragraf", "Ur poent a vank marteze."),
    "no_space_after_cite": ("Ebet egor goude ar meneg", ""),
    "no_space_before_cite": ("Ebet egor a-raok ar meneg", ""),
    "uline_starts_early": ("An dindanlinenn a grog re abred", ""),
    "uline_ends_late": ("An dindanlinenn a echu re ziwezhat", ""),
    "space_before_footnote": ("Egor a-raok an notenn-traoñ", ""),
    "footnote_period_comma": ("Poent/virgulenn goude an notenn", "Mard eo ar frazenn e-bezh evit an notenn, lakaat goude ar poent."),
    "double_punct": ("Peñseñchadur doubl", ""),
    "implies_in_proof": ("Implij \\implies er prouenn", "Implijit \\Longrightarrow evit tu ar prouenn."),
    "no_space_after_ref": ("Ebet egor goude an dave", ""),
    "single_char": ("Un arouez hepken", "Un arouez hepken ne ra ket talvoudegezh."),
    "empty_begin_end": ("Bloc begin/end goullo", ""),
    "proof_not_newline": ("Ar prouenn ne grog ket war ul linenn nevez", "Lakaat un disrann paragraf etre an teoreom hag ar prouenn (Enter e LyX)."),
    "no_space_ref_left": ("Ebet egor a-gleiz d'an dave", "Martezed un egor dic'hortoz (~) a-raok an dave?"),
    "no_space_ref_right": ("Ebet egor a-zehoù d'an dave", "Martezed un egor dic'hortoz (~) goude an dave?"),
    "too_many_dots": ("Re kalz poentoù", "Perak muioc'h eget un '.'?"),
    "space_cite_punct": ("Egor etre ar meneg hag ar peñseñchadur", ""),
    "space_after_period_cap": ("Egor a vank etre ar poent hag al lizherenn vras", ""),
    "space_after_period_word": ("Egor a vank etre ar poent hag ar ger", ""),
    "textquotedbl": ("Implij fall a \\textquotedbl", "Implijit `` pe ''."),
    "math_punct": ("Egor etre ar bloc matematik hag ar peñseñchadur", ""),
    "cap_after_math": ("Lizherenn vras goude ar bloc matematik", "Perak lizherenn vras goude ar bloc matematik?"),
    "equals_outside_math": ("Arouez kevatal er-maez eus ar bloc matematik", "Emañ ar '=' e diabarzh ar bloc."),
    "no_space_before_math": ("Ebet egor a-raok ar bloc matematik", ""),
    "no_space_before_cite": ("Ebet egor a-raok ar meneg", ""),
    "footnote_no_stop": ("Notenn hep poent", ""),
    "no_space_after_math": ("Ebet egor goude ar bloc matematik", ""),
    "no_space_before_macro": ("Ebet egor a-raok ar makro", ""),
    "no_space_after_macro": ("Ebet egor goude ar makro", ""),
    "colon_in_math": (": er mod matematik", "Implijit \\colon evit displegañ fonksionoù."),
    "ugly_fraction": ("Rann n'eo ket aes", r"Implijit \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Re kalz zeroù hep disranner", ""),
    "duplicated_word": ("Ger doubl", ""),
    "para_no_stop": ("Paragraf a echu hep poent", ""),
    "para_no_cap": ("Paragraf a grog hep lizherenn vras", ""),
    "para_starts_dot": ("Paragraf a grog gant poent?", ""),
    "punct_in_math": ("Peñseñchadur er mod matematik", "Lakaat ARG1 er-maez eus ar mod matematik."),
    "double_dot": ("Div boent", "Un poent a-walc'h."),
    "space_before_punct_math": ("Egor a-raok dibenn ar bloc matematik", ""),
    "space_before_rparen": ("Egor a-raok )", ""),
    "proof_no_begin": ("\\end{proof} hep \\begin", "Lemel disrann paragraf a-raok \\end{proof}?"),
    "section_has_dot": ("Rann gant poent", "Ar rannoù ne echuont ket gant poent."),
    "no_stop_def": ("Ebet poent a-raok \\end{definition}", ""),
    "no_stop_end": ("Ebet poent a-raok \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Breton rules."""
    return structural_rules(_MSGS) + common_academic_rules()
