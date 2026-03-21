"""Urdu grammar rules - LaTeX structural rules with Urdu messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("خالی ریاضی بلاک", ""),
    "macro_no_brace": ("میکرو {} کے بغیر", "میکرو کے بعد شاید {} کی ضرورت ہے۔"),
    "no_fullstop_after_cite": ("پیراگراف کے اختتام پر حوالہ کے بعد نقطہ نہیں", "نقطہ غائب ہو سکتا ہے۔"),
    "no_space_after_cite": ("حوالہ کے بعد خالی جگہ نہیں", ""),
    "no_space_before_cite": ("حوالہ سے پہلے خالی جگہ نہیں", ""),
    "uline_starts_early": ("انڈرلائن بہت جلدی شروع ہوتی ہے", ""),
    "uline_ends_late": ("انڈرلائن بہت دیر سے ختم ہوتی ہے", ""),
    "space_before_footnote": ("فوٹ نوٹ سے پہلے خالی جگہ", ""),
    "footnote_period_comma": ("فوٹ نوٹ کے بعد نقطہ/کوما", "اگر فوٹ نوٹ پوری جملہ سے متعلق ہے تو نقطہ کے بعد رکھیں۔"),
    "double_punct": ("دہرا اوقاف", ""),
    "implies_in_proof": ("ثبوت میں \\implies کا استعمال", "ثبوت کی سمت کے لیے \\Longrightarrow استعمال کریں۔"),
    "no_space_after_ref": ("حوالہ کے بعد خالی جگہ نہیں", ""),
    "single_char": ("واحد حرف", "واحد حرف عام طور پر بامعنی نہیں ہوتا۔"),
    "empty_begin_end": ("خالی begin/end بلاک", ""),
    "proof_not_newline": ("ثبوت نئی لائن پر شروع نہیں ہوتا", "قضیہ اور ثبوت کے درمیان پیراگراف جداگانہ داخل کریں (LyX میں Enter)۔"),
    "no_space_ref_left": ("حوالہ کے بائیں خالی جگہ نہیں", "شاید حوالہ سے پہلے ناٹوٹنے والی خالی جگہ (~)؟"),
    "no_space_ref_right": ("حوالہ کے دائیں خالی جگہ نہیں", "شاید حوالہ کے بعد ناٹوٹنے والی خالی جگہ (~)؟"),
    "too_many_dots": ("بہت زیادہ نقطے", "ایک سے زیادہ '.' کیوں؟"),
    "space_cite_punct": ("حوالہ اور اوقاف کے درمیان خالی جگہ", ""),
    "space_after_period_cap": ("نقطہ اور بڑے حرف کے درمیان خالی جگہ نہیں", ""),
    "space_after_period_word": ("نقطہ اور لفظ کے درمیان خالی جگہ نہیں", ""),
    "textquotedbl": ("\\textquotedbl کا غلط استعمال", "`` یا '' استعمال کریں۔"),
    "math_punct": ("ریاضی بلاک اور اوقاف کے درمیان خالی جگہ", ""),
    "cap_after_math": ("ریاضی بلاک کے بعد بڑا حرف", "ریاضی بلاک کے بعد بڑا حرف کیوں؟"),
    "equals_outside_math": ("ریاضی بلاک کے باہر مساوات کا نشان", "'=' ریاضی بلاک کے اندر ہونا چاہیے۔"),
    "no_space_before_math": ("ریاضی بلاک سے پہلے خالی جگہ نہیں", ""),
    "no_space_before_cite": ("حوالہ سے پہلے خالی جگہ نہیں", ""),
    "footnote_no_stop": ("نقطہ کے بغیر فوٹ نوٹ", ""),
    "no_space_after_math": ("ریاضی بلاک کے بعد خالی جگہ نہیں", ""),
    "no_space_before_macro": ("میکرو سے پہلے خالی جگہ نہیں", ""),
    "no_space_after_macro": ("میکرو کے بعد خالی جگہ نہیں", ""),
    "colon_in_math": (": ریاضی موڈ میں", "افعال کی تعریف کے لیے \\colon استعمال کریں۔"),
    "ugly_fraction": ("بدصورت کسر", r"\\nicefrac{ARG1}{ARG2} استعمال کریں۔"),
    "too_many_zeros": ("جداکار کے بغیر زیادہ صفر", ""),
    "duplicated_word": ("دوہری لفظ", ""),
    "para_no_stop": ("پیراگراف نقطہ کے بغیر ختم ہوتا ہے", ""),
    "para_no_cap": ("پیراگراف بڑے حرف کے بغیر شروع ہوتا ہے", ""),
    "para_starts_dot": ("پیراگراف نقطہ سے شروع ہوتا ہے؟", ""),
    "punct_in_math": ("ریاضی موڈ میں اوقاف", "ARG1 کو ریاضی موڈ سے باہر منتقل کریں۔"),
    "double_dot": ("دہرا نقطہ", "ایک نقطہ کافی ہے۔"),
    "space_before_punct_math": ("ریاضی بلاک کے اختتام سے پہلے خالی جگہ", ""),
    "space_before_rparen": (") سے پہلے خالی جگہ", ""),
    "proof_no_begin": ("\\end{proof} \\begin کے بغیر", "\\end{proof} سے پہلے پیراگراف جداگانہ ہٹائیں؟"),
    "section_has_dot": ("نقطہ والا سیکشن", "سیکشن عام طور پر نقطہ سے ختم نہیں ہوتے۔"),
    "no_stop_def": ("\\end{definition} سے پہلے نقطہ نہیں", ""),
    "no_stop_end": ("\\end{...} سے پہلے نقطہ نہیں", ""),
}


def generate_error_types() -> list:
    """Return Urdu rules."""
    return structural_rules(_MSGS) + common_academic_rules()
