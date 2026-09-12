"""Proportional tone and Loughran-McDonald (2011), equation (1).

Pass only the final analysis corpus. IDF is descriptive, fitted to that corpus;
it must not be presented as an out-of-sample trading predictor.
"""

from collections import Counter
from collections.abc import Mapping, Sequence
from math import log

import pandas as pd


def score_corpus(
    documents: Sequence[Mapping[str, int]],
    word_lists: Mapping[str, set[str]],
) -> pd.DataFrame:
    """Return one row per document, preserving input order.

    a_j is the mean count over distinct observed tokens, total / distinct.
    Category tf.idf scores sum equation-(1) weights, without a second length
    division. Proportional scores are fractions, not percentages.
    Counts and lexicons must use the same token normalization.
    """
    if not documents:
        raise ValueError("The analysis corpus is empty")
    document_frequency = Counter()
    for counts in documents:
        if not counts or any(not isinstance(n, int) or n <= 0 for n in counts.values()):
            raise ValueError("Each document must contain positive integer token counts")
        document_frequency.update(counts.keys())
    n_documents = len(documents)
    rows = []
    for counts in documents:
        total = sum(counts.values())
        average = total / len(counts)
        normalization = 1 + log(average)
        row = {"n_words": total, "n_distinct": len(counts)}
        for category, words in word_lists.items():
            selected = counts.keys() & words
            row[f"{category}_proportional"] = sum(counts[w] for w in selected) / total
            row[f"{category}_tfidf"] = sum(
                (1 + log(counts[w])) / normalization
                * log(n_documents / document_frequency[w])
                for w in selected
            )
        rows.append(row)
    return pd.DataFrame(rows)
