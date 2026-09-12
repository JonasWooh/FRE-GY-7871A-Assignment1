import pandas as pd
import pytest

from src.corporate_actions import future_split_factors


def test_split_and_reverse_split_preserve_historical_units():
    splits = pd.DataFrame({"X": [0, 4, 0, .5, 0]})
    factor = future_split_factors(splits)["X"]
    assert factor.tolist() == [2, .5, .5, 1, 1]
    # A historical USD 100 price is stored at USD 50 after net 2-for-1 splitting.
    assert 50 * factor.iloc[0] == 100
    assert 2000 / factor.iloc[0] == 1000
