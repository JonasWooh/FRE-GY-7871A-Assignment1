from collections import Counter
from math import log

import pytest

from src.tone import score_corpus


def test_hand_calculated_equation_one():
    docs = [Counter({"LOSS": 2, "MAY": 1, "FIRM": 1}), Counter({"MAY": 3, "GAIN": 1})]
    scores = score_corpus(docs, {"Negative": {"LOSS"}, "Uncertainty": {"MAY"}})
    assert scores.loc[0, "Negative_proportional"] == 0.5
    expected = (1 + log(2)) / (1 + log(4 / 3)) * log(2)
    assert scores.loc[0, "Negative_tfidf"] == pytest.approx(expected)
    assert scores.loc[1, "Negative_tfidf"] == 0
    # A word in every document has zero inverse document frequency.
    assert (scores["Uncertainty_tfidf"] == 0).all()


def test_idf_is_reestimated_on_the_provided_corpus():
    docs = [Counter({"LOSS": 1}), Counter({"GAIN": 1})]
    assert score_corpus(docs, {"Negative": {"LOSS"}}).loc[0, "Negative_tfidf"] == pytest.approx(log(2))
    assert score_corpus(docs[:1], {"Negative": {"LOSS"}}).loc[0, "Negative_tfidf"] == 0


def test_empty_document_is_an_explicit_sample_error():
    with pytest.raises(ValueError):
        score_corpus([Counter()], {"Negative": {"LOSS"}})
