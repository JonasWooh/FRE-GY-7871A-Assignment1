"""Build the frozen assignment universe using reviewed security-to-issuer keys.

Default: enumerate SEC filings for approved CIKs. --from-local-filings reuses
and checks the prior full download, and removes obsolete identities.
"""
import argparse
import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config import UNIVERSE_DIR, INTERIM_DIR, SAMPLE_START, SAMPLE_END, FORMS
from src.edgar import EdgarClient
from src.universe import resolve_holdings, enumerate_universe


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from-local-filings', action='store_true')
    args = ap.parse_args()
    raw = pd.read_csv(UNIVERSE_DIR/'ark_holdings_raw.csv', dtype=str)
    holdings = resolve_holdings(raw)
    if args.from_local_filings:
        meta_path = INTERIM_DIR/'filings_meta.csv'
        meta = pd.read_csv(meta_path, dtype={'cik': str})
        from src.issuer_map import VERIFIED_FILING_COUNTS
        def get_filings(cik):
            frame = meta.loc[meta.cik.eq(cik)].drop_duplicates('accession')
            observed = (int(frame.form.eq('10-K').sum()), int(frame.form.eq('10-Q').sum()))
            if observed != VERIFIED_FILING_COUNTS[cik]:
                raise ValueError(f'Incomplete local filings for {cik}: {observed}; run full download')
            return frame
    else:
        client = EdgarClient()
        def get_filings(cik):
            frame = client.list_filings(cik, FORMS, SAMPLE_START, SAMPLE_END)
            return pd.DataFrame(columns=['form']) if frame.empty else frame
    audit, universe = enumerate_universe(holdings, get_filings)
    audit.to_csv(UNIVERSE_DIR/'holding_resolution.csv', index=False)
    universe.to_csv(UNIVERSE_DIR/'universe.csv', index=False)
    if args.from_local_filings:
        allowed = set(zip(universe.ticker, universe.cik))
        retained = [pair in allowed for pair in zip(meta.ticker, meta.cik)]
        meta.loc[retained].to_csv(meta_path, index=False)
    print(audit.groupby('status').size().to_string())
    print(f'{len(universe)} eligible listings; {universe.cik.nunique()} issuers; '
          f'{int(universe.n_10k.sum()+universe.n_10q.sum())} filing-listing records')


if __name__ == '__main__':
    main()
