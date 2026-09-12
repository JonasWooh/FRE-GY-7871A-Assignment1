"""Create and execute the submission notebook, preserving all seven exhibits."""
from pathlib import Path
import sys

import nbformat as nbf
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main():
    nb = nbf.v4.new_notebook()
    md, code = nbf.v4.new_markdown_cell, nbf.v4.new_code_cell
    nb.cells = [
        md("# Assignment 1: Uncertainty and Sentiment in SEC Filings\n\nJonas Wu | NetID: jw9452\n\n"
           "FRE-GY 7871 A, Fall 2026. This notebook reconstructs all seven required exhibits. "
           "Read `METHODS.md` for definitions and `AI_USE.md` for assistance disclosure. "
           "Download data with scripts 00–03 first; data are intentionally excluded from submission."),
        md("## Method and execution\n\nBoth Negative and Uncertainty are scored as token fractions and as sums of "
           "Loughran–McDonald (2011), equation (1): `(1+ln(tf))/(1+ln(total/distinct))*ln(N/df)`. "
           "N and df use the common final regression corpus. This retrospective IDF is not an out-of-sample predictor. "
           "Day 0 is the first NYSE session closing after acceptance, with actual early closes. "
           "Four-day excess return is the difference of compounded stock and SPY returns on [0,3]. "
           "Annualised realised volatility uses [-60,-6] and [1,63]. Complete windows are required. "
           "Aggregate trends include calendar-quarter seasonality and HAC(4); panel inference clusters by firm and filing quarter. "
           "The two-way covariance estimate is used as computed, without replacing negative diagonal entries."),
        code("from pathlib import Path\nimport json\nimport pandas as pd\nfrom IPython.display import display, HTML, Image\n"
             "from src.analysis import run, RESULTS\n"
             "tables, audit = run()\n"
             "def show(name, digits=5):\n    display(HTML(tables[name].to_html(index=False, float_format=lambda x: f'{x:.{digits}g}')))\n"
             "display(audit)"),
        md("## Table 1. Sample construction\n\nI retain the snapshot's original security codes and identifiers when "
           "matching issuers. Airbus and AAR share the ticker AIR in different markets. Discovery's DSY and "
           "Dassault's DSY FP also require separate records. The holding audit lists each excluded security and "
           "its evidence. I count missing prices before applying the USD 3 threshold. The word-count and market "
           "filters are research choices; the filing waterfall reports them in the order applied."),
        code("display(tables['table1_holdings'].groupby('status').size().rename('securities'))\n"
             "show('table1_excluded_holdings')\nshow('table1_waterfall')"),
        md("## Table 2. Summary statistics, by form\n\nProportional scores are fractions; tf.idf scores are summed weights. "
           "The correlation matrix shows both category overlap and agreement between weighting schemes."),
        code("show('table2_summary')\nshow('table2_correlations')"),
        md("## Table 3. The thirty most frequent words in each list\n\nThe denominator is all occurrences in that "
           "category, not only its top thirty words. Ties are ordered alphabetically."),
        code("show('table3_words')"),
        md("## Figure 1. Quarterly measures and VIX\n\nEach firm-form-quarter receives one vote. Solid lines split "
           "forms. Dashed lines remove firm-form baseline means and add the common mean; they illustrate composition "
           "but are not balanced-panel estimates. The within-firm fixed-effect regressions below provide the primary trend test."),
        code("display(Image(filename=str(RESULTS / 'figure1.png')))"),
        md("## Table 4. Aggregate and within-firm trends\n\nQuarterly time runs from 0 to 19. Aggregate estimates "
           "control for season-of-year and compare conventional OLS with Newey–West lag 4. Panel estimates include "
           "firm-form fixed effects and seasonality; covariance clusters on firm and filing quarter. "
           "Twenty quarters limit aggregate inference even when there are many filings."),
        code("show('table4_trends')"),
        md("## Table 5. Uncertainty and subsequent-quarter volatility\n\nDependent variable: log annualised post-filing "
           "volatility. Tone regressors are standardised once on the common sample. Both versions use identical "
           "observations and controls: log size, log pre-filing turnover, log word count, pre-filing excess return, "
           "form and quarter effects. Compare the uncertainty coefficient before and after adding log pre-volatility. "
           "The relationship is conditional association, not causal evidence."),
        code("show('table5_volatility')"),
        md("## Table 6. Sentiment and four-day filing excess return\n\nPower first: the approximate 80%-power "
           "minimum detectable effect is `(t_0.975, min(clusters)-1 + z_0.8) * clustered SE` for a one-SD "
           "tone change. This is a design-sensitivity calculation using estimated noise, not observed post-hoc power. "
           "The controls match Table 5 and include pre-volatility."),
        code("show('table6_power')\nshow('table6_returns')"),
        md("## Full regression coefficients and reproducibility\n\nAll specifications run are saved, including "
           "nuisance controls and fixed effects, in `results/regression_all_terms.csv`. No p-value-based model selection "
           "or covariance repairs are performed. ARKK excess return is constructed but is not an additional fitted test. "
           "`REPORT.md` and the PDF interpret the actual estimates. The common complete-case sample and exclusion "
           "identifiers are local under `data/interim/`. The GitHub submission includes no downloaded data."),
        code("import sys, importlib.metadata as metadata\nprint(sys.version)\n"
             "for package in ['pandas','numpy','statsmodels','pandas_market_calendars','yfinance']:\n"
             "    print(package, metadata.version(package))"),
    ]
    nb.metadata.kernelspec = {"display_name": "Python (fre7871-assignment1)", "language": "python", "name": "python3"}
    NotebookClient(nb, timeout=1800, kernel_name="python3", resources={"metadata": {"path": str(ROOT)}}).execute()
    path = ROOT / "Assignment1.ipynb"
    nbf.write(nb, path)
    print(f"Executed notebook saved to {path}")


if __name__ == "__main__":
    main()
