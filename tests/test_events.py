import numpy as np
import pandas as pd
import pytest

from src.events import assign_day_zero, buy_and_hold_excess, event_features


def test_acceptance_uses_actual_close_and_skips_weekend():
    # Friday after Thanksgiving has an early 13:00 New York close.
    schedule = pd.DataFrame({"market_close": pd.to_datetime([
        "2024-11-29 18:00Z", "2024-12-02 21:00Z", "2024-12-03 21:00Z"
    ])}, index=pd.to_datetime(["2024-11-29", "2024-12-02", "2024-12-03"]))
    accepted = pd.Series(["2024-11-29 17:59Z", "2024-11-29 18:00Z", "2024-11-30 12:00Z", None])
    result = assign_day_zero(accepted, schedule)
    assert result.iloc[0] == pd.Timestamp("2024-11-29")
    assert result.iloc[1] == result.iloc[2] == pd.Timestamp("2024-12-02")
    assert pd.isna(result.iloc[3])


def test_compounded_excess_is_not_sum_of_daily_excess():
    stock = pd.Series([0.1, -0.1, 0.0, 0.1])
    market = pd.Series([0.01, 0.02, 0.03, 0.04])
    assert buy_and_hold_excess(stock, market) == pytest.approx(1.1 * 0.9 * 1.1 - 1.01 * 1.02 * 1.03 * 1.04)
    stock.iloc[1] = np.nan
    assert np.isnan(buy_and_hold_excess(stock, market))


def test_windows_are_complete_and_turnover_uses_consistent_split_units():
    dates = pd.bdate_range("2021-01-01", periods=200)
    schedule = pd.DataFrame({"market_close": dates.tz_localize("UTC") + pd.Timedelta(hours=21)}, index=dates)
    returns = .01 * np.sin(np.arange(200))
    close = 100 * np.cumprod(1 + returns)
    prices = pd.DataFrame({"X": close, "SPY": 100., "ARKK": 100.}, index=dates)
    factors = pd.DataFrame({"X": np.where(np.arange(200) < 40, 4., 1.)}, index=dates)
    volume = 1000 / factors
    raw = prices[["X"]] * factors
    meta = pd.DataFrame({"accession": ["A"], "ticker": ["X"], "day0": [dates[80]]})
    f = event_features(meta, prices, volume, raw, schedule, factors).iloc[0]
    assert f.pre_vol == pytest.approx(np.std(returns[20:75], ddof=1) * np.sqrt(252))
    assert f.post_vol == pytest.approx(np.std(returns[81:144], ddof=1) * np.sqrt(252))
    assert f.mean_pre_volume == pytest.approx(1000)
    assert f.filing_return == pytest.approx(np.prod(1 + returns[80:84]) - 1)
    prices.loc[dates[100], "X"] = np.nan
    f = event_features(meta, prices, volume, raw, schedule, factors).iloc[0]
    assert pd.isna(f.post_vol)
