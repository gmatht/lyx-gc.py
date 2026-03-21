"""Arabic grammar rules - LaTeX structural rules with Arabic messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("كتلة رياضية فارغة", ""),
    "macro_no_brace": ("ماكرو بدون {}", "يُحتمل أن {} مطلوب بعد الماكرو."),
    "no_fullstop_after_cite": ("لا توجد نقطة بعد الاقتباس في نهاية الفقرة", "يبدو أن النقطة ناقصة."),
    "no_space_after_cite": ("لا مسافة بعد الاقتباس", ""),
    "no_space_before_cite": ("لا مسافة قبل الاقتباس", ""),
    "uline_starts_early": ("يبدأ السطر التحتي بوقت مبكر جداً", ""),
    "uline_ends_late": ("ينتهي السطر التحتي متأخراً جداً", ""),
    "space_before_footnote": ("مسافة قبل الحاشية", ""),
    "footnote_period_comma": ("نقطة/فاصلة بعد الحاشية", "إن أشارت الحاشية إلى الجملة كاملة، ضعها بعد النقطة."),
    "double_punct": ("ترقيم مزدوج", ""),
    "implies_in_proof": ("استخدام \\implies في البرهان", "استخدم \\Longrightarrow لاتجاه البرهان."),
    "no_space_after_ref": ("لا مسافة بعد المرجع", ""),
    "single_char": ("حرف واحد", "الحرف الواحد عادةً لا معنى له."),
    "empty_begin_end": ("كتلة begin/end فارغة", ""),
    "proof_not_newline": ("البرهان لا يبدأ في سطر جديد", "أدخل فاصل فقرة بين النظرية والبرهان (Enter في LyX)."),
    "no_space_ref_left": ("لا مسافة قبل المرجع", "ربما مسافة غير قابلة للكسر (~) قبل المرجع؟"),
    "no_space_ref_right": ("لا مسافة بعد المرجع", "ربما مسافة غير قابلة للكسر (~) بعد المرجع؟"),
    "too_many_dots": ("نقاط كثيرة جداً", "لماذا أكثر من '.'؟"),
    "space_cite_punct": ("مسافة بين الاقتباس والترقيم", ""),
    "space_after_period_cap": ("مسافة ناقصة بين النقطة والحرف الكبير", ""),
    "space_after_period_word": ("مسافة ناقصة بين النقطة والكلمة", ""),
    "textquotedbl": ("استخدام خاطئ لـ \\textquotedbl", "استخدم `` أو ''."),
    "math_punct": ("مسافة بين كتلة الرياضيات والترقيم", ""),
    "cap_after_math": ("حرف كبير بعد كتلة الرياضيات", "لماذا حرف كبير بعد كتلة الرياضيات؟"),
    "equals_outside_math": ("علامة يساوي خارج كتلة الرياضيات", "ينبغي أن تكون '=' داخل كتلة الرياضيات."),
    "no_space_before_math": ("لا مسافة قبل كتلة الرياضيات", ""),
    "no_space_before_cite": ("لا مسافة قبل الاقتباس", ""),
    "footnote_no_stop": ("حاشية بدون نقطة", ""),
    "no_space_after_math": ("لا مسافة بعد كتلة الرياضيات", ""),
    "no_space_before_macro": ("لا مسافة قبل الماكرو", ""),
    "no_space_after_macro": ("لا مسافة بعد الماكرو", ""),
    "colon_in_math": (": في وضع الرياضيات", "استخدم \\colon لتعريف الدوال."),
    "ugly_fraction": ("كسر قبيح", r"استخدم \\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("أصفار كثيرة بدون فاصل", ""),
    "duplicated_word": ("كلمة مكررة", ""),
    "para_no_stop": ("الفقرة تنتهي بدون نقطة", ""),
    "para_no_cap": ("الفقرة تبدأ بدون حرف كبير", ""),
    "para_starts_dot": ("الفقرة تبدأ بنقطة؟", ""),
    "punct_in_math": ("ترقيم داخل وضع الرياضيات", "انقل ARG1 خارج وضع الرياضيات."),
    "double_dot": ("نقطتان", "نقطة واحدة تكفي."),
    "space_before_punct_math": ("مسافة قبل نهاية كتلة الرياضيات", ""),
    "space_before_rparen": ("مسافة قبل )", ""),
    "proof_no_begin": ("\\end{proof} بدون \\begin", "أزل فاصل الفقرة قبل \\end{proof}؟"),
    "section_has_dot": ("قسم بنقطة", "الأقسام عادةً لا تنتهي بنقطة."),
    "no_stop_def": ("لا نقطة قبل \\end{definition}", ""),
    "no_stop_end": ("لا نقطة قبل \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Arabic rules."""
    return structural_rules(_MSGS) + common_academic_rules()
