import pandas as pd
import pytest
from src.company_comparison import aggregate_companies


def test_equal_filing_mean_differs_from_pooled_token_share_and_counts():
    rows = [
        ('a', 'A', 'Alpha', '10-K', 'a1', '2021-01-01', 100, 10, 2),
        ('a', 'A', 'Alpha', '10-K', 'a2', '2022-01-01', 900, 0, 18),
        ('b', 'B', 'Beta', '10-K', 'b1', '2021-01-01', 1000, 20, 30),
        ('b', 'B', 'Beta', '10-Q', 'b2', '2021-04-01', 100, 30, 4),
    ]
    frame = pd.DataFrame(rows, columns=['cik','ticker','company','form','accession',
        'filing_date','n_words','Negative_count','Uncertainty_count'])
    frame.filing_date = pd.to_datetime(frame.filing_date)
    tables = aggregate_companies(frame)
    summary = tables['company_summary']
    alpha = summary.query("cik == 'a' and form == '10-K' and category == 'Negative'").iloc[0]
    assert alpha.mean_share_pct == 5
    assert alpha.pooled_share_pct == 1
    assert alpha.occurrences == 10
    top = tables['company_top5']
    assert top.query("category == 'Negative' and form == '10-K' and rank == 1").ticker.tolist() == ['A']
    assert top.query("category == 'Negative' and form == 'All' and rank == 1").ticker.tolist() == ['B']
    with pytest.raises(ValueError, match='unique accessions'):
        aggregate_companies(pd.concat([frame, frame.iloc[:1]]))
