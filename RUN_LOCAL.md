# Local reproduction and submission

## Environment

From this repository directory:

```powershell
conda env create -f environment.yml
conda activate fre7871-assignment1
$env:SEC_USER_AGENT = "Jonas Wu jw9452@nyu.edu"
```

The environment already exists on the machine used for this assignment at
`D:\Miniconda\envs\fre7871-assignment1`. Activate it rather than recreate it.
If conda is not on PATH, use `D:\Miniconda\Scripts\conda.exe run -n fre7871-assignment1`
before each Python command. Run everything from `D:\Code Folder\7871\assignment1`.
`requirements-lock-windows.txt` records exact installed package versions for this
Windows run; use it with pip when an exact package recreation is needed.

## Pipeline

```powershell
python scripts/00_get_lexicons.py
python scripts/01_build_universe.py
python scripts/02_download_filings.py --limit 3
python scripts/02_download_filings.py
python scripts/03_get_market_data.py
python -m pytest -q
python scripts/05_build_notebook.py
python scripts/06_build_report.py
python scripts/07_package_submission.py
```

The executed notebook runs the analysis, so a separate `04_analyze.py` run is
optional. Use it for rebuilding just the exhibit files. Do not run the limited
filing download after the full run: the starter script overwrites its metadata
CSV with the selected subset, although extracted text remains cached.

Step 01 uses the reviewed identity configuration in `src/issuer_map.py`. It
preserves the original ticker, security identifier and company name. It does
not refresh holdings or guess CIKs for new securities. A different snapshot
requires a new identity review. For this machine's complete cached download,
`python scripts/01_build_universe.py --from-local-filings` checks coverage and
rebuilds the corrected universe without another network download.

Step 07 validates the notebook, report and exhibit inventory, then packages
the current files. It writes `submission/validation.json` and a file manifest.
It does not publish to GitHub or upload to Brightspace.

## File locations

- `Assignment1.ipynb`: executed notebook with saved tables and figure.
- `submission/Assignment1_Report.pdf`: Brightspace report.
- `REPORT.md`: report text with table HTML, generated from the same results.
- `results/`: aggregate exhibit CSVs, full coefficient outputs, Figure 1 and audit.
- `src/` and `scripts/`: calculation and reproduction code.
- `tests/`: synthetic checks of formulas, calendar edges, shares and exhibits.
- `data/`: local downloaded data and filing-level analysis/exclusion tables.
- `AI_USE.md`: actual assistance disclosure; read and update personal-review
  statements only after performing that review.

## Submission

The brief requires a viewable personal GitHub repository with the executed
notebook, code and AI disclosure; upload the PDF and repository URL to
Brightspace. The cloned origin is the instructor's source repository, not a
student-owned submission destination. Publishing or uploading has not been done
by these scripts.

Do not add downloaded data or the environment to Git. The original frozen
holdings input remains part of the starter repository. Aggregated exhibits are
results, not a redistributed filing or price dataset. Keep the accession-level
analysis files only under the ignored `data/` directory.

The supplied brief says the deadline is 09:00 on Saturday 12 September 2026;
check the course page for the applicable timezone and any revisions.
