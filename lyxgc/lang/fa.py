"""Farsi grammar rules - LaTeX structural rules with Farsi messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("بلوک ریاضی خالی", ""),
    "macro_no_brace": ("ماکرو بدون {}", "احتمالاً {} پس از ماکرو لازم است."),
    "no_fullstop_after_cite": ("بدون نقطهٔ کامل پس از ارجاع در انتهای پاراگراف", "نقطه ممکن است مفقود باشد."),
    "no_space_after_cite": ("بدون فاصله پس از ارجاع", ""),
    "no_space_before_cite": ("بدون فاصله پیش از ارجاع", ""),
    "uline_starts_early": ("زیرخط خیلی زود شروع می‌شود", ""),
    "uline_ends_late": ("زیرخط خیلی دیر تمام می‌شود", ""),
    "space_before_footnote": ("فاصله پیش از پاورقی", ""),
    "footnote_period_comma": ("نقطه/ویرگول پس از پاورقی", "اگر پاورقی به کل جمله اشاره دارد، آن را پس از نقطه قرار دهید."),
    "double_punct": ("علائم سجاوندی دوتایی", ""),
    "implies_in_proof": ("استفاده از \\implies در اثبات", "برای جهت اثبات از \\Longrightarrow استفاده کنید."),
    "no_space_after_ref": ("بدون فاصله پس از ارجاع", ""),
    "single_char": ("یک نویسهٔ تنها", "یک نویسهٔ تنها معمولاً معنایی ندارد."),
    "empty_begin_end": ("بلوک begin/end خالی", ""),
    "proof_not_newline": ("اثبات در خط جدید شروع نمی‌شود", "جداکنندهٔ پاراگراف بین قضیه و اثبات قرار دهید (Enter در LyX)."),
    "no_space_ref_left": ("بدون فاصله در سمت چپ ارجاع", "شاید فاصلهٔ غیرشکستنی (~) پیش از ارجاع؟"),
    "no_space_ref_right": ("بدون فاصله در سمت راست ارجاع", "شاید فاصلهٔ غیرشکستنی (~) پس از ارجاع؟"),
    "too_many_dots": ("نقطهٔ زیاد", "چرا بیش از یک '.'؟"),
    "space_cite_punct": ("فاصله بین ارجاع و علائم سجاوندی", ""),
    "space_after_period_cap": ("فاصلهٔ مفقود بین نقطه و حرف بزرگ", ""),
    "space_after_period_word": ("فاصلهٔ مفقود بین نقطه و واژه", ""),
    "textquotedbl": ("استفادهٔ نادرست از \\textquotedbl", "از `` یا '' استفاده کنید."),
    "math_punct": ("فاصله بین بلوک ریاضی و علائم سجاوندی", ""),
    "cap_after_math": ("حرف بزرگ پس از بلوک ریاضی", "چرا حرف بزرگ پس از بلوک ریاضی؟"),
    "equals_outside_math": ("علامت تساوی خارج از بلوک ریاضی", "'=' باید داخل بلوک ریاضی باشد."),
    "no_space_before_math": ("بدون فاصله پیش از بلوک ریاضی", ""),
    "no_space_before_cite": ("بدون فاصله پیش از ارجاع", ""),
    "footnote_no_stop": ("پاورقی بدون نقطه", ""),
    "no_space_after_math": ("بدون فاصله پس از بلوک ریاضی", ""),
    "no_space_before_macro": ("بدون فاصله پیش از ماکرو", ""),
    "no_space_after_macro": ("بدون فاصله پس از ماکرو", ""),
    "colon_in_math": (": در حالت ریاضی", "برای تعریف تابع از \\colon استفاده کنید."),
    "ugly_fraction": ("کسر زشت", r"از \\nicefrac{ARG1}{ARG2} استفاده کنید."),
    "too_many_zeros": ("صفرهای زیاد بدون جداکننده", ""),
    "duplicated_word": ("واژهٔ تکراری", ""),
    "para_no_stop": ("پاراگراف بدون نقطه تمام می‌شود", ""),
    "para_no_cap": ("پاراگراف بدون حرف بزرگ شروع می‌شود", ""),
    "para_starts_dot": ("پاراگراف با نقطه شروع می‌شود؟", ""),
    "punct_in_math": ("علائم سجاوندی داخل حالت ریاضی", "ARG1 را خارج از حالت ریاضی قرار دهید."),
    "double_dot": ("دو نقطه", "یک نقطه کافی است."),
    "space_before_punct_math": ("فاصله پیش از پایان بلوک ریاضی", ""),
    "space_before_rparen": ("فاصله پیش از )", ""),
    "proof_no_begin": ("\\end{proof} بدون \\begin", "جداکنندهٔ پاراگراف پیش از \\end{proof} را حذف کنید؟"),
    "section_has_dot": ("بخش با نقطه", "بخش‌ها معمولاً با نقطه تمام نمی‌شوند."),
    "no_stop_def": ("بدون نقطه پیش از \\end{definition}", ""),
    "no_stop_end": ("بدون نقطه پیش از \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Farsi rules."""
    return structural_rules(_MSGS) + common_academic_rules()
