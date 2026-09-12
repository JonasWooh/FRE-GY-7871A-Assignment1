"""Download prices, volume and point-in-time shares outstanding.

    python scripts/03_get_market_data.py

Writes:
    data/prices/prices.csv   daily auto-adjusted closes, tickers in columns
    data/prices/volume.csv   daily share volume
    data/prices/shares.csv   dei:EntityCommonStockSharesOutstanding, per filing

On shares outstanding. The cover page of every 10-K and 10-Q states the share
count as of a date shortly before filing, and EDGAR exposes it as the XBRL fact
dei:EntityCommonStockSharesOutstanding. That is a point-in-time number: it was
printed on the document you are scoring. Market cap built from today's share
count and a 2021 price is a look-ahead bug, and it is the most common one in
assignments like this.

Some filings will have no such fact. Leave those rows missing rather than filling
them forward from a later filing, and report how many you lost.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config import (  # noqa: E402
    ALT_BENCHMARK, BENCHMARK, INTERIM_DIR, PRICE_DIR, SAMPLE_END, SAMPLE_START,
    SEC_USER_AGENT, VIX_TICKER,
)
from src.edgar import EdgarClient  # noqa: E402
from src.market import download_prices, download_volume  # noqa: E402
from src.corporate_actions import download_as_traded  # noqa: E402

FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

# Use cover-page shares only. Weighted-average EPS denominators are not an
# outstanding share count and must not silently enter the market-cap control.
# Prices need a run-up before the first filing (for the [-60,-6] controls) and a
# run-out after the last one (for the [0,+3] window).
PRICE_START = "2020-09-01"
PRICE_END = "2026-03-31"


def get_shares(client: EdgarClient, meta: pd.DataFrame) -> pd.DataFrame:
    """Exact-accession cover-page shares; latest eligible date, no EPS proxies.

    Conflicting values on the latest date are excluded, not chosen by API order.
    Missing flat-API facts (including some multi-class issuers) remain missing.
    """
    rows = []
    meta = meta.drop_duplicates(subset="accession")
    for i, cik in enumerate(sorted(meta["cik"].unique()), 1):
        facts = client._get(FACTS_URL.format(cik=str(cik).zfill(10))).json().get("facts", {})
        arr = facts.get("dei", {}).get("EntityCommonStockSharesOutstanding", {}).get("units", {}).get("shares", [])
        for filing in meta.loc[meta["cik"] == cik].itertuples():
            candidates = [f for f in arr if f.get("accn") == filing.accession
                          and f.get("val", 0) > 0 and f.get("end")
                          and f["end"] <= str(filing.filing_date)[:10]]
            if not candidates:
                continue
            latest = max(f["end"] for f in candidates)
            values = {f["val"] for f in candidates if f["end"] == latest}
            if len(values) != 1:
                continue
            rows.append({"cik": str(cik).zfill(10), "accession": filing.accession,
                         "shares_outstanding": values.pop(), "shares_as_of": latest,
                         "shares_tag": "dei:EntityCommonStockSharesOutstanding"})
        if i % 20 == 0:
            print(f"  company facts: {i} companies...")
    return pd.DataFrame(rows, columns=["cik", "accession", "shares_outstanding", "shares_as_of", "shares_tag"])


def main() -> int:
    meta = pd.read_csv(INTERIM_DIR / "filings_meta.csv", dtype={"cik": str})
    tickers = sorted(meta["ticker"].unique()) + [BENCHMARK, ALT_BENCHMARK, VIX_TICKER]
    print(f"{len(set(tickers))} tickers, {SAMPLE_START} to {SAMPLE_END}")

    px = download_prices(tickers, PRICE_START, PRICE_END)
    print(f"prices:  {px.shape[0]} days x {px.shape[1]} tickers -> {PRICE_DIR / 'prices.csv'}")
    missing = [t for t in tickers if t not in px.columns or px[t].notna().sum() == 0]
    if missing:
        print(f"  no price history for: {missing}")

    vol = download_volume(tickers, PRICE_START, PRICE_END)
    print(f"volume:  {vol.shape[0]} days x {vol.shape[1]} tickers -> {PRICE_DIR / 'volume.csv'}")

    download_as_traded(tickers, PRICE_START, PRICE_DIR)
    print(f"Historical as-traded prices and volume saved under {PRICE_DIR}")

    if VIX_TICKER in px.columns:
        print(f"VIX:     {px[VIX_TICKER].notna().sum()} days, mean "
              f"{px[VIX_TICKER].mean():.1f} (for the Figure 1 overlay)")

    client = EdgarClient(SEC_USER_AGENT or None)
    shares = get_shares(client, meta)
    shares.to_csv(PRICE_DIR / "shares.csv", index=False)
    matched = meta["accession"].isin(shares["accession"]).mean()
    print(f"shares:  {len(shares)} facts -> {PRICE_DIR / 'shares.csv'} "
          f"({matched:.1%} of filings matched)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
