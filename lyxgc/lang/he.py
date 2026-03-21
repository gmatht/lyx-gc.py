"""Hebrew grammar rules - LaTeX structural rules with Hebrew messages."""
from ._structural import structural_rules
from ._common import common_academic_rules

_MSGS = {
    "empty_mathblock": ("בלוק מתמטי ריק", ""),
    "macro_no_brace": ("מאקרו ללא {}", "כנראה נדרש {} אחרי המאקרו."),
    "no_fullstop_after_cite": ("ללא נקודה אחרי ציטוט בסוף פסקה", "נראה שנקודה חסרה."),
    "no_space_after_cite": ("ללא רווח אחרי ציטוט", ""),
    "no_space_before_cite": ("ללא רווח לפני ציטוט", ""),
    "uline_starts_early": ("הקו התחתון מתחיל מוקדם מדי", ""),
    "uline_ends_late": ("הקו התחתון נגמר מאוחר מדי", ""),
    "space_before_footnote": ("רווח לפני הערת שוליים", ""),
    "footnote_period_comma": ("נקודה/פסיק אחרי הערת שוליים", "אם ההערה מתייחסת למשפט המלא, שים אותה אחרי הנקודה."),
    "double_punct": ("סימני פיסוק כפולים", ""),
    "implies_in_proof": ("שימוש ב-\\implies בהוכחה", "השתמש ב-\\Longrightarrow לכיוון ההוכחה."),
    "no_space_after_ref": ("ללא רווח אחרי אזכור", ""),
    "single_char": ("תו בודד", "תו בודד בדרך כלל אינו הגיוני."),
    "empty_begin_end": ("בלוק begin/end ריק", ""),
    "proof_not_newline": ("ההוכחה לא מתחילה בשורה חדשה", "הוסף הפרדת פסקה בין המשפט להוכחה (Enter ב-LyX)."),
    "no_space_ref_left": ("ללא רווח משמאל לאזכור", "אולי רווח לא-שביר (~) לפני האזכור?"),
    "no_space_ref_right": ("ללא רווח מימין לאזכור", "אולי רווח לא-שביר (~) אחרי האזכור?"),
    "too_many_dots": ("יותר מדי נקודות", "למה יותר מנקודה אחת '.'?"),
    "space_cite_punct": ("רווח בין ציטוט לסימני פיסוק", ""),
    "space_after_period_cap": ("רווח חסר בין נקודה לאות גדולה", ""),
    "space_after_period_word": ("רווח חסר בין נקודה למילה", ""),
    "textquotedbl": ("שימוש שגוי ב-\\textquotedbl", "השתמש ב-`` או ''."),
    "math_punct": ("רווח בין בלוק מתמטי לסימני פיסוק", ""),
    "cap_after_math": ("אות גדולה אחרי בלוק מתמטי", "למה אות גדולה אחרי בלוק מתמטי?"),
    "equals_outside_math": ("סימן שוויון מחוץ לבלוק מתמטי", "ה-'=' צריך להיות בתוך בלוק המתמטי."),
    "no_space_before_math": ("ללא רווח לפני בלוק מתמטי", ""),
    "no_space_before_cite": ("ללא רווח לפני ציטוט", ""),
    "footnote_no_stop": ("הערת שוליים ללא נקודה", ""),
    "no_space_after_math": ("ללא רווח אחרי בלוק מתמטי", ""),
    "no_space_before_macro": ("ללא רווח לפני מאקרו", ""),
    "no_space_after_macro": ("ללא רווח אחרי מאקרו", ""),
    "colon_in_math": (": במצב מתמטי", "השתמש ב-\\colon להגדרת פונקציות."),
    "ugly_fraction": ("שבר מכוער", r"השתמש ב-\\nicefrac{ARG1}{ARG2}."),
    "too_many_zeros": ("יותר מדי אפסים בלי מפריד", ""),
    "duplicated_word": ("מילה כפולה", ""),
    "para_no_stop": ("פסקה נגמרת ללא נקודה", ""),
    "para_no_cap": ("פסקה מתחילה ללא אות גדולה", ""),
    "para_starts_dot": ("פסקה מתחילה בנקודה?", ""),
    "punct_in_math": ("סימן פיסוק בתוך מצב מתמטי", "העבר את ARG1 מחוץ למצב המתמטי."),
    "double_dot": ("שתי נקודות", "נקודה אחת מספיקה."),
    "space_before_punct_math": ("רווח לפני סוף בלוק מתמטי", ""),
    "space_before_rparen": ("רווח לפני )", ""),
    "proof_no_begin": ("\\end{proof} ללא \\begin", "להסיר הפרדת פסקה לפני \\end{proof}?"),
    "section_has_dot": ("סעיף עם נקודה", "סעיפים בדרך כלל לא נגמרים בנקודה."),
    "no_stop_def": ("ללא נקודה לפני \\end{definition}", ""),
    "no_stop_end": ("ללא נקודה לפני \\end{...}", ""),
}


def generate_error_types() -> list:
    """Return Hebrew rules."""
    return structural_rules(_MSGS) + common_academic_rules()
