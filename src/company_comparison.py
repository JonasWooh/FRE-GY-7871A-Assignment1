"""Descriptive issuer rankings on the unchanged complete-case corpus."""
from collections import Counter
import gzip

import numpy as np
import pandas as pd

from .config import ROOT
from .lexicons import load_all
from .parse import tokenize


def aggregate_companies(filings):
    """Keep form-specific intensity distinct from pooled occurrence volume."""
    if filings.accession.duplicated().any():
        raise ValueError('Company comparisons require unique accessions')
    rows = []
    for form, subset in [('All', filings), ('10-K', filings[filings.form.eq('10-K')]),
                         ('10-Q', filings[filings.form.eq('10-Q')])]:
        for cik, group in subset.groupby('cik', sort=True):
            for category in ['Negative', 'Uncertainty']:
                counts = group[category + '_count']
                rows.append(dict(cik=cik, ticker=group.ticker.iloc[0],
                    company=group.company.iloc[0], form=form, category=category,
                    filings=len(group), years=group.filing_date.dt.year.nunique(),
                    first_filing=group.filing_date.min().strftime('%Y-%m-%d'),
                    last_filing=group.filing_date.max().strftime('%Y-%m-%d'),
                    tokens=int(group.n_words.sum()), occurrences=int(counts.sum()),
                    mean_share_pct=float((100 * counts / group.n_words).mean()),
                    pooled_share_pct=float(100 * counts.sum() / group.n_words.sum())))
    summary = pd.DataFrame(rows)
    top = []
    for category in ['Negative', 'Uncertainty']:
        for form, metric in [('All', 'occurrences'), ('10-K', 'mean_share_pct'),
                             ('10-Q', 'mean_share_pct')]:
            ranked = summary.loc[summary.category.eq(category) & summary.form.eq(form)].copy()
            ranked['rank'] = ranked[metric].rank(method='min', ascending=False).astype(int)
            ranked = ranked.loc[ranked['rank'].le(5)].sort_values(['rank', 'cik'])
            ranked['ranking_metric'] = metric
            top.append(ranked)
    return {'company_summary': summary, 'company_top5': pd.concat(top, ignore_index=True)}


def company_tables(sample):
    """Count dictionary occurrences in retained texts and verify stored proportions."""
    frame = sample.copy()
    lists = load_all()
    counts = {category: [] for category in ['Negative', 'Uncertainty']}
    for row in frame.itertuples():
        with gzip.open(ROOT / row.text_path, 'rt', encoding='utf-8') as stream:
            tokens = Counter(tokenize(stream.read()))
        if tokens.total() != row.n_words:
            raise ValueError(f'Token count mismatch: {row.accession}')
        for category in counts:
            counts[category].append(sum(tokens[word] for word in lists[category]))
    for category, values in counts.items():
        frame[category + '_count'] = values
        np.testing.assert_allclose(frame[category + '_count'] / frame.n_words,
                                   frame[category + '_proportional'], rtol=1e-10, atol=1e-12)
    frame['filing_date'] = pd.to_datetime(frame.filing_date)
    return aggregate_companies(frame)
