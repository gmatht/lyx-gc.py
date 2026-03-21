"""French grammar rules - ported from chktex_fr.pl."""
import re
from ..tokenizer import (
    START_MATH_CHAR,
    END_MATH_CHAR,
    RECURSIVE_BRACE,
    MATHBLOCK,
    NOTINMATH,
    PAR,
    MACROBLOCK,
    LATEX_BS,
)
from ..rules import simple_rule

# Perl [[:digit:]] -> [0-9], [[:alpha:]] -> [a-zA-Z], [[:alnum:]] -> [a-zA-Z0-9]
# [[:upper:]] -> [A-Z], [[:lower:]] -> [a-z], [[:space:]] -> \s
LBS = LATEX_BS


def generate_error_types() -> list:
    """Return list of [Name, Regex, Special, Description]."""
    termdef = r"(?:(?:[A-Z][a-zA-Z0-9]*|dans|un|une|le|la|et|pour|les|de|du|en)\s+)+(?:" + LBS + r"cite\{[^}]*\}\s*)?\("
    capword = r"\b(Monsieur|Madame|M\.|Mme\.|(Lun|Mar|Mecre|Jeu|Vendre)di|Dimanche|Isabelle|CTL|PSPACE|Emerson|Katoen|Clarke|Baier|Kripke)\b"
    lowerword = r"\b(?<!\\)[a-z]+\b"
    names = r"Hilbert|Gentzen|Coomb|Hare|Marquis|Khachian"
    s = r"(?:\n|\s)"

    return [
        # Lines 18-53 (first batch) + 55-88 (from nested sub - merged)
        ["Empty mathblock", START_MATH_CHAR + "  *" + END_MATH_CHAR, "", ""],
        ["Macro sans {}.", r"[^\\]" + LBS + r"[a-zA-Z0-9]+?CTL[a-zA-Z0-9]+\s", "", "Une {} est probablement nécessaire après la macro pour ne pas supprimer l'espace"],
        ["Le second mot de la phrase commence par une majuscule.", r"[.]\s+[a-zA-Z0-9]+\s+(?!" + capword + r")[A-Z]", "", "Quand le second mot possède une majuscule, c'est généralement une erreur."],
        ["pas de point d'arrêt après une citation en fin de paragraphe", r"[a-zA-Z0-9]\s+" + LBS + r"cite\{[^}]*\}\s*" + PAR, "", "Je pense qu'un arrêt total manque ici."],
        ["Espace après citation", LBS + r"cite\{[^}]*\}[a-zA-Z0-9]", "", ""],
        ["Espace avant citation", r"[a-zA-Z0-9]" + LBS + r"cite\{[^}]*\}", "", ""],
        ["Le soulignement commence trop tôt", LBS + r"uline\{\s", "", ""],
        ["Le soulignement fini trop loin", LBS + r"uline\{[^}]\s\}", "", ""],
        ["Espace avant note de bas de page", r"(?: %\s+| )" + LBS + r"footnote\{", "", ""],
        ["Point/Virgule après note de bas de page", LBS + r"footnote" + RECURSIVE_BRACE + r'[.,]', "", "Si la note de bas de page fait référence à la phrase complète, elle doit se situer après la phrase en question."],
        ["Ponctuation double", r'(?<!\\)[,.:;]\s+[,.:;]', "", ""],
        ["Utilisation d'une implication dans une preuve", r'(?:(?:' + LBS + r'left)?\(' + LBS + r'implies(?:' + LBS + r'right)?\)|\(.' + LBS + r'implies.\))', "", "L'utilisation de (\\implies) engendre une espace indésirable entre la fléche et les crochets. Pour indiquer la direction d'une preuve, il est préférable d'utiliser '(\\Longrightarrow)'"],
        ["Pas d'espace après un référencement", r'ref\{[^}]*\}[a-zA-Z0-9]', "", ""],
        ["Un seul caractère", r'\s[b-z]\s(?![&' + LBS + r'])' + r"(?![^" + re.escape(START_MATH_CHAR) + r"]*[_" + re.escape(END_MATH_CHAR) + r"])", "", "Un caractère unique n'a, a priori, pas de sens ?"],
        ["Majuscule au milieu d'une phrase", r"(?!(?:en|du|de|avec)\b)(?:" + lowerword + r"|ref\{[^{}]*\}),?:?(?:(%.*\n)|\s)+(?!" + capword + r")([A-Z][a-zA-Z0-9]*)", "erase:(?:" + LBS + r"(?:chapter|(?:sub)*section[*]?" + RECURSIVE_BRACE + r")|" + MATHBLOCK + r")", "ARG2~CAP, 1;ARG1, 2;ARG2"],
        ["Block Begin/End vide", LBS + r"begin\{[^}]+\}\s*(?:" + LBS + r"par)?" + LBS + r"end\{[^}]*\}", "", ""],
        ["La preuve ne démarre pas sur une nouvelle ligne", r'.+' + LBS + r'begin\{proof\}', "Il semble que le lemme/théorème et sa preuve soit sur la même ligne.\n(utilisez la touche \"Entrée\" dans LyX pour en ajouter une)"],
        ["Pas d'espace entre une référence et le texte à sa gauche", r'[a-zA-Z0-9]' + LBS + r'(pretty)?ref\{', "Peut-être souhaitez-vous une espace insécable\n('~' ou Ctrl-Espace dans LyX)\n entre une référence et le texte ?"],
        ["Pas d'espace entre une référence et le texte à sa droite", r'^.' + LBS + r'(?:pretty)?ref\{', "Perhaps you should add a non-breaking space \n('~' or Ctrl-Space in the LyX GUI)\n between the text and the reference?"],
        ["Trop de points", r'[.]\s+[.]', "Pourquoi avoir plusieurs points '.' ?"],
        ["Trop de points", r'[.][ ][.]', "Pourquoi avoir plusieurs points '.' ?"],
        ["Trop de points", r"^.\s+[A-Z]", "Pourquoi avoir plusieurs points '.' ?"],
        ["Trop de points", r'[.][ ][.]', "Pourquoi avoir plusieurs points '.' ?"],
        ["espace entre la citation et la ponctuation", LBS + r"cite\{[^{}]*\}\s+[,.]", "", ""],
        ["Espace manquant entre point et majuscule", r'[.][A-Z][^.]', "", "Un espace est probablement manquant entre le . et la majuscule ?"],
        ["Espace manquant entre point et mot", r'[.][a-z]+[ \t]', "", "Un espace est probablement manquant entre le . et le mot ?"],
        ["Mauvaise usage des guillements", LBS + r'textquotedbl\{[}]', "", "Il faut plutôt utiliser `` ou '' à la place de \\textquotedbl{} ou '\""],
        ["Espace entre block de math et ponctuation", MATHBLOCK + r'\s+[,.]', "", 'Pourquoi une majuscule est placé après un block de math ?'],
        ["Majuscule après block de math", r'[a-zA-Z0-9] ' + MATHBLOCK + r' (?!' + capword + r')(?!Robustly)[A-Z]', "", 'Pourquoi se trouve une majuscule après un block de math?'],
        ["Signe égal '=' en dehors d'un block de math", MATHBLOCK + r'\s*=\s*' + MATHBLOCK, "", "Le signe égal '=' devrait peut-être se trouver à l'intérieur du block de math ?"],
        ["Pas d'espace avant un block de math", r"[a-zA-Z0-9]" + START_MATH_CHAR + r"(?!_|\^|" + LBS + r"dots)", "", ""],
        ["Pas d'espace avant une citation", r"[^\s(~]" + LBS + r"cite", "", ""],
        # From nested sub (lines 55-88)
        ["Majuscule après virgule", r",\s*(?!b|" + names + r"|Coomb|Hare\b|Marquis\b|Khachian\b|Dominating\s+Set\b|Impartial\s+Culture\b)[A-Z][a-z]", 'Supprimer la majuscule après la virgule ARG1', ""],
        # Exclude known proper nouns and acronyms; exclude \n (paragraph start).
["Majuscule inattendue", r'[^.\n?:}](?<![.]\'\')(?<![.]\')(?<![.]")\s+(?!(?:Isabelle|CTL|PSPACE|Emerson|Katoen|Clarke|Baier|Kripke)\b)[A-Z]', 'Supprimez la majuscule', ""],
        ["La note de bas de page manque un point", r"[a-zA-Z0-9,]\s*" + LBS + r"footnote" + RECURSIVE_BRACE + r"\s*[A-Z]", "", ""],
        ["La note de bas de page manque un point", r"[a-zA-Z0-9,](\s|%)*" + LBS + r"footnote" + RECURSIVE_BRACE + r"\s*[A-Z]", "", ""],
        ["Pas d'espace après block de math", r'(?!..sim)' + MATHBLOCK + r'(?<!dots.)(?!s\s)[a-zA-Z0-9]', "..sim", ""],
        ["Pas d'espace avant une macro", r"[a-zA-Z0-9]" + MACROBLOCK, "", ""],
        ["Pas d'espace après une macro", MACROBLOCK + r'[a-zA-Z0-9]', "", ""],
        ["Un(e) utilisé avec un pluriel", r'\b(Un|Une)\s+sequences\b', "", ""],
        ["Utilisation de : dans le mode math", START_MATH_CHAR + r'[^' + END_MATH_CHAR + r']*(?<!' + LBS + r')[a-zA-Z]:', "", "LaTeX pense qu'un ':' dans le mode math signifie une division, utilisez plutôt \\colon si vous souhaitez définir une fonction."],
        ["Fraction disgracieuse", r"([0-9])/([0-9])(?!n[}])(?!_home)", "erase:" + LBS + r"url" + RECURSIVE_BRACE, r"Utilisez \nicefrac{ARG1}{ARG2} à la place."],
        ["Trop de zéros sans séparateur", r"(?<![0-9.])0000(?![^\s]*[.]tex[}])", "", "Une virgule ou une espace fine est manquante"],
        ["Mot dupliqué", r'(?i)\b([a-zA-Z]+)\b[,.;]?\s+\b\2\b' + NOTINMATH, 'ARG1 apparaît deux fois.', ""],
        ["Un paragraphe doit se terminer par un point", r"[a-zA-Z0-9](?<!iffalse)(?<!maketitle)(?<!medskip)(?<!hline)(?<![A-Z]{3})(?<!\\else)(?<!" + LBS + r"fi)[ \t]*\n\n", "", ""],
        ["Un paragraphe doit commencer par une majuscule", PAR + r"[a-z]", "", ""],
        ["Paragraphe démarrant par un point ?", PAR + r"\.", "", ""],
        ["Ponctuation à l'intérieur du mode math", r".([,.:?])" + END_MATH_CHAR, "", "Déplacez ARG1 en dehors du mode math"],
        ["Deux points", r'\. \.', "", "Un seul point suffit probablement."],
        # In French typography, only ; ? ! require space before. Period and comma do not.
# Exclude : when followed by letter (e.g. \label{thm:principal}).
["Ajouter une espace avant ponctuation", r"(?<!\\)\b[a-zA-Z0-9]+(?:" + LBS + r"@)?([;?!]|:(?![a-zA-Z]))(?!=)", "", "Ajouter une espace avant ARG1"],
        ["Supprimer une espace avant punctuation", r"(?<!\\)\b[a-zA-Z0-9]+\s+(['])", "", "Supprimez l'espace avant ARG1... ou peut-être souhaitez-vous «`» au lieu de «'» ?"],
        ["Les entrées de l'index commencent par une majuscule", LBS + r"index\{[a-z]", "", ""],
        ["Vous devriez utiliser Var()", LBS + r"[Vv]ari\[|" + LBS + r"sigma\(|" + LBS + r"sigma\^{2}[}]\(|" + LBS + r"cov\[", r"\bit\s+that\b", "", "En statistiques, la variance s'utilise avec Var(). Même si vous utilisez E[X] au lieu de E(X). Étonnant hein ?"],
        ["Utilisation de prettyref sans préfixe", LBS + r"prettyref\{[^}]*\}", "", 'Si vous utilisez prettyref pour référencer un chapitre, le label doit commencer par "cha:", "sec:" pour une section, etc.'],
        ["Label «Lemme» sans «lem:»", LBS + r"begin\{lem\}\s+" + LBS + r"label\{(?!lem:)", "", 'Si vous démarrez un label «Lemme» sans lem, prettyref peut-être confus.'],
        ["Label «Corollaire» sans «cor:»", LBS + r"begin\{cor\}\s+" + LBS + r"label\{(?!cor:)", "", 'Si vous démarrez un label «Corollaire» sans cor, prettyref peut-être confus.'],
        ["Label «Théorème» sans «thm:»", LBS + r"begin\{thm\}\s+" + LBS + r"label\{(?!thm:)", "", 'Si vous démarrez un label «Théorème sans thm, prettyref peut-être confus.'],
        ["Préfixe Lemme manquant", r"\b(?!Lemme|and)[^\s~]+[~\s]+" + LBS + r"ref\{lem:", "", ""],
        ["Préfixe Corollaire maquant", r"\b(?!Corollaire)[^~\s]+[~\s]+" + LBS + r"ref\{cor:", "", ""],
        ["Préfixe Théorème maquant", r"\b(?!Théorème|et)[^\s~]+[~\s]+" + LBS + r"ref\{thm:", "", ""],
        ["Référence en minuscule", r"(lemme|théorème|table|figure|corollaire)[~ ]" + LBS + r"ref\b", "", "La premiére lettre de ARG1 devrait être en majuscule en accord avec le standard \\prettyref LaTeX."],
        ["lemme/théorème apparaît avant prettyref", r"(emma|héorèm|xemples|Exemple|orollaire|éfinition)\s+" + LBS + r"prettyref\b", "", "Il vaut mieux utiliser une référence formatté (i.e. \\prettyref), plutôt qu'un formattage manuel des références, parce qu'une référence formattée va automatiquement changer la référence si l'objet référencé est modifié (passage d'un lemme à un théorème par exemple)."],
        ["Note de bas de page vide", LBS + r"footnote\{(\s|\n)*\}", "", "Peut-être devriez-vous la supprimer"],
        ["Section se terminant par un '.'", LBS + r"(?:sub)*section\{[^}]*[.]\}\s*(?:\n|$|\\)", "", "Terminer une section avec un point n'est pas commun"],
        ["Pas d'espace avant ponctuation", END_MATH_CHAR + r'+(?:' + LBS + r'[@])?([;.,])', "", "Il manque un espace avant la fin du block math et 'ARG1'"],
        ["Espace avant «)»", END_MATH_CHAR + r"[^" + START_MATH_CHAR + r"]*\s\)", "", ""],
        ["Fin de preuve sans début", PAR + LBS + r'end\{proof\}', "", "Vous devriez probablement supprimer le saut de paragraphe avant \\end{proof}"],
        ["pas de point à la fin de la définition", r"[a-zA-Z0-9]\s*" + LBS + r"end\{definition\}", "", ""],
        ["pas de point à la fin de .*", r"[a-zA-Z0-9](?:\s|%[^\n]*)*" + LBS + r"end\{(?!algorithmic|enum|item|array|eqnarray|align|document|proof)", "", ""],
    ]
