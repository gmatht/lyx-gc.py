"""Scottish Gaelic grammar rules - LaTeX structural rules with Scottish Gaelic messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("Bloc matamataigs falamh", ""),
    "macro_no_brace": ("Macro gun {}", "Dh'fhaodadh gum feum {} às dèidh a' mhacro."),
    "no_fullstop_after_cite": ("Gun phuing às dèidh an iomradh aig ceann na paragraf", "Dh'fhaodadh gum bi puing air a dhol a-mach."),
    "no_space_after_cite": ("Gun àite às dèidh an iomradh", ""),
    "no_space_before_cite": ("Gun àite ro an iomradh", ""),
    "uline_starts_early": ("Tha an loidhne fo-thaobh a' tòiseachadh ro thràth", ""),
    "uline_ends_late": ("Tha an loidhne fo-thaobh a' crìochnachadh ro fhadalach", ""),
    "space_before_footnote": ("Àite ro an nota-coise", ""),
    "footnote_period_comma": ("Puing/cromag às dèidh an nota", "Ma tha an nota a' toirt iomradh air an t-sèantans gu lèir, cuir e às dèidh na puinge."),
    "double_punct": ("Dà chomharradh-puings", ""),
    "implies_in_proof": ("Cleachdadh \\implies anns an dearbhadh", "Cleachd \\Longrightarrow airson stiùireadh an dearbhaidh."),
    "no_space_after_ref": ("Gun àite às dèidh an iomraidh", ""),
    "single_char": ("Aon charactar", "Tha aon charactar mar as trice gun chiall."),
    "empty_begin_end": ("Bloc begin/end falamh", ""),
    "proof_not_newline": ("Chan eil an dearbhadh a' tòiseachadh air loidhne ùr", "Cuir eadar-dhealachadh paragraf eadar an teòiridh agus an dearbhadh (Enter ann an LyX)."),
    "no_space_ref_left": ("Gun àite air taobh clì an iomraidh", "Dh'fhaodadh àite neo-bhriseadh (~) ro an iomradh?"),
    "no_space_ref_right": ("Gun àite air taobh deas an iomraidh", "Dh'fhaodadh àite neo-bhriseadh (~) às dèidh an iomraidh?"),
    "too_many_dots": ("Cus phuingean", "Carson barrachd air aon '.'?"),
    "space_cite_punct": ("Àite eadar an iomradh agus na comharran-puings", ""),
    "space_after_period_cap": ("Àite a dh'fhàgas eadar a' phuing agus an litir mhòr", ""),
    "space_after_period_word": ("Àite a dh'fhàgas eadar a' phuing agus an fhacal", ""),
    "textquotedbl": ("Cleachdadh ceàrr air \\textquotedbl", "Cleachd `` no ''."),
    "math_punct": ("Àite eadar am bloc matamataigs agus na comharran-puings", ""),
    "cap_after_math": ("Litir mhòr às dèidh a' bhloc matamataigs", "Carson litir mhòr às dèidh a' bhloc matamataigs?"),
    "equals_outside_math": ("Comharra co-ionannachd taobh a-muigh a' bhloc matamataigs", "Bu chòir an '=' a bhith taobh a-staigh a' bhloc matamataigs."),
    "no_space_before_math": ("Gun àite ro bhloc matamataigs", ""),
    "no_space_before_cite": ("Gun àite ro an iomradh", ""),
    "footnote_no_stop": ("Nota gun phuing", ""),
    "no_space_after_math": ("Gun àite às dèidh a' bhloc matamataigs", ""),
    "no_space_before_macro": ("Gun àite ro an macro", ""),
    "no_space_after_macro": ("Gun àite às dèidh an macro", ""),
    "colon_in_math": (": ann am modh matamataigs", "Cleachd \\colon airson feartan a mhìneachadh."),
    "ugly_fraction": ("Bloigh mì-shnog", r"Cleachd \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("Cus nulan gun sgaradair", ""),
    "duplicated_word": ("Facal dùblaichte", ""),
    "para_no_stop": ("Tha a' pharagraf a' crìochnachadh gun phuing", ""),
    "para_no_cap": ("Tha a' pharagraf a' tòiseachadh gun litir mhòr", ""),
    "para_starts_dot": ("A bheil a' pharagraf a' tòiseachadh le puing?", ""),
    "punct_in_math": ("Comharra-puing taobh a-staigh modh matamataigs", "Gluais ARG1 a-mach às a' mhodh matamataigs."),
    "double_dot": ("Dà phuing", "Tha aon phuing gu leòr."),
    "space_before_punct_math": ("Àite ro dheireadh a' bhloc matamataigs", ""),
    "space_before_rparen": ("Àite ro )", ""),
    "proof_no_begin": ("\\end{proof} gun \\begin", "Thoir air falbh an eadar-dhealachadh paragraf ro \\end{proof}?"),
    "section_has_dot": ("Earrann le puing", "Mar as trice chan eil na h-earrannan a' crìochnachadh le puing."),
    "no_stop_def": ("Gun phuing ro \\end{definition}", ""),
    "no_stop_end": ("Gun phuing ro \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Scottish Gaelic rules."""
    return structural_rules(_MSGS) + common_academic_rules()
