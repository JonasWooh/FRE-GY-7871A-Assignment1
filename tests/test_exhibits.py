"""End-to-end exhibit construction using independent simulated observations."""
import numpy as np
import pandas as pd

from src import analysis


def test_all_exhibits_build_on_a_complete_simulated_panel(tmp_path, monkeypatch):
    rng = np.random.default_rng(7871)
    rows = []
    for firm in range(12):
        baseline = rng.normal()
        for time in range(20):
            for form in ["10-K", "10-Q"]:
                row = {"cik": str(firm), "form": form, "time": time,
                       "quarter": str(pd.Period("2021Q1") + time), "season": time % 4 + 1,
                       "log_size": 20 + rng.normal(), "log_turnover": -4 + rng.normal(),
                       "log_words": 10 + rng.normal(), "pre_return": rng.normal(0, .1),
                       "log_pre_vol": rng.normal(-1, .2)}
                for measure in analysis.MEASURES:
                    row[measure] = 5 + .1 * time + baseline + rng.normal()
                row["log_post_vol"] = .6 * row["log_pre_vol"] + rng.normal(0, .2)
                row["filing_return"] = rng.normal(0, .05)
                rows.append(row)
    meta = pd.DataFrame(rows)
    for measure in analysis.MEASURES:
        meta[measure + "_z"] = (meta[measure] - meta[measure].mean()) / meta[measure].std()
    prices = pd.DataFrame({"^VIX": np.linspace(15, 25, 20)}, index=pd.date_range("2021-01-01", periods=20, freq="QS"))
    monkeypatch.setattr(analysis, "RESULTS", tmp_path)
    tables = analysis.make_exhibits(meta, prices)
    assert len(tables["table4_trends"]) == 28
    assert len(tables["regressions"]) == 18
    assert len(tables["table6_power"]) == 6
    # A clear planted positive trend should be recovered in every within fit.
    within = tables["table4_trends"].query("covariance == 'Firm and quarter clusters'")
    assert within.coefficient.between(.06, .14).all()
    assert tables["regressions"].n.isin([240, 480]).all()
    assert (tmp_path / "figure1.png").stat().st_size > 1000
