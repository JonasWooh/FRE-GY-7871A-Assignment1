"""Undo Yahoo's split restatement using the observed corporate-action history."""

import pandas as pd


def future_split_factors(splits: pd.DataFrame) -> pd.DataFrame:
    """Product of split ratios strictly after each date, including reverse splits.

    A zero denotes 'no split' in Yahoo action data. Exclude the date's own action:
    that session's reported price already trades on the post-split basis.
    """
    ratios = splits.fillna(0).replace(0, 1)
    return ratios.iloc[::-1].cumprod().iloc[::-1] / ratios


def download_as_traded(tickers, start, price_dir):
    """Fetch through retrieval day so later splits do not contaminate past size.

    Yahoo Close (auto_adjust=False) still reflects splits, and its historical
    volume uses the same share basis. Restore price by multiplication and volume
    by division. This is an algebraic unit conversion, not a price repair.
    """
    import yfinance as yf
    close_path = price_dir / "as_traded_close.csv"
    volume_path = price_dir / "as_traded_volume.csv"
    factor_path = price_dir / "future_split_factors.csv"
    if close_path.exists() and volume_path.exists() and factor_path.exists():
        return
    end = (pd.Timestamp.now(tz="UTC").normalize() + pd.Timedelta(days=1)).date().isoformat()
    raw = yf.download(tickers=sorted(set(tickers)), start=start, end=end,
                      auto_adjust=False, actions=True, progress=False, threads=True)
    factors = future_split_factors(raw["Stock Splits"])
    (raw["Close"] * factors).to_csv(close_path)
    (raw["Volume"] / factors).to_csv(volume_path)
    factors.to_csv(factor_path)
    raw["Stock Splits"].to_csv(price_dir / "stock_splits.csv")
