"""Validate the saved deliverables and package an explicit submission inventory."""
import hashlib
import argparse
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

import nbformat
import numpy as np
import pandas as pd
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'submission'
EXHIBITS = ['table1_waterfall', 'table1_holdings', 'table1_excluded_holdings',
            'table2_summary', 'table2_correlations', 'table3_words', 'table4_trends',
            'table5_volatility', 'table6_returns', 'table6_power', 'regressions',
            'regression_all_terms', 'quarterly_means', 'quarterly_within_baseline',
            'company_summary', 'company_top5']


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive-name', default='Assignment1_Submission.zip')
    args = parser.parse_args()
    require(Path(args.archive_name).name == args.archive_name and args.archive_name.endswith('.zip'),
            'Archive name must be a .zip filename')
    tables = {name: pd.read_csv(ROOT / f'results/{name}.csv', dtype={'cik': str})
              for name in EXHIBITS}
    audit = json.loads((ROOT / 'results/audit.json').read_text())
    waterfall = tables['table1_waterfall']
    require((waterfall.remaining.shift(1) - waterfall.remaining).iloc[1:].eq(
        waterfall.removed.iloc[1:]).all(), 'Filing waterfall does not reconcile')
    require(int(waterfall.remaining.iloc[-1]) == audit['final_filings'], 'Final sample mismatch')
    holdings = tables['table1_holdings']
    require(len(holdings) == audit['snapshot_securities'], 'Holding count mismatch')
    require(holdings.status.value_counts().to_dict() == audit['holding_status_counts'],
            'Holding dispositions mismatch')
    require(not holdings.cik.isin(['0000001750', '0001999297']).any(), 'Wrong issuer returned')
    excluded = tables['table1_excluded_holdings']
    require(len(excluded) == len(holdings) - audit['domestic_filers'], 'Excluded holding mismatch')
    for name in ['table4_trends', 'table5_volatility', 'table6_returns']:
        require(np.isfinite(tables[name][['coefficient', 'se', 'p']]).all().all(),
                f'Nonfinite focal estimate: {name}')
    require(tables['table3_words'].groupby('category').size().eq(30).all(), 'Missing top words')
    vol = tables['table5_volatility']
    require(vol.groupby(['form', 'weighting']).n.nunique().eq(1).all(), 'Paired sample mismatch')

    nb = nbformat.read(ROOT / 'Assignment1.ipynb', as_version=4)
    nbformat.validate(nb)
    cells = [cell for cell in nb.cells if cell.cell_type == 'code']
    require(bool(cells) and all(cell.execution_count is not None for cell in cells),
            'Notebook has unexecuted code')
    require(all(output.output_type != 'error' for cell in cells for output in cell.outputs),
            'Notebook contains errors')
    html = '\n'.join(output.get('data', {}).get('text/html', '')
                     for cell in cells for output in cell.outputs)
    for name in ['table1_waterfall', 'table1_excluded_holdings', 'table2_summary',
                 'table2_correlations', 'table3_words', 'table4_trends',
                 'table5_volatility', 'table6_returns', 'table6_power', 'company_top5']:
        frame = tables[name]
        if name == 'table1_excluded_holdings':
            frame = frame.fillna('')
        expected = frame.to_html(index=False, float_format=lambda x: f'{x:.5g}')
        require(expected in html, f'Notebook output differs from current {name}')

    pdf = PdfReader(OUT / 'Assignment1_Report.pdf')
    text = '\n'.join(page.extract_text() for page in pdf.pages)
    for label in [f'Table {i}.' for i in range(1, 7)] + ['Figure 1.']:
        require(label in text, f'Report missing {label}')
    require('Table 7.' in text, 'Report missing company comparison')
    for record in tables['company_top5'].itertuples():
        require(record.ticker in text, f'Report missing ranked ticker: {record.ticker}')
        displayed = f'{record.occurrences:,}' if record.form == 'All' else f'{record.mean_share_pct:.3f}'
        require(displayed in text, f'Report missing company statistic: {displayed}')
    require(f"{audit['final_filings']:,}" in text, 'Report sample is stale')
    appendix = text[text.index('Appendix to Table 1.'):]
    require(all(cik in appendix for cik in excluded.cik.dropna()), 'Report loses CIK precision')

    files = [ROOT / name for name in ['.gitignore', '.gitattributes', 'README.md', 'REPORT.md', 'METHODS.md',
             'RUN_LOCAL.md', 'AI_USE.md', 'requirements.txt', 'requirements-lock-windows.txt',
             'environment.yml', 'Assignment1.ipynb', 'data/universe/ark_holdings_raw.csv',
             'submission/Assignment1_Report.pdf']]
    for folder in ['src', 'scripts', 'tests']:
        files.extend(sorted((ROOT / folder).glob('*.py')))
    files.extend(ROOT / f'results/{name}.csv' for name in EXHIBITS)
    files.extend([ROOT / 'results/audit.json', ROOT / 'results/figure1.png'])
    require(all(path.is_file() for path in files), 'Required submission file is missing')
    validation = {'status': 'passed', 'final_filings': audit['final_filings'],
                  'final_firms': audit['final_firms'], 'notebook_executed_cells': len(cells),
                  'notebook_tables_match_csv': True, 'pdf_pages': len(pdf.pages),
                  'pdf_exhibits_present': True, 'pdf_ciks_exact': True,
                  'downloaded_filing_and_price_data_included': False,
                  'instructor_frozen_holdings_included': True,
                  'scope': 'Inventory and saved-output consistency; run pytest and inspect rendered PDF separately.'}
    (OUT / 'validation.json').write_text(json.dumps(validation, indent=2) + '\n', encoding='utf-8')
    files.append(OUT / 'validation.json')
    manifest = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sorted(files)}
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    files.append(OUT / 'manifest.json')
    archive = OUT / args.archive_name
    with ZipFile(archive, 'w', ZIP_DEFLATED) as z:
        for path in sorted(files):
            z.write(path, 'assignment1/' + path.relative_to(ROOT).as_posix())
    with ZipFile(archive) as z:
        require(z.testzip() is None, 'Archive CRC check failed')
        for path in files:
            require(z.read('assignment1/' + path.relative_to(ROOT).as_posix()) == path.read_bytes(),
                    f'Archive bytes differ: {path.name}')
    print(json.dumps(validation, indent=2))
    print(f'Verified {len(files)} files: {archive}')


if __name__ == '__main__':
    main()
