"""North Sami grammar rules - LaTeX structural rules with North Sami messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Guhkes matematihka bloakku", ""),
    "macro_no_brace": ("Makro {} haga", "Makro maŋŋá {} fertejit vejolaččat."),
    "no_fullstop_after_cite": ("Oaivil gitta čuoggá loahpahagas", "Cuoggá sáhttá lihkat."),
    "no_space_after_cite": ("Gaska eanet čuoggá maŋá", ""),
    "no_space_before_cite": ("Gaska eanet čuoggá ovdal", ""),
    "uline_starts_early": ("Vuolitláseloddi álgá olle ovdal", ""),
    "uline_ends_late": ("Vuolitláseloddi loahppá olle maŋŋá", ""),
    "space_before_footnote": ("Gaska vuolitláselotti ovdal", ""),
    "footnote_period_comma": ("Cuoggá/gaskalágan vuolitláselotti maŋá", "Jos vuolitláseloddi váldá buot cealkaga, biddjo dan cuoggá maŋá."),
    "double_punct": ("Guokte interpunktasiuvdna", ""),
    "implies_in_proof": ("\\implies geavat čujuhusas", "Geavat \\Longrightarrow čujuhusa suorgis."),
    "no_space_after_ref": ("Gaska eanet referansa maŋá", ""),
    "single_char": ("Oktii merkki", "Oktii merkki ii leat dábáleamos."),
    "empty_begin_end": ("Guhkes begin/end bloakku", ""),
    "proof_not_newline": ("Čujuhus álgá ii ođđa joavdus", "Biddjo paragráffa juohke theoréma ja čujuhusa gaskka (Enter LyX:s)."),
    "no_space_ref_left": ("Gaska eanet referansa gurut bealde", "Vehket vejolaččat gaskamearka (~) referansa ovdal?"),
    "no_space_ref_right": ("Gaska eanet referansa olgeš bealde", "Vehket vejolaččat gaskamearka (~) referansa maŋá?"),
    "too_many_dots": ("Eanet cuoggá", "Manne eanet go okta '.'?"),
    "space_cite_punct": ("Gaska čuoggá ja interpunktasiuvdna gaskka", ""),
    "space_after_period_cap": ("Gaska vuollái cuoggá ja stuorit bustávva gaskka", ""),
    "space_after_period_word": ("Gaska vuollái cuoggá ja ságastallamiid gaskka", ""),
    "textquotedbl": ("Hálaš \\textquotedbl geavat", "Geavat `` dahje ''."),
    "math_punct": ("Gaska matematihka bloakku ja interpunktasiuvdna gaskka", ""),
    "cap_after_math": ("Stuorit bustávva matematihka bloakku maŋá", "Manne stuorit bustávva matematihka bloakku maŋá?"),
    "equals_outside_math": ("Vástádusmerkki matematihka bloakkus olggos", "'=' ferte leat matematihka bloakkus siste."),
    "no_space_before_math": ("Gaska eanet matematihka bloakku ovdal", ""),
    "no_space_before_cite": ("Gaska eanet čuoggá ovdal", ""),
    "footnote_no_stop": ("Vuolitláseloddi cuoggá haga", ""),
    "no_space_after_math": ("Gaska eanet matematihka bloakku maŋá", ""),
    "no_space_before_macro": ("Gaska eanet makro ovdal", ""),
    "no_space_after_macro": ("Gaska eanet makro maŋá", ""),
    "colon_in_math": (": matematihkarežiimás", "Geavat \\colon funkšuvnnaid defineren."),
    "ugly_fraction": ("Boahtte jorbbas", r"Geavat \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Eanet nollaid juohke haga", ""),
    "duplicated_word": ("Guokte ságastallan", ""),
    "para_no_stop": ("Paragráffa loahppá cuoggá haga", ""),
    "para_no_cap": ("Paragráffa álgá stuorit bustávva haga", ""),
    "para_starts_dot": ("Paragráffa álgá cuoggáin?", ""),
    "punct_in_math": ("Interpunktasiuvdna matematihkarežiimás siste", "Biddjo ARG1 matematihkarežiimás olggos."),
    "double_dot": ("Guokte cuoggá", "Oktii cuoggá lea nana."),
    "space_before_punct_math": ("Gaska matematihka bloakku loahpahagas ovdal", ""),
    "space_before_rparen": ("Gaska ) ovdal", ""),
    "proof_no_begin": ("\\end{proof} \\begin haga", "Sihko paragráffa juohke \\end{proof} ovdal?"),
    "section_has_dot": ("Oassi cuoggáin", "Oassit loahppet eanet cuoggáin."),
    "no_stop_def": ("Cuoggá eanet \\end{definition} ovdal", ""),
    "no_stop_end": ("Cuoggá eanet \\end{...} ovdal", ""),
}


def generate_error_types() -> list:
    """Return North Sami rules."""
    return structural_rules(_MSGS) + common_academic_rules()
