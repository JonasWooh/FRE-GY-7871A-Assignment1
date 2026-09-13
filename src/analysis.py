"""Reproducible assignment exhibits, with an explicit common analysis sample."""

import gzip
import json
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_market_calendars as mcal
import statsmodels.formula.api as smf
from scipy.stats import norm, t

from .config import ROOT, INTERIM_DIR, PRICE_DIR, UNIVERSE_DIR
from .events import assign_day_zero, event_features
from .lexicons import load_all
from .parse import tokenize
from .tone import score_corpus

MEASURES = [f"{category}_{weight}" for category in ["Negative", "Uncertainty"]
            for weight in ["proportional", "tfidf"]]
RESULTS = ROOT / "results"


def read_panel(path):
    return pd.read_csv(path, index_col=0, parse_dates=True).sort_index()


def prepare_sample():
    """Return common complete-case sample and a reconciled exclusion waterfall."""
    universe = pd.read_csv(UNIVERSE_DIR / "universe.csv", dtype={"cik": str})
    resolution = pd.read_csv(UNIVERSE_DIR / "holding_resolution.csv", dtype={"cik": str})
    expected = int(universe.n_10k.sum() + universe.n_10q.sum())
    meta = pd.read_csv(INTERIM_DIR / "filings_meta.csv", dtype={"cik": str})
    allowed = set(zip(universe.ticker, universe.cik))
    if any(pair not in allowed for pair in zip(meta.ticker, meta.cik)):
        raise ValueError("Filing metadata contains an issuer outside the reviewed universe; rebuild step 01")
    meta["filing_date"] = pd.to_datetime(meta.filing_date)
    meta["acceptance_datetime"] = pd.to_datetime(meta.acceptance_datetime, utc=True)
    waterfall = [{"stage": "Eligible SEC filings in 2021-2025", "remaining": expected, "removed": 0},
                 {"stage": "Downloaded and parsed", "remaining": len(meta), "removed": expected-len(meta)}]
    if len(meta) > expected:
        raise ValueError("Parsed metadata exceeds the enumerated filing universe")
    exclusions = []

    def keep(condition, label):
        nonlocal meta
        condition = condition.fillna(False)
        removed = meta.loc[~condition, ["ticker", "accession"]].copy()
        removed["reason"] = label
        exclusions.append(removed)
        meta = meta.loc[condition].copy()
        waterfall.append({"stage": label, "remaining": len(meta), "removed": len(removed)})

    keep(~meta.accession.duplicated(), "Unique accession")
    keep(meta.form.isin(["10-K", "10-Q"]) & meta.filing_date.between("2021-01-01", "2025-12-31"), "Required forms and filing dates")
    keep(meta.n_words.ge(2000), "At least 2,000 parsed tokens (both forms)")
    schedule = mcal.get_calendar("NYSE").schedule("2020-09-01", "2026-03-30")
    meta["day0"] = assign_day_zero(meta.acceptance_datetime, schedule)
    keep(meta.day0.notna(), "Observed acceptance and tradable day 0")
    moved = int(meta.day0.ne(meta.filing_date).sum())
    prices = read_panel(PRICE_DIR / "prices.csv")
    volume = read_panel(PRICE_DIR / "as_traded_volume.csv")
    raw = read_panel(PRICE_DIR / "as_traded_close.csv")
    factors = read_panel(PRICE_DIR / "future_split_factors.csv")
    features = event_features(meta, prices, volume, raw, schedule, factors)
    meta = meta.merge(features, on="accession", validate="one_to_one")
    shares = pd.read_csv(PRICE_DIR / "shares.csv", dtype={"cik": str})
    meta = meta.merge(shares.drop(columns="cik"), on="accession", how="left", validate="one_to_one")
    keep(meta.shares_outstanding.gt(0) & meta.shares_tag.eq("dei:EntityCommonStockSharesOutstanding"), "Unambiguous exact-filing cover-page shares")
    # Convert the reported share units if a split separates the cover-page date
    # and the previous session. This uses action ratios, not later share counts.
    dates = pd.DatetimeIndex(schedule.index).tz_localize(None)
    for i, row in meta.iterrows():
        before_date = dates[dates.get_loc(row.day0) - 1]
        asof_pos = factors.index.searchsorted(pd.Timestamp(row.shares_as_of), side="right") - 1
        before_pos = factors.index.searchsorted(before_date, side="right") - 1
        if asof_pos < 0 or before_pos < 0:
            raise ValueError("Share date precedes available corporate-action history")
        ratio = factors[row.ticker].iloc[asof_pos] / factors[row.ticker].iloc[before_pos]
        meta.loc[i, "shares_price_basis"] = row.shares_outstanding * ratio
    keep(meta.price_before.notna(), "Observed unadjusted previous-session close")
    keep(meta.price_before.ge(3), "Unadjusted previous-session close at least USD 3")
    keep(meta.filing_return.notna(), "Complete four-day stock and SPY returns")
    keep(meta.pre_vol.gt(0) & meta.pre_return.notna(), "Complete 55-day pre-filing return window")
    keep(meta.post_vol.gt(0), "Complete 63-day post-filing return window")
    keep(meta.mean_pre_volume.gt(0), "Complete positive pre-filing volume control")
    meta["market_cap"] = meta.price_before * meta.shares_price_basis
    meta["turnover"] = meta.mean_pre_volume / meta.shares_price_basis
    keep(np.isfinite(meta.market_cap) & np.isfinite(meta.turnover), "Finite size and turnover controls")
    # Statistical comparisons must use the same documents that define IDF.
    meta = meta.sort_values(["cik", "filing_date", "accession"]).reset_index(drop=True)
    counts = []
    for row in meta.itertuples():
        with gzip.open(ROOT / row.text_path, "rt", encoding="utf-8") as stream:
            c = Counter(tokenize(stream.read()))
        if sum(c.values()) != row.n_words:
            raise ValueError(f"Parser counts disagree with metadata for {row.accession}")
        counts.append(c)
    word_lists = {k: v for k, v in load_all().items() if k in ["Negative", "Uncertainty"]}
    scores = score_corpus(counts, word_lists)
    meta = pd.concat([meta, scores[MEASURES]], axis=1)
    meta["quarter"] = meta.filing_date.dt.to_period("Q").astype(str)
    meta["time"] = (meta.filing_date.dt.year - 2021) * 4 + meta.filing_date.dt.quarter - 1
    meta["season"] = meta.filing_date.dt.quarter
    meta["firm_form"] = meta.cik + "_" + meta.form
    meta["log_size"] = np.log(meta.market_cap)
    meta["log_turnover"] = np.log(meta.turnover)
    meta["log_words"] = np.log(meta.n_words)
    meta["log_pre_vol"] = np.log(meta.pre_vol)
    meta["log_post_vol"] = np.log(meta.post_vol)
    for measure in MEASURES:
        sd = meta[measure].std(ddof=1)
        if not sd > 0:
            raise ValueError(f"No variation in {measure}")
        meta[measure + "_z"] = (meta[measure] - meta[measure].mean()) / sd
    total_words = Counter()
    for c in counts:
        total_words.update(c)
    top_rows = []
    for category, words in word_lists.items():
        category_counts = Counter({w: total_words[w] for w in words if total_words[w]})
        total = category_counts.total()
        for rank, (word, count) in enumerate(sorted(category_counts.items(), key=lambda x: (-x[1], x[0]))[:30], 1):
            top_rows.append({"category": category, "rank": rank, "word": word, "count": count,
                             "share_pct": 100 * count / total})
    audit = {"snapshot_positions": len(pd.read_csv(UNIVERSE_DIR / "ark_holdings_raw.csv")),
             "snapshot_securities": len(resolution),
             "holding_status_counts": {str(k): int(v) for k, v in resolution.status.value_counts().items()},
             "cik_matches": int(resolution.resolution.eq("verified").sum()),
             "domestic_filers": int(universe.status.eq("domestic_filer").sum()),
             "eligible_unique_ciks": int(universe.loc[universe.status.eq("domestic_filer"), "cik"].nunique()),
             "eligible_filings": expected, "day0_moved_before_market_filters": moved,
             "day0_moved_final": int(meta.day0.ne(meta.filing_date).sum()),
             "final_filings": len(meta), "final_firms": int(meta.cik.nunique()),
             "negative_words": len(word_lists["Negative"]), "uncertainty_words": len(word_lists["Uncertainty"]),
             "lexicon_overlap": len(word_lists["Negative"] & word_lists["Uncertainty"]),
             "total_final_tokens": int(meta.n_words.sum()),
             "forms": {k: int(v) for k, v in meta.form.value_counts().items()},
             "dictionary_vintage": "Downloaded from the starter repository's specified URL"}
    return meta, pd.DataFrame(waterfall), pd.DataFrame(top_rows), pd.concat(exclusions, ignore_index=True), audit, prices


def fit_panel(formula, data):
    """Two-way cluster covariance: repeated firms and common filing quarters."""
    groups = np.column_stack([pd.factorize(data.cik)[0], pd.factorize(data.quarter)[0]])
    return smf.ols(formula, data=data, missing="raise").fit(
        cov_type="cluster", cov_kwds={"groups": groups, "use_correction": True, "df_correction": True}, use_t=True)


def coefficient_row(result, term, **labels):
    confidence = result.conf_int().loc[term]
    return dict(labels, term=term, coefficient=float(result.params[term]),
                se=float(result.bse[term]), t=float(result.tvalues[term]), p=float(result.pvalues[term]),
                ci_low=float(confidence.iloc[0]), ci_high=float(confidence.iloc[1]),
                n=int(result.nobs), r_squared=float(result.rsquared))


def make_exhibits(meta, prices):
    summary = meta.groupby("form")[MEASURES].describe(percentiles=[.25, .5, .75]).stack(level=0, future_stack=True).reset_index()
    summary = summary.rename(columns={"level_1": "measure"})
    corr_rows = []
    for form, group in meta.groupby("form"):
        for a in MEASURES:
            for b in MEASURES:
                corr_rows.append({"form": form, "measure_a": a, "measure_b": b, "correlation": group[a].corr(group[b])})

    # One vote per firm-form-quarter; multiple original filings are averaged.
    cells = meta.groupby(["cik", "form", "quarter", "time", "season"], as_index=False)[MEASURES].mean()
    cells["firm_form"] = cells.cik + "_" + cells.form
    quarterly = cells.groupby(["form", "quarter", "time", "season"], as_index=False)[MEASURES].mean()
    quarterly["n_firms"] = cells.groupby(["form", "quarter", "time", "season"]).size().values
    trend_rows = []
    for form, group in quarterly.groupby("form"):
        group = group.sort_values("time")
        if len(group) != 20:
            raise ValueError(f"Aggregate {form} trend lacks one of the 20 required quarters")
        for measure in MEASURES:
            model = smf.ols(f"{measure} ~ time + C(season)", data=group)
            for covariance, result in [("OLS", model.fit()),
                                       ("Newey-West lag 4", model.fit(cov_type="HAC", cov_kwds={"maxlags": 4, "use_correction": True}, use_t=True))]:
                trend_rows.append(coefficient_row(result, "time", form=form, measure=measure,
                                                  specification="Aggregate + calendar-quarter seasonality", covariance=covariance))
    for label, group in [("Pooled", cells), *list(cells.groupby("form"))]:
        for measure in MEASURES:
            result = fit_panel(f"{measure} ~ time + C(firm_form) + C(season)", group)
            trend_rows.append(coefficient_row(result, "time", form=label, measure=measure,
                                              specification="Within firm-form + calendar-quarter seasonality", covariance="Firm and quarter clusters"))
    # Demeaning visualizes firm-form baseline composition; inference uses FE above.
    adjusted = cells.copy()
    for measure in MEASURES:
        adjusted[measure] = (cells[measure] - cells.groupby("firm_form")[measure].transform("mean")
                             + cells[measure].mean())
    adjusted = adjusted.groupby(["form", "quarter", "time"], as_index=False)[MEASURES].mean()
    vix = prices["^VIX"].groupby(prices.index.to_period("Q")).mean()
    vix = vix.reindex(pd.period_range("2021Q1", "2025Q4", freq="Q"))
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False})
    fig, axes = plt.subplots(2, 2, figsize=(13, 8.5), sharex=True)
    for ax, measure in zip(axes.flat, MEASURES):
        factor = 100 if measure.endswith("proportional") else 1
        for form, color in [("10-K", "#176b87"), ("10-Q", "#b65f21")]:
            raw = quarterly.loc[quarterly.form.eq(form)].sort_values("time")
            adj = adjusted.loc[adjusted.form.eq(form)].sort_values("time")
            ax.plot(raw.time, raw[measure] * factor, color=color, label=form + " raw", linewidth=1.7)
            ax.plot(adj.time, adj[measure] * factor, color=color, linestyle="--", label=form + " within baseline", linewidth=1.3)
        right = ax.twinx()
        right.plot(range(20), vix.values, color="#888888", alpha=.38, linewidth=1.5)
        right.set_ylabel("VIX", color="#777777")
        ax.set_title(measure.replace("_", " "))
        ax.set_ylabel("% tokens" if factor == 100 else "Summed equation (1) weight")
        ax.set_xticks([0, 4, 8, 12, 16, 19], ["2021Q1", "2022Q1", "2023Q1", "2024Q1", "2025Q1", "2025Q4"], rotation=25)
        ax.grid(axis="y", alpha=.2)
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, ncol=4, loc="lower center", frameon=False)
    fig.suptitle("Figure 1. Filing language by calendar quarter; grey line is VIX", fontsize=15)
    fig.tight_layout(rect=[0, .05, 1, .96])
    fig.savefig(RESULTS / "figure1.png", dpi=180)
    plt.close(fig)

    regression_rows, power_rows, full_rows = [], [], []
    controls = "log_size + log_turnover + log_words + pre_return + C(form) + C(quarter)"
    for form_label, group in [("Pooled", meta), *list(meta.groupby("form"))]:
        # Drop the redundant form effect in single-form regressions.
        rhs_controls = controls if form_label == "Pooled" else controls.replace(" + C(form)", "")
        for weight in ["proportional", "tfidf"]:
            uncertainty = "Uncertainty_" + weight + "_z"
            negativity = "Negative_" + weight + "_z"
            for pre_control in [False, True]:
                formula = f"log_post_vol ~ {uncertainty} + {rhs_controls}" + (" + log_pre_vol" if pre_control else "")
                result = fit_panel(formula, group)
                labels = dict(table="Table 5", form=form_label, weighting=weight,
                              pre_vol_control=pre_control, covariance="Firm and quarter clusters", formula=formula)
                regression_rows.append(coefficient_row(result, uncertainty, **labels))
                for term in result.params.index:
                    full_rows.append(coefficient_row(result, term, **labels))
            formula = f"filing_return ~ {negativity} + log_pre_vol + {rhs_controls}"
            result = fit_panel(formula, group)
            labels = dict(table="Table 6", form=form_label, weighting=weight,
                          pre_vol_control=True, covariance="Firm and quarter clusters", formula=formula)
            regression_rows.append(coefficient_row(result, negativity, **labels))
            for term in result.params.index:
                full_rows.append(coefficient_row(result, term, **labels))
            cluster_df = min(group.cik.nunique(), group.quarter.nunique()) - 1
            critical = t.ppf(.975, cluster_df)
            se = float(result.bse[negativity])
            power_rows.append({"form": form_label, "weighting": weight, "n": len(group),
                               "firms": group.cik.nunique(), "quarters": group.quarter.nunique(),
                               "cluster_df": cluster_df, "cluster_se": se,
                               "mde_80pct": (critical + norm.ppf(.8)) * se,
                               "interpretation": "Approximate 80% power, two-sided 5%, return effect per common-sample 1 SD tone"})
    return {"table2_summary": summary, "table2_correlations": pd.DataFrame(corr_rows),
            "table4_trends": pd.DataFrame(trend_rows), "regressions": pd.DataFrame(regression_rows),
            "table6_power": pd.DataFrame(power_rows), "regression_all_terms": pd.DataFrame(full_rows),
            "quarterly_means": quarterly, "quarterly_within_baseline": adjusted}


def run():
    RESULTS.mkdir(exist_ok=True)
    meta, waterfall, words, excluded, audit, prices = prepare_sample()
    # Filing-level data stay local and are ignored by Git.
    meta.to_csv(INTERIM_DIR / "analysis_sample.csv", index=False)
    excluded.to_csv(INTERIM_DIR / "analysis_exclusions.csv", index=False)
    tables = make_exhibits(meta, prices)
    from .company_comparison import company_tables
    tables.update(company_tables(meta))
    tables["table1_waterfall"] = waterfall
    resolution = pd.read_csv(UNIVERSE_DIR / "holding_resolution.csv", dtype={"cik": str}).fillna("")
    tables["table1_holdings"] = resolution
    tables["table1_excluded_holdings"] = resolution.loc[resolution.status.ne("domestic_filer")]
    tables["table3_words"] = words
    tables["table5_volatility"] = tables["regressions"].query("table == 'Table 5'")
    tables["table6_returns"] = tables["regressions"].query("table == 'Table 6'")
    for name, table in tables.items():
        table.to_csv(RESULTS / f"{name}.csv", index=False)
    (RESULTS / "audit.json").write_text(json.dumps(audit, indent=2), encoding="utf-8")
    print(json.dumps(audit, indent=2))
    return tables, audit
