"""Hindi grammar rules - LaTeX structural rules with Hindi messages."""
from ._structural import structural_rules
from ..rules import simple_rule
from ..tokenizer import MATHBLOCK

_MSGS = {
    "empty_mathblock": ("खाली गणित ब्लॉक", ""),
    "macro_no_brace": ("मैक्रो बिना {}", "मैक्रो के बाद शायद {} की आवश्यकता है।"),
    "no_fullstop_after_cite": ("पैराग्राफ के अंत में उद्धरण के बाद बिन्दु नहीं", "बिन्दु गायब हो सकता है।"),
    "no_space_after_cite": ("उद्धरण के बाद रिक्ति नहीं", ""),
    "no_space_before_cite": ("उद्धरण से पहले रिक्ति नहीं", ""),
    "uline_starts_early": ("रेखांकन बहुत जल्दी शुरू होता है", ""),
    "uline_ends_late": ("रेखांकन बहुत देर से समाप्त होता है", ""),
    "space_before_footnote": ("फुटनोट से पहले रिक्ति", ""),
    "footnote_period_comma": ("फुटनोट के बाद बिन्दु/अल्पविराम", "यदि फुटनोट पूरे वाक्य से संबंधित है तो बिन्दु के बाद रखें।"),
    "double_punct": ("दोहरा विराम चिह्न", ""),
    "implies_in_proof": ("प्रमाण में \\implies का उपयोग", "प्रमाण की दिशा के लिए \\Longrightarrow का उपयोग करें।"),
    "no_space_after_ref": ("संदर्भ के बाद रिक्ति नहीं", ""),
    "single_char": ("एक अक्षर", "एक अक्षर का आमतौर पर कोई अर्थ नहीं होता।"),
    "empty_begin_end": ("खाली begin/end ब्लॉक", ""),
    "proof_not_newline": ("प्रमाण नई पंक्ति पर शुरू नहीं होता", "प्रमेय और प्रमाण के बीच पैराग्राफ विभाजक डालें (LyX में Enter)।"),
    "no_space_ref_left": ("संदर्भ के बाएँ रिक्ति नहीं", "शायद संदर्भ से पहले अटूट रिक्ति (~)?"),
    "no_space_ref_right": ("संदर्भ के दाएँ रिक्ति नहीं", "शायद संदर्भ के बाद अटूट रिक्ति (~)?"),
    "too_many_dots": ("बहुत अधिक बिन्दु", "एक से अधिक '.' क्यों?"),
    "space_cite_punct": ("उद्धरण और विराम चिह्न के बीच रिक्ति", ""),
    "space_after_period_cap": ("बिन्दु और बड़े अक्षर के बीच रिक्ति नहीं", ""),
    "space_after_period_word": ("बिन्दु और शब्द के बीच रिक्ति नहीं", ""),
    "textquotedbl": ("\\textquotedbl का गलत उपयोग", "`` या '' का उपयोग करें।"),
    "math_punct": ("गणित ब्लॉक और विराम चिह्न के बीच रिक्ति", ""),
    "cap_after_math": ("गणित ब्लॉक के बाद बड़ा अक्षर", "गणित ब्लॉक के बाद बड़ा अक्षर क्यों?"),
    "equals_outside_math": ("गणित ब्लॉक के बाहर बराबर चिह्न", "'=' गणित ब्लॉक के अंदर होना चाहिए।"),
    "no_space_before_math": ("गणित ब्लॉक से पहले रिक्ति नहीं", ""),
    "no_space_before_cite": ("उद्धरण से पहले रिक्ति नहीं", ""),
    "footnote_no_stop": ("बिन्दु के बिना फुटनोट", ""),
    "no_space_after_math": ("गणित ब्लॉक के बाद रिक्ति नहीं", ""),
    "no_space_before_macro": ("मैक्रो से पहले रिक्ति नहीं", ""),
    "no_space_after_macro": ("मैक्रो के बाद रिक्ति नहीं", ""),
    "colon_in_math": (": गणित मोड में", "फलन परिभाषित करने के लिए \\colon का उपयोग करें।"),
    "ugly_fraction": ("बदसूरत भिन्न", r"\\nicefrac{ARG1}{ARG2} का उपयोग करें।"),
    "too_many_zeros": ("विभाजक के बिना अधिक शून्य", ""),
    "duplicated_word": ("दोहराया गया शब्द", ""),
    "para_no_stop": ("पैराग्राफ बिन्दु के बिना समाप्त", ""),
    "para_no_cap": ("पैराग्राफ बड़े अक्षर के बिना शुरू", ""),
    "para_starts_dot": ("पैराग्राफ बिन्दु से शुरू होता है?", ""),
    "punct_in_math": ("गणित मोड के अंदर विराम चिह्न", "ARG1 को गणित मोड से बाहर ले जाएं।"),
    "double_dot": ("दो बिन्दु", "एक बिन्दु काफी है।"),
    "space_before_punct_math": ("गणित ब्लॉक के अंत से पहले रिक्ति", ""),
    "space_before_rparen": (") से पहले रिक्ति", ""),
    "proof_no_begin": ("\\end{proof} बिना \\begin", "\\end{proof} से पहले पैराग्राफ विभाजक हटाएं?"),
    "section_has_dot": ("बिन्दु के साथ अनुभाग", "अनुभाग आमतौर पर बिन्दु से समाप्त नहीं होते।"),
    "no_stop_def": ("\\end{definition} से पहले बिन्दु नहीं", ""),
    "no_stop_end": ("\\end{...} से पहले बिन्दु नहीं", ""),
}


def _hindi_specific_rules() -> list:
    """Top 20 Hindi grammatical/typographical errors + LaTeX-Hindi rules."""
    return [
        # LaTeX + Hindi punctuation: space between math block and Devanagari danda
        ["गणित ब्लॉक और दंड के बीच रिक्ति", MATHBLOCK + r"\s+[\u0964\u0965]", "", "दंड के बीच रिक्ति हटाएं।"],
        # Romanized/Hinglish common errors
        simple_rule("pariksha", "parīkṣā"),
        simple_rule("mein school", "school mein"),
        simple_rule("ho tel mein", "hotel mein"),
        simple_rule("ladka achchi", "ladka achcha hai"),
        simple_rule("main gayi hoon", "main gayā hoon"),
    ]


def generate_error_types() -> list:
    """Return Hindi rules."""
    return structural_rules(_MSGS) + _hindi_specific_rules()
