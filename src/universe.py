"""Resolve the supplied holdings by security identity, then enumerate SEC filings."""
import pandas as pd
from .issuer_map import ISSUERS


def resolve_holdings(raw):
    """Use reviewed (ticker, identifier, issuer name) keys, never ticker alone."""
    rows = []
    groups = raw.groupby(['ticker', 'cusip', 'company'], sort=True, dropna=False)
    for (ticker, identifier, company), group in groups:
        key = (ticker.strip(), identifier.strip(), company.strip())
        if key not in ISSUERS:
            raise ValueError(f'Unreviewed holding identity: {key!r}')
        entry = ISSUERS[key]
        rows.append(dict(raw_ticker=ticker, identifier=identifier, ark_name=company,
                         ticker=entry['ticker'], cik=entry['cik'],
                         sec_name=entry['sec_name'], resolution=entry['resolution'],
                         evidence=entry['evidence'], observed_forms=entry['observed_forms'],
                         funds='|'.join(sorted(set(group.fund)))))
    return pd.DataFrame(rows)


def enumerate_universe(holdings, filings_for_cik):
    """Return the security audit and eligible universe from one enumeration."""
    counts = {}
    for cik in holdings.loc[holdings.resolution.eq('verified'), 'cik'].unique():
        filings = filings_for_cik(cik)
        counts[cik] = (int(filings.form.eq('10-K').sum()),
                       int(filings.form.eq('10-Q').sum()))
    audit = holdings.copy()
    audit['n_10k'] = [counts.get(c, (0, 0))[0] for c in audit.cik]
    audit['n_10q'] = [counts.get(c, (0, 0))[1] for c in audit.cik]
    audit['status'] = audit.resolution
    verified = audit.resolution.eq('verified')
    audit.loc[verified, 'status'] = 'no_10x_filings'
    audit.loc[verified & (audit.n_10k + audit.n_10q).gt(0), 'status'] = 'domestic_filer'
    eligible = audit.loc[audit.status.eq('domestic_filer')].copy()
    if eligible.ticker.duplicated().any():
        raise ValueError('Multiple eligible securities use the same price ticker')
    return audit, eligible.sort_values('ticker').reset_index(drop=True)
