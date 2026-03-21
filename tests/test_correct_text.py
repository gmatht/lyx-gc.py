"""Test that grammatically correct text does not trigger any rules.

Sample texts (~1 page each) that passed the original Perl chktex rules.
The Python implementation should also report zero errors for these.
"""
import io
import pytest

from lyxgc.engine import find_errors
from lyxgc.lang import get_generate_error_types

generate_en = get_generate_error_types("en")
generate_fr = get_generate_error_types("fr")


# ~1 page of grammatically correct English LaTeX (academic style)
SAMPLE_EN = r"""
\documentclass{article}
\begin{document}

\section{Introduction}

This paper studies the complexity of model checking for branching-time temporal
logics. We show that the problem is PSPACE-complete for a broad class of
formulas. Our results extend earlier work by Clarke and Emerson, who established
the decidability of the problem for computational tree logic (CTL).

The remainder of this paper is organised as follows. In Section~2 we recall
the necessary definitions. Section~3 presents our main theorem. We conclude
with a discussion of open problems. All proofs have been formalised with
Isabelle.

\section{Preliminary Definitions}

Let $\mathcal{M}$ be a Kripke structure over a set of atomic propositions.
A path $\pi$ in $\mathcal{M}$ is an infinite sequence of states. We say that
$\pi$ satisfies a CTL formula $\phi$ when $\phi$ holds at the initial state
of $\pi$ under the usual semantics of path quantifiers and temporal operators.

For example, the formula $\mathbf{AG}\, p$ states that $p$ holds at every
state along every path. We refer the reader to Clarke and Emerson for a
comprehensive treatment of these notions.

\section{Main Result}

\begin{theorem}\label{thm:main}
The model-checking problem for CTL is PSPACE-complete.
\end{theorem}

\begin{proof}
The upper bound follows from a nondeterministic algorithm that guesses a
witness path. The lower bound is by reduction from quantified Boolean formulas.
\end{proof}

As an immediate corollary we obtain that the problem remains hard when
restricted to the fragment of formulas without nested path quantifiers.
\end{document}
"""

# ~1 page of grammatically correct French LaTeX
SAMPLE_FR = r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[french]{babel}
\begin{document}

\section{Introduction}

Cet article étudie la complexité de la vérification de modèles pour les
logiques temporelles à branches. Nous montrons que le problème est
PSPACE-complet pour une large classe de formules. Nos résultats prolongent
les travaux antérieurs de Clarke et Emerson, qui ont établi la décidabilité
du problème pour la logique des arbres de calcul (CTL).

Le reste de cet article est organisé comme suit. La section~2 rappelle les
définitions nécessaires. La section~3 présente notre théorème principal.
Nous concluons par une discussion des problèmes ouverts. Toutes les preuves
ont été formalisées dans l’assistant de preuve Isabelle.

\section{Définitions préliminaires}

Soit $\mathcal{M}$ une structure de Kripke sur un ensemble de propositions
atomiques. Un chemin $\pi$ dans $\mathcal{M}$ est une suite infinie d’états.
Nous disons que $\pi$ satisfait une formule CTL $\phi$ lorsque $\phi$ est
vraie à l’état initial de $\pi$ sous la sémantique usuelle des quantificateurs
de chemin et des opérateurs temporels.

Par exemple, la formule $\mathbf{AG}\, p$ exprime que $p$ est vraie à
chaque état le long de chaque chemin. Nous renvoyons le lecteur à l’ouvrage
de Baier et Katoen pour un traitement complet de ces notions.

\section{Résultat principal}

\begin{theoreme}\label{thm:principal}
Le problème de vérification de modèles pour CTL est PSPACE-complet.
\end{theoreme}

\begin{preuve}
La borne supérieure provient d’un algorithme non déterministe qui devine
un chemin témoin. La borne inférieure est par réduction depuis les formules
booléennes quantifiées.
\end{preuve}

En corollaire immédiat nous obtenons que le problème reste difficile lorsque
restreint au fragment de formules sans quantificateurs de chemin imbriqués.
\end{document}
"""


def _run_find_errors(error_types, tex: str) -> int:
    """Run find_errors and return error count."""
    out = io.StringIO()
    n = find_errors(
        error_types,
        [out],
        tex,
        "sample.tex",
        min_block_size=0,
        output_format="-v0",
    )
    return n


def test_correct_english_text_triggers_no_rules():
    """Grammatically correct English text should not trigger any rules."""
    error_types = generate_en()
    n = _run_find_errors(error_types, SAMPLE_EN)
    assert n == 0, f"Expected 0 errors for correct English text, got {n}"


def test_correct_french_text_triggers_no_rules():
    """Grammatically correct French text should not trigger any rules."""
    error_types = generate_fr()
    n = _run_find_errors(error_types, SAMPLE_FR)
    assert n == 0, f"Expected 0 errors for correct French text, got {n}"
