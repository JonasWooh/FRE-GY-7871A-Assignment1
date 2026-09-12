"""Exchange-session event dates and strictly complete price windows."""

import numpy as np
import pandas as pd


def assign_day_zero(acceptance: pd.Series, schedule: pd.DataFrame) -> pd.Series:
    """First session closing strictly after SEC acceptance (timestamps in UTC)."""
    closes = pd.DatetimeIndex(pd.to_datetime(schedule["market_close"], utc=True))
    accepted = pd.to_datetime(acceptance, utc=True)
    positions = closes.searchsorted(accepted, side="right")
    result = pd.Series(pd.NaT, index=acceptance.index, dtype="datetime64[ns]")
    valid = accepted.notna() & (positions < len(schedule))
    result.loc[valid] = pd.DatetimeIndex(schedule.index).tz_localize(None)[positions[valid]].values
    return result


def buy_and_hold_excess(stock: pd.Series, benchmark: pd.Series) -> float:
    """Buy-and-hold difference; caller provides the exact event return window."""
    if stock.empty or len(stock) != len(benchmark) or stock.isna().any() or benchmark.isna().any():
        return np.nan
    return float((1 + stock).prod() - (1 + benchmark).prod())


def event_features(
    meta: pd.DataFrame, prices: pd.DataFrame, volume: pd.DataFrame,
    raw_close: pd.DataFrame, schedule: pd.DataFrame, split_factors: pd.DataFrame,
) -> pd.DataFrame:
    """Missing sessions remain missing: no forward fill or shortened windows."""
    dates = pd.DatetimeIndex(schedule.index).tz_localize(None)
    prices = prices.reindex(dates)
    returns = prices.pct_change(fill_method=None)
    volume = volume.reindex(dates)
    raw_close = raw_close.reindex(dates)
    split_factors = split_factors.reindex(dates)
    benchmark = returns["SPY"]
    alternative = returns["ARKK"]
    rows = []
    for row in meta.itertuples():
        features = {"accession": row.accession}
        if pd.isna(row.day0) or row.ticker not in returns:
            rows.append(features)
            continue
        p = dates.get_loc(row.day0)
        if p < 61 or p + 63 >= len(dates):
            rows.append(features)
            continue
        r = returns[row.ticker]
        pre = r.iloc[p - 60:p - 5]
        post = r.iloc[p + 1:p + 64]
        event = r.iloc[p:p + 4]
        features["pre_vol"] = float(pre.std(ddof=1) * np.sqrt(252)) if pre.notna().all() else np.nan
        features["post_vol"] = float(post.std(ddof=1) * np.sqrt(252)) if post.notna().all() else np.nan
        features["filing_return"] = buy_and_hold_excess(event, benchmark.iloc[p:p + 4])
        features["filing_return_arkk"] = buy_and_hold_excess(event, alternative.iloc[p:p + 4])
        features["pre_return"] = buy_and_hold_excess(pre, benchmark.iloc[p - 60:p - 5])
        features["price_before"] = raw_close[row.ticker].iloc[p - 1] if row.ticker in raw_close else np.nan
        if row.ticker in volume:
            # Express every day's volume in the same share units as day -1.
            v = (volume[row.ticker].iloc[p - 60:p - 5]
                 * split_factors[row.ticker].iloc[p - 60:p - 5]
                 / split_factors[row.ticker].iloc[p - 1])
            features["mean_pre_volume"] = float(v.mean()) if v.notna().all() else np.nan
        rows.append(features)
    return pd.DataFrame(rows)
