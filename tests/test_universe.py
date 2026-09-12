"""Identity regressions from real cross-market ticker collisions."""
import pandas as pd
import pytest
from src.universe import resolve_holdings, enumerate_universe


def holdings():
    return pd.DataFrame([
        ('AIR', '4012250', 'AIRBUS SE', 'ARKX'),
        ('DSY', '6177878', 'DISCOVERY LTD', 'ARKF'),
        ('DSY FP', 'BM8H5Y5', 'DASSAULT SYSTEMES SE', 'ARKX'),
    ], columns=['ticker', 'cusip', 'company', 'fund'])


def test_same_ticker_in_different_markets_keeps_distinct_issuers():
    resolved = resolve_holdings(holdings()).set_index('raw_ticker')
    assert resolved.loc['AIR', 'cik'] == '0001697546'
    assert resolved.loc['DSY FP', 'cik'] == '0001016118'
    assert resolved.loc['DSY', 'resolution'] == 'no_verified_sec_match'
    assert not resolved.cik.isin(['0000001750', '0001999297']).any()
    assert len(resolved) == 3


def test_unknown_security_cannot_inherit_another_issuers_cik():
    raw = holdings()
    raw.loc[0, 'company'] = 'AAR CORP'
    with pytest.raises(ValueError, match='Unreviewed holding identity'):
        resolve_holdings(raw)


def test_no_target_filings_and_unmatched_identity_are_different_exclusions():
    resolved = resolve_holdings(holdings())
    calls = []
    def no_target_filings(cik):
        calls.append(cik)
        return pd.DataFrame(columns=['form'])
    audit, eligible = enumerate_universe(resolved, no_target_filings)
    assert eligible.empty
    assert len(calls) == 2
    assert audit.status.value_counts().to_dict() == {'no_10x_filings': 2, 'no_verified_sec_match': 1}
