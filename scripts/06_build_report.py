"""Build the report from the current exhibits; all numerical prose uses results."""
from pathlib import Path
import json
from html import escape
import numpy as np
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT/'results'
OUT = ROOT/'submission'
SHORT = {'Negative_proportional':'Neg-P','Negative_tfidf':'Neg-T',
         'Uncertainty_proportional':'Unc-P','Uncertainty_tfidf':'Unc-T'}


def main():
    OUT.mkdir(exist_ok=True)
    audit=json.loads((RESULTS/'audit.json').read_text())
    get=lambda name: pd.read_csv(RESULTS/f'{name}.csv')
    summary=get('table2_summary'); words=get('table3_words'); trends=get('table4_trends')
    vol=get('table5_volatility'); ret=get('table6_returns'); power=get('table6_power')
    holdings=pd.read_csv(RESULTS/'table1_holdings.csv', dtype={'cik': str}).fillna('')
    waterfall=get('table1_waterfall')
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='BodySmall',fontName='Times-Roman',fontSize=10.5,leading=13,spaceAfter=8,alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='CellSmall',fontName='Times-Roman',fontSize=8,leading=9))
    styles.add(ParagraphStyle(name='CellHeader',parent=styles['CellSmall'],fontName='Times-Bold'))
    styles.add(ParagraphStyle(name='TitleSmall',fontName='Times-Bold',fontSize=16,leading=20,spaceAfter=12,alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Author',fontName='Times-Roman',fontSize=11,leading=14,spaceAfter=16,alignment=TA_CENTER))
    for name, size in [('Heading1', 13), ('Heading2', 11)]:
        styles[name].fontName='Times-Bold'
        styles[name].fontSize=size
        styles[name].leading=size+3
        styles[name].textColor=colors.black
        styles[name].spaceBefore=10
        styles[name].spaceAfter=8
    story=[]; markdown=[]
    def heading(text,level=1):
        story.append(Paragraph(escape(text),styles['Heading1' if level==1 else 'Heading2']))
        markdown.append('#'*(level+1)+' '+text)
    def paragraph(text):
        story.append(Paragraph(escape(text),styles['BodySmall'])); markdown.append(text)
    def table(frame,widths):
        rows=[[Paragraph(escape(str(c)),styles['CellHeader']) for c in frame.columns]]
        for row in frame.itertuples(index=False,name=None):
            cells=[]
            for value in row:
                text=(f'{value:.4g}' if np.isfinite(value) else 'undefined') if isinstance(value,(float,np.floating)) else str(value)
                cells.append(Paragraph(escape(text),styles['CellSmall']))
            rows.append(cells)
        t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('LINEABOVE',(0,0),(-1,0),.6,colors.black),
            ('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.4,colors.black),
            ('LINEBELOW',(0,-1),(-1,-1),.6,colors.black),
            ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
            ('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5)]))
        story.extend([t,Spacer(1,7)]); markdown.append(frame.to_html(index=False,float_format=lambda x:f'{x:.5g}'))
    def page(): story.append(PageBreak())
    def mean(form,measure): return summary.loc[(summary.form==form)&(summary.measure==measure),'mean'].iloc[0]
    def row(frame,form,weight): return frame.loc[(frame.form==form)&(frame.weighting==weight)].iloc[0]

    story.append(Paragraph("Uncertainty and sentiment in ARK portfolio firms' SEC filings",styles['TitleSmall']))
    author='Jonas Wu (jw9452) | FRE-GY 7871 A | Assignment 1 | September 2026'
    story.append(Paragraph(escape(author),styles['Author'])); markdown.append(author)
    heading('1. Sample and research question')
    paragraph(f"I examine negative language and uncertainty in {audit['final_filings']:,} SEC filings from {audit['final_firms']} firms. "
        f"The sample includes {audit['forms']['10-K']} annual reports and {audit['forms']['10-Q']} quarterly reports filed in 2021-2025. "
        'I test changes in language within firms, the association between uncertainty and subsequent volatility, and the association between negative tone and four-day filing returns.')
    paragraph(f"I start with all {audit['snapshot_positions']} positions in the six-fund snapshot, covering {audit['snapshot_securities']} distinct security records. "
        'I match the original ticker, security identifier and issuer name to reviewed SEC identities. '
        'Airbus (AIR) remains separate from AAR; Discovery (DSY) remains separate from Dassault Systemes (DSY FP). '
        'Neither foreign DSY holding maps to the US-listed Big Tree Cloud. The appendix lists each excluded security.')
    statuses=audit['holding_status_counts']
    stage=pd.DataFrame([['Fund holdings',statuses.get('fund_holding',0)],
        ['No verified SEC issuer match',statuses.get('no_verified_sec_match',0)],
        ['Verified issuer, no 2021-2025 10-K/10-Q',statuses.get('no_10x_filings',0)],
        ['Eligible listings',audit['domestic_filers']]],columns=['Holding disposition','Securities'])
    heading('Table 1. Holding reconciliation and filing filters',2)
    table(stage,[405,90])
    paragraph(f"The {audit['domestic_filers']} eligible listings represent {audit['eligible_unique_ciks']} issuers; GOOG and GOOGL share a CIK. "
        'The filing waterfall counts listing records before accession deduplication. I report missing prices before the USD 3 screen.')
    table(waterfall.rename(columns={'stage':'Retained condition','remaining':'Remaining','removed':'Removed'}),[365,65,65])
    paragraph('The 2,000-token and USD 3 thresholds are research choices. I require a common complete-case sample so the paired regressions use the same observations and the same IDF corpus.')
    page()

    heading('2. Language measures')
    paragraph(f"I use the Loughran-McDonald financial dictionary: {audit['negative_words']:,} negative words and {audit['uncertainty_words']} uncertainty words, "
        f"with {audit['lexicon_overlap']} in both lists. Negative tone describes adverse outcomes; uncertainty describes qualifications and indeterminacy. "
        'A financial dictionary avoids the broad negative labels that general-purpose lists assign to ordinary accounting language.')
    heading('Table 2. Summary statistics by report type',2)
    s=summary.copy(); s['measure']=s.measure.map(SHORT)
    table(s[['form','measure','count','mean','std','25%','50%','75%']],[43,45,40,73,73,73,73,73])
    paragraph('P denotes the fraction of tokens in the category; T denotes the summed tf.idf weight. Neg is negative language and Unc is uncertainty. The notebook includes minima, maxima and the correlation matrix.')
    corr=get('table2_correlations')
    corr=corr[(corr.measure_a=='Negative_proportional')&(corr.measure_b=='Uncertainty_proportional')]
    paragraph('The negative/uncertainty proportion correlation is '+ '; '.join(f'{r.correlation:.3f} for {r.form}' for r in corr.itertuples())+'.')
    heading('Table 3. Thirty most frequent words in each list',2)
    neg=words.query("category == 'Negative'")[['rank','word','share_pct']].reset_index(drop=True)
    unc=words.query("category == 'Uncertainty'")[['word','share_pct']].reset_index(drop=True)
    top=pd.concat([neg,unc],axis=1); top.columns=['Rank','Negative word','% of Neg','Uncertainty word','% of Unc']
    table(top,[34,165,65,165,66])
    totals=words.groupby('category').share_pct.sum()
    may=words.loc[(words.category=='Uncertainty')&(words.word=='MAY'),'share_pct'].iloc[0]
    paragraph(f"The top 30 words account for {totals['Negative']:.2f}% of negative occurrences and {totals['Uncertainty']:.2f}% of uncertainty occurrences. "
        f"MAY alone accounts for {may:.2f}% of uncertainty words. I use all category occurrences as the denominator. Common hedges dominate the proportions, which motivates the tf.idf comparison.")
    page()

    heading('3. Measurement and quarterly composition')
    paragraph('I retain the starter parser: it removes inline-XBRL elements, hidden content and tables with digits exceeding 15% of non-space characters. '
        'It produces uppercase tokens of at least two letters, allowing internal apostrophes and hyphens. I analyse the resulting whole-document text. '
        'The parser can remove narrative inside XBRL tags and leave boilerplate; the scores inherit these measurement limits.')
    paragraph('Proportional tone is category word occurrences divided by total tokens. For each observed term, equation (1) of Loughran and McDonald gives '
        '[(1 + ln tf)/(1 + ln a)] ln(N/df), where a is total tokens divided by distinct observed tokens in that filing. '
        'I sum these weights within each category. N and df use the final regression corpus. This full-sample construction contains future corpus information, so I interpret the tests as retrospective associations.')
    heading('Figure 1. Quarterly language and VIX',2)
    story.append(Image(str(RESULTS/'figure1.png'),width=495,height=495*8.5/13))
    markdown.append('![Figure 1](results/figure1.png)')
    cells=len(get('quarterly_means')); n_cells=int(trends.loc[(trends.form=='Pooled')&trends.specification.str.startswith('Within'),'n'].iloc[0])
    paragraph(f"I average multiple filings within each firm-form-quarter, giving {n_cells:,} cells from {audit['final_filings']:,} filings, and then give each cell equal weight. "
        'Solid lines separate 10-Ks and 10-Qs. For the dashed lines I subtract each firm-form mean and add the pooled mean; these lines describe baseline composition in an unbalanced panel. '
        'I use fixed effects in Table 4 for the trend test. The grey right-axis series is the quarterly mean VIX.')
    paragraph('Annual reports cluster in particular quarters and contain more risk discussion. Firms also differ in their baseline language. '
        'I therefore separate report types and include quarter-of-year controls in both aggregate and within-firm trends. I use VIX as context; the overlay alone cannot establish a predictive relation.')
    page()

    heading('4. Trends within firms')
    primary=trends[(trends.form=='Pooled')&trends.specification.str.startswith('Within')]
    for r in primary.itertuples():
        paragraph(f"{SHORT[r.measure]}: the within-firm-form slope is {r.coefficient:.4g} per quarter "
            f"(95% CI [{r.ci_low:.4g}, {r.ci_high:.4g}]; clustered p={r.p:.3g}).")
    paragraph('I find the clearest pooled trend in weighted uncertainty. The form-specific estimates distinguish rising proportional negativity and uncertainty in 10-Ks from declining uncertainty in 10-Qs. '
        'Aggregate 10-Q negativity crosses the 5% threshold under OLS and Newey-West, whereas the within-firm estimate does not. I therefore avoid reading the aggregate decline as a change shared by firms.')
    heading('Table 4. Aggregate and within-firm trend tests',2)
    v=trends.copy(); v['measure']=v.measure.map(SHORT)
    v['Estimator']=v.covariance.map({'OLS':'Aggregate OLS','Newey-West lag 4':'Aggregate NW(4)','Firm and quarter clusters':'Within, 2-way'})
    table(v[['form','measure','Estimator','coefficient','t','p','n']],[42,45,113,80,75,75,65])
    paragraph('Aggregate regressions use 20 quarter means and quarter-of-year effects. Newey-West uses four lags with a finite-sample correction. '
        'Within regressions include firm-form and quarter-of-year effects; I cluster covariance by CIK and filing quarter and use t inference with the smaller cluster count minus one. '
        'In the 10-K sample, the Q3 indicator duplicates one firm effect. The least-squares fit identifies the time slope, but cannot separate those two nuisance effects. '
        'I report the full specification set without multiple-testing adjustments. Marginal p values warrant caution.')
    page()

    heading('5. Uncertainty and subsequent volatility')
    paragraph(f"Day 0 is the first NYSE session whose close follows SEC acceptance, using the actual close on early-close days. "
        f"This moves {audit['day0_moved_final']} retained filings relative to their filing date. "
        'I compute annualised sample standard deviations of adjusted daily returns over [-60,-6] and [1,63]: 55 pre-filing and 63 post-filing sessions. '
        'The post window approximates the following trading quarter and can overlap later filings.')
    paragraph('I regress log post-volatility on uncertainty, log size, log turnover, log token count, pre-filing excess return, form and filing-quarter effects. '
        'The paired specification adds log pre-volatility on the same rows. I standardise tone on the common sample. '
        'Size uses the same filing\'s cover-page shares and the previous-session price; I align historical price, volume and share units with observed split ratios.')
    heading('Table 5. Uncertainty coefficients with and without pre-volatility',2)
    table(vol[['form','weighting','pre_vol_control','coefficient','se','p','n']].rename(columns={'pre_vol_control':'Pre-vol?'}),[42,70,57,85,85,85,71])
    for weight in ['proportional','tfidf']:
        pair=vol[(vol.form=='Pooled')&(vol.weighting==weight)].sort_values('pre_vol_control')
        before,after=pair.iloc[0],pair.iloc[1]
        paragraph(f"For {weight} uncertainty, adding pre-volatility changes the coefficient from {before.coefficient:.4g} "
            f"(p={before.p:.3g}) to {after.coefficient:.4g} (p={after.p:.3g}), a reduction of {100*(1-after.coefficient/before.coefficient):.1f}%. "
            f"The controlled 95% interval is [{after.ci_low:.4g}, {after.ci_high:.4g}].")
    paragraph('The attenuation is the central result: earlier volatility accounts for much of the raw uncertainty association. '
        'The proportional measure retains an incremental association at 5%; the weighted measure has a wider interval that includes zero. These observational regressions do not establish causation.')
    heading('6. Precision of the four-day return test')
    p=power[['form','weighting','n','cluster_se','mde_80pct']].copy(); p[['cluster_se','mde_80pct']]*=100
    p.columns=['Form','Weight','N','SE, return pp','80% MDE, pp']
    table(p,[55,90,65,140,145])
    paragraph('The approximate two-sided 5%, 80%-power minimum detectable effect is (t critical + 0.842) times the clustered SE, per one-SD tone change. '
        'I express it in return percentage points. This sensitivity calculation uses estimated noise; it leaves smaller effects unresolved.')
    page()

    heading('Table 6. Negative tone and four-day excess returns')
    table(ret[['form','weighting','coefficient','se','p','ci_low','ci_high']],[43,72,76,76,76,76,76])
    paragraph('I subtract the compounded SPY return from the compounded stock return over [0,3]. Coefficients are return fractions per one-SD negative tone. '
        'Controls match Table 5 with log pre-volatility included. For intraday filings, close-to-close returns include some price movement before publication, which limits a trading interpretation.')
    for r in ret.loc[ret.form.eq('Pooled')].itertuples():
        paragraph(f"The pooled {r.weighting} coefficient is {100*r.coefficient:.3f} return percentage points "
            f"(95% CI [{100*r.ci_low:.3f}, {100*r.ci_high:.3f}]; p={r.p:.3g}).")
    rq=row(ret,'10-Q','proportional')
    paragraph(f"The 10-Q proportional estimate has p={rq.p:.4f}. Its interval includes zero at 5%, and I do not count it as evidence of predictive returns. "
        'The broad pooled intervals remain compatible with small negative effects. I regard the return test as inconclusive; that judgment does not imply that the trend and volatility tests lack power.')
    heading('7. Interpretation and limitations')
    paragraph(f"Mean negative and uncertainty fractions are {100*mean('10-K','Negative_proportional'):.2f}% and {100*mean('10-K','Uncertainty_proportional'):.2f}% for 10-Ks, "
        f"versus {100*mean('10-Q','Negative_proportional'):.2f}% and {100*mean('10-Q','Uncertainty_proportional'):.2f}% for 10-Qs. "
        'Different report scopes and repetition offer plausible explanations for these gaps. A difference between significance labels would require a formal interaction test before I could interpret it as a difference between slopes.')
    paragraph(f"The complete-case filters retain {audit['final_filings']:,} of {audit['eligible_filings']:,} filing-listing records from {audit['final_firms']} firms. "
        'The frozen holdings mix dates labelled 01/02/2026 and 09/04/2026. They omit companies ARK sold before those dates. '
        'I cannot measure that survivorship effect from this snapshot. The share-count requirement also removes firms with missing or ambiguous flat-API facts, including multi-class issuers.')
    full=get('regression_all_terms'); undefined=int(full.se.isna().sum())
    paragraph(f"SPY proxies for the broad market, and cover-page shares may predate the price used for size. Twenty quarters limit inference about common shocks. "
        f"Two-way covariance produces undefined standard errors for {undefined} of {len(full)} control or fixed-effect entries; I leave those entries undefined and do not interpret them. "
        'The reported tone and trend standard errors are finite. The parser, sample selection and retrospective IDF remain sources of uncertainty.')
    paragraph('I place the most weight on the within-firm decline in weighted uncertainty and the attenuation of the volatility coefficient after controlling for pre-volatility. '
        'Historical holdings including exits and a chronological holdout with training-only IDF would help test whether these associations generalise.')
    heading('Sources and reproduction',2)
    paragraph('Loughran, T. and B. McDonald (2011), When Is a Liability Not a Liability?, Journal of Finance 66, 35-65, doi:10.1111/j.1540-6261.2010.01625.x. '
        'Inputs: SEC EDGAR, the instructor\'s frozen ARK holdings and LM dictionary, and Yahoo Finance through yfinance. '
        'The repository contains the executed notebook, scripts, identity configuration, results, environment instructions and AI_USE.md. Supply the personal repository URL with the Brightspace PDF.')
    page()

    excluded=holdings.loc[holdings.status.ne('domestic_filer')].copy()
    def reason(r):
        if r.status=='fund_holding': return 'Fund security'
        if r.status=='no_verified_sec_match': return 'Foreign listing; no verified SEC issuer match'
        forms=set(str(r.observed_forms).split(', '))
        periodic=sorted(forms & {'20-F','40-F','6-K'})
        return 'No 10-K/10-Q; '+('/'.join(periodic) if periodic else 'other forms or no filings in 2021-2025')
    excluded['Reason']=[reason(r) for r in excluded.itertuples()]
    for start in range(0,len(excluded),19):
        heading('Appendix to Table 1. Excluded holdings'+(' (continued)' if start else ''))
        paragraph('One row per original security. A blank CIK means that I did not verify a SEC issuer match. '
            'For matched issuers I checked 2021-2025 form counts in SEC submissions. The notebook and src/issuer_map.py provide identity evidence links. '
            'Discovery, LY Corporation and JD Logistics remain explicit matching exclusions; I do not substitute a similarly named US company or a parent.')
        e=excluded.iloc[start:start+19][['raw_ticker','ark_name','cik','Reason']].copy()
        e.columns=['Original code','Holding issuer','CIK','Reason']
        table(e,[55,170,65,205])
        if start+19<len(excluded): page()
    def footer(canvas,doc):
        canvas.setFont('Times-Roman',10); canvas.setFillColor(colors.black)
        canvas.drawCentredString(A4[0]/2,25,str(doc.page))
    path=OUT/'Assignment1_Report.pdf'
    SimpleDocTemplate(str(path),pagesize=A4,rightMargin=50,leftMargin=50,topMargin=50,bottomMargin=50,
        title='Assignment 1 - Jonas Wu',author='Jonas Wu').build(story,onFirstPage=footer,onLaterPages=footer)
    (ROOT/'REPORT.md').write_text('# Assignment 1 report\n\n'+'\n\n'.join(markdown)+'\n',encoding='utf-8')
    print(path)


if __name__=='__main__':
    main()
