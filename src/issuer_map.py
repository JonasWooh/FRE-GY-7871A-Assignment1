"""Reviewed identity configuration for the instructor's frozen holdings.

Keys preserve the original ticker, CUSIP/SEDOL field and company name. SEC names
and form coverage were checked against submissions metadata on 2026-09-12 UTC.
This map is research configuration; it contains no filing text or price history.
AIR refers to Airbus, DSY to Discovery, and DSY FP to Dassault Systemes.
A new snapshot requires identity review before adding entries. Do not infer CIKs
from bare tickers. Blank CIKs describe an exclusion, not an assertion of absence
from all SEC records. Filing counts are used only to verify cached downloads.
"""

ISSUERS = {('2618', 'BNMBPD9', 'JD LOGISTICS INC'): {'ticker': '2618',
                                           'cik': '',
                                           'sec_name': '',
                                           'resolution': 'no_verified_sec_match',
                                           'evidence': 'https://www.sec.gov/Archives/edgar/data/1549802/000119312521043418/d131620dex991.htm',
                                           'observed_forms': ''},
 ('4689', '6084848', 'LY CORP'): {'ticker': '4689',
                                  'cik': '',
                                  'sec_name': '',
                                  'resolution': 'no_verified_sec_match',
                                  'evidence': 'https://www2.jpx.co.jp/tseHpFront/StockSearch.do?callJorEFlg=1&topSearchStr=4689',
                                  'observed_forms': ''},
 ('6301', '6496584', 'KOMATSU LTD'): {'ticker': '6301',
                                      'cik': '0000056594',
                                      'sec_name': 'KOMATSU LTD',
                                      'resolution': 'verified',
                                      'evidence': 'https://data.sec.gov/submissions/CIK0000056594.json',
                                      'observed_forms': ''},
 ('ABNB', '009066101', 'AIRBNB INC-CLASS A'): {'ticker': 'ABNB',
                                               'cik': '0001559720',
                                               'sec_name': 'Airbnb, Inc.',
                                               'resolution': 'verified',
                                               'evidence': 'https://data.sec.gov/submissions/CIK0001559720.json',
                                               'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, 4/A, 424B7, '
                                                                 '5, 8-K, CORRESP, DEF 14A, DEFA14A, PRE '
                                                                 '14A, PX14A6G, S-3ASR, S-8, SC 13G, SC '
                                                                 '13G/A, SCHEDULE 13G/A, UPLOAD'},
 ('ABSI', '00091E109', 'ABSCI CORP'): {'ticker': 'ABSI',
                                       'cik': '0001672688',
                                       'sec_name': 'Absci Corp',
                                       'resolution': 'verified',
                                       'evidence': 'https://data.sec.gov/submissions/CIK0001672688.json',
                                       'observed_forms': '10-K, 10-K/A, 10-Q, 144, 3, 4, 4/A, 424B3, 424B4, '
                                                         '424B5, 5, 8-A12B, 8-K, 8-K/A, ARS, CERT, CORRESP, '
                                                         'D, D/A, DEF 14A, DEFA14A, DRS, DRS/A, DRSLTR, '
                                                         'EFFECT, PRE 14A, S-1, S-1/A, S-3, S-8, SC 13D, SC '
                                                         '13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE '
                                                         '13G, SCHEDULE 13G/A, SEC STAFF LETTER, UPLOAD'},
 ('ACHR', '03945R102', 'ARCHER AVIATION INC-A'): {'ticker': 'ACHR',
                                                  'cik': '0001824502',
                                                  'sec_name': 'Archer Aviation Inc.',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0001824502.json',
                                                  'observed_forms': '10-K, 10-K/A, 10-Q, 10-Q/A, 144, 144/A, '
                                                                    '25-NSE, 3, 3/A, 4, 4/A, 424B3, 424B5, '
                                                                    '424B7, 424B8, 425, 8-K, 8-K/A, ARS, '
                                                                    'CORRESP, DEF 14A, DEFA14A, EFFECT, NT '
                                                                    '10-Q, POS AM, PRE 14A, S-1, S-1/A, S-3, '
                                                                    'S-3ASR, S-4, S-4/A, S-8, SC 13D, SC '
                                                                    '13D/A, SC 13G, SC 13G/A, SCHEDULE '
                                                                    '13D/A, SCHEDULE 13G, SCHEDULE 13G/A, '
                                                                    'UPLOAD'},
 ('ADPT', '00650F109', 'ADAPTIVE BIOTECHNOLOGIES'): {'ticker': 'ADPT',
                                                     'cik': '0001478320',
                                                     'sec_name': 'Adaptive Biotechnologies Corp',
                                                     'resolution': 'verified',
                                                     'evidence': 'https://data.sec.gov/submissions/CIK0001478320.json',
                                                     'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, 4/A, '
                                                                       '8-K, ARS, DEF 14A, DEFA14A, S-8, SC '
                                                                       '13G, SC 13G/A, SCHEDULE 13G, '
                                                                       'SCHEDULE 13G/A'},
 ('ADYEN', 'BZ1HM42', 'ADYEN NV'): {'ticker': 'ADYEN',
                                    'cik': '0001788707',
                                    'sec_name': 'Adyen N.V./ADR',
                                    'resolution': 'verified',
                                    'evidence': 'https://data.sec.gov/submissions/CIK0001788707.json',
                                    'observed_forms': 'F-6 POS, F-6EF, SC 13G, SCHEDULE 13G/A'},
 ('AIR', '4012250', 'AIRBUS SE'): {'ticker': 'AIR',
                                   'cik': '0001697546',
                                   'sec_name': 'AIRBUS SE',
                                   'resolution': 'verified',
                                   'evidence': 'https://data.sec.gov/submissions/CIK0001697546.json',
                                   'observed_forms': 'D'},
 ('ALMR', '010911105', 'ALAMAR BIOSCIENCES INC'): {'ticker': 'ALMR',
                                                   'cik': '0002104204',
                                                   'sec_name': 'Alamar Biosciences, Inc.',
                                                   'resolution': 'verified',
                                                   'evidence': 'https://data.sec.gov/submissions/CIK0002104204.json',
                                                   'observed_forms': ''},
 ('AMD', '007903107', 'ADVANCED MICRO DEVICES'): {'ticker': 'AMD',
                                                  'cik': '0000002488',
                                                  'sec_name': 'ADVANCED MICRO DEVICES INC',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0000002488.json',
                                                  'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B3, '
                                                                    '424B5, 425, 5, 5/A, 8-K, 8-K/A, ARS, '
                                                                    'CORRESP, DEF 14A, DEFA14A, EFFECT, FWP, '
                                                                    'IRANNOTICE, POS EX, PRE 14A, S-3ASR, '
                                                                    'S-4/A, S-4MEF, S-8, SC 13G/A, SD, '
                                                                    'UPLOAD'},
 ('AMZN', '023135106', 'AMAZON.COM INC'): {'ticker': 'AMZN',
                                           'cik': '0001018724',
                                           'sec_name': 'AMAZON COM INC',
                                           'resolution': 'verified',
                                           'evidence': 'https://data.sec.gov/submissions/CIK0001018724.json',
                                           'observed_forms': '10-K, 10-Q, 13F-HR, 144, 144/A, 3, 3/A, 4, '
                                                             '424B2, 424B5, 8-K, ARS, CORRESP, DEF 14A, '
                                                             'DEFA14A, FWP, IRANNOTICE, N-PX, PRE 14A, '
                                                             'PX14A6G, S-3ASR, SC 13G, SC 13G/A, SCHEDULE '
                                                             '13G/A, SD, UPLOAD'},
 ('ARCT UQ', '03969T109', 'ARCTURUS THERAPEUTICS HOLDIN'): {'ticker': 'ARCT',
                                                            'cik': '0001768224',
                                                            'sec_name': 'Arcturus Therapeutics Holdings Inc.',
                                                            'resolution': 'verified',
                                                            'evidence': 'https://data.sec.gov/submissions/CIK0001768224.json',
                                                            'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, '
                                                                              '424B5, 8-K, 8-K/A, CORRESP, '
                                                                              'DEF 14A, DEFR14A, DEL AM, '
                                                                              'EFFECT, NT 10-Q, S-3, S-8, SC '
                                                                              '13D/A, SC 13G, SC 13G/A, '
                                                                              'SCHEDULE 13G, SCHEDULE 13G/A, '
                                                                              'UPLOAD'},
 ('ARKY', '00214Q724', 'ARK ACTIVE AUTOCALL INC ETF'): {'ticker': 'ARKY',
                                                        'cik': '',
                                                        'sec_name': '',
                                                        'resolution': 'fund_holding',
                                                        'evidence': 'Frozen holdings: fund security; outside '
                                                                    'operating-company sample',
                                                        'observed_forms': ''},
 ('AUR', '051774107', 'AURORA INNOVATION INC'): {'ticker': 'AUR',
                                                 'cik': '0001828108',
                                                 'sec_name': 'Aurora Innovation, Inc.',
                                                 'resolution': 'verified',
                                                 'evidence': 'https://data.sec.gov/submissions/CIK0001828108.json',
                                                 'observed_forms': '10-K, 10-K/A, 10-Q, 144, 25-NSE, 3, 4, '
                                                                   '4/A, 424B3, 424B4, 424B5, 425, 8-A12B, '
                                                                   '8-K, 8-K/A, ARS, CERT, CORRESP, DEF 14A, '
                                                                   'DEFA14A, EFFECT, POS AM, PRE 14A, S-1, '
                                                                   'S-1/A, S-3, S-3ASR, S-4, S-4/A, S-8, SC '
                                                                   '13D, SC 13D/A, SC 13G, SC 13G/A, '
                                                                   'SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE '
                                                                   '13G/A, UPLOAD'},
 ('AVAV', '008073108', 'AEROVIRONMENT INC'): {'ticker': 'AVAV',
                                              'cik': '0001368622',
                                              'sec_name': 'AeroVironment Inc',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001368622.json',
                                              'observed_forms': '10-K, 10-K/A, 10-Q, 144, 3, 4, 4/A, 424B3, '
                                                                '424B5, 425, 8-K, 8-K/A, ARS, CORRESP, D, '
                                                                'DEF 14A, DEFA14A, EFFECT, FWP, PRE 14A, '
                                                                'S-3ASR, S-4, S-4/A, S-8, SC 13G/A, SCHEDULE '
                                                                '13D, SCHEDULE 13G, SCHEDULE 13G/A, SD, '
                                                                'UPLOAD'},
 ('AVGO', '11135F101', 'BROADCOM INC'): {'ticker': 'AVGO',
                                         'cik': '0001730168',
                                         'sec_name': 'Broadcom Inc.',
                                         'resolution': 'verified',
                                         'evidence': 'https://data.sec.gov/submissions/CIK0001730168.json',
                                         'observed_forms': '10-K, 10-Q, 144, 144/A, 15-12B, 25-NSE, 3, 3/A, '
                                                           '4, 4/A, 424B2, 424B3, 424B5, 425, 5, 8-K, 8-K/A, '
                                                           'ARS, CORRESP, DEF 14A, DEFA14A, DEL AM, EFFECT, '
                                                           'FWP, S-3ASR, S-4, S-4/A, S-8, SC 13G/A, SCHEDULE '
                                                           '13G/A, SD, UPLOAD'},
 ('BABA', '01609W102', 'ALIBABA GROUP HOLDING-SP ADR'): {'ticker': 'BABA',
                                                         'cik': '0001577552',
                                                         'sec_name': 'Alibaba Group Holding Ltd',
                                                         'resolution': 'verified',
                                                         'evidence': 'https://data.sec.gov/submissions/CIK0001577552.json',
                                                         'observed_forms': '13F-HR, 144, 20-F, 20-F/A, '
                                                                           '424B2, 424B3, 424B5, 6-K, '
                                                                           'CORRESP, EFFECT, F-3ASR, F-4, '
                                                                           'F-6EF, FWP, IRANNOTICE, N-PX, '
                                                                           'S-8, SC 13D/A, SC 13G, SC 13G/A, '
                                                                           'SCHEDULE 13G/A, SD, UPLOAD'},
 ('BEAM', '07373V105', 'BEAM THERAPEUTICS INC'): {'ticker': 'BEAM',
                                                  'cik': '0001745999',
                                                  'sec_name': 'Beam Therapeutics Inc.',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0001745999.json',
                                                  'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B5, '
                                                                    '424B7, 8-K, ARS, CORRESP, DEF 14A, '
                                                                    'DEFA14A, FWP, S-3ASR, S-8, SC 13G, SC '
                                                                    '13G/A, SCHEDULE 13G/A, UPLOAD'},
 ('BFLY', '124155102', 'BUTTERFLY NETWORK INC'): {'ticker': 'BFLY',
                                                  'cik': '0001804176',
                                                  'sec_name': 'Butterfly Network, Inc.',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0001804176.json',
                                                  'observed_forms': '10-K, 10-K/A, 10-Q, 10-Q/A, 144, '
                                                                    '25-NSE, 3, 4, 4/A, 424B3, 424B5, 425, '
                                                                    '8-K, 8-K/A, ARS, CORRESP, DEF 14A, '
                                                                    'DEFA14A, EFFECT, POS AM, PRE 14A, S-1, '
                                                                    'S-1/A, S-3, S-3/A, S-4/A, S-8, SC 13D, '
                                                                    'SC 13D/A, SC 13G, SC 13G/A, SCHEDULE '
                                                                    '13D/A, SCHEDULE 13G, SCHEDULE 13G/A, '
                                                                    'SEC STAFF LETTER, UPLOAD'},
 ('BIDU', '056752108', 'BAIDU INC - SPON ADR'): {'ticker': 'BIDU',
                                                 'cik': '0001329099',
                                                 'sec_name': 'Baidu, Inc.',
                                                 'resolution': 'verified',
                                                 'evidence': 'https://data.sec.gov/submissions/CIK0001329099.json',
                                                 'observed_forms': '144, 144/A, 20-F, 424B2, 424B5, 6-K, '
                                                                   'CORRESP, F-3ASR, FWP, S-8, SC 13D/A, SC '
                                                                   '13G, SC 13G/A, SCHEDULE 13G/A, UPLOAD'},
 ('BLSH', 'G16910120', 'BULLISH'): {'ticker': 'BLSH',
                                    'cik': '0001872195',
                                    'sec_name': 'Bullish',
                                    'resolution': 'verified',
                                    'evidence': 'https://data.sec.gov/submissions/CIK0001872195.json',
                                    'observed_forms': '424B4, 425, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, '
                                                      'DRSLTR, EFFECT, F-1, F-1/A, F-4, F-4/A, RW, S-8, '
                                                      'SCHEDULE 13D, SCHEDULE 13G, UPLOAD'},
 ('BMNR', '09175A206', 'BITMINE IMMERSION TECHNOLOGI'): {'ticker': 'BMNR',
                                                         'cik': '0001829311',
                                                         'sec_name': 'BITMINE IMMERSION TECHNOLOGIES, INC.',
                                                         'resolution': 'verified',
                                                         'evidence': 'https://data.sec.gov/submissions/CIK0001829311.json',
                                                         'observed_forms': '10-K, 10-K/A, 10-Q, 10-Q/A, 144, '
                                                                           '144/A, 3, 4, 4/A, 424B4, 424B5, '
                                                                           '5, 8-A12B, 8-K, 8-K/A, ARS, '
                                                                           'CERT, CORRESP, D, D/A, DEF 14A, '
                                                                           'DEF 14C, DEFA14A, DEFR14A, '
                                                                           'EFFECT, NT 10-K, NT 10-Q, '
                                                                           'POSASR, PRE 14A, PRE 14C, RW, '
                                                                           'S-1, S-1/A, S-1MEF, S-3ASR, S-8, '
                                                                           'SC 13D, SCHEDULE 13D, SCHEDULE '
                                                                           '13G, SCHEDULE 13G/A, UPLOAD'},
 ('BWXT', '05605H100', 'BWX TECHNOLOGIES INC'): {'ticker': 'BWXT',
                                                 'cik': '0001486957',
                                                 'sec_name': 'BWX Technologies, Inc.',
                                                 'resolution': 'verified',
                                                 'evidence': 'https://data.sec.gov/submissions/CIK0001486957.json',
                                                 'observed_forms': '10-K, 10-K/A, 10-Q, 144, 3, 3/A, 4, 4/A, '
                                                                   '8-K, 8-K/A, ARS, DEF 14A, DEFA14A, PRE '
                                                                   '14A, SC 13G, SC 13G/A, SCHEDULE 13G/A, '
                                                                   'SD'},
 ('BYDDY', '05606L100', 'BYD CO LTD-UNSPONSORED ADR'): {'ticker': 'BYDDY',
                                                        'cik': '0001445162',
                                                        'sec_name': 'BYD CO LTD',
                                                        'resolution': 'verified',
                                                        'evidence': 'https://data.sec.gov/submissions/CIK0001445162.json',
                                                        'observed_forms': 'F-6 POS, F-6EF'},
 ('CAT', '149123101', 'CATERPILLAR INC'): {'ticker': 'CAT',
                                           'cik': '0000018230',
                                           'sec_name': 'CATERPILLAR INC',
                                           'resolution': 'verified',
                                           'evidence': 'https://data.sec.gov/submissions/CIK0000018230.json',
                                           'observed_forms': '10-K, 10-Q, 11-K, 144, 25-NSE, 3, 4, 4/A, '
                                                             '424B5, 8-K, ARS, CORRESP, DEF 14A, DEFA14A, '
                                                             'FWP, IRANNOTICE, PX14A6G, S-3ASR, S-8, S-8 '
                                                             'POS, SC 13G, SC 13G/A, SD, UPLOAD'},
 ('CBRS', '15675D103', 'CEREBRAS SYSTEMS INC - A'): {'ticker': 'CBRS',
                                                     'cik': '0002021728',
                                                     'sec_name': 'Cerebras Systems Inc.',
                                                     'resolution': 'verified',
                                                     'evidence': 'https://data.sec.gov/submissions/CIK0002021728.json',
                                                     'observed_forms': 'DRS, DRS/A, RW, S-1'},
 ('CCJ', '13321L108', 'CAMECO CORP'): {'ticker': 'CCJ',
                                       'cik': '0001009001',
                                       'sec_name': 'CAMECO CORP',
                                       'resolution': 'verified',
                                       'evidence': 'https://data.sec.gov/submissions/CIK0001009001.json',
                                       'observed_forms': '144, 144/A, 40-F, 6-K, CORRESP, F-10, F-X, FWP, '
                                                         'S-8, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE '
                                                         '13G/A, SD, SUPPL, UPLOAD'},
 ('CDNA', '14167L103', 'CAREDX INC'): {'ticker': 'CDNA',
                                       'cik': '0001217234',
                                       'sec_name': 'CareDx, Inc.',
                                       'resolution': 'verified',
                                       'evidence': 'https://data.sec.gov/submissions/CIK0001217234.json',
                                       'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B5, 8-K, ARS, CT '
                                                         'ORDER, DEF 14A, DEFA14A, EFFECT, POS AM, POSASR, '
                                                         'PRE 14A, S-3ASR, S-8, SC 13G, SC 13G/A, SCHEDULE '
                                                         '13G, SCHEDULE 13G/A'},
 ('CERS', '157085101', 'CERUS CORP'): {'ticker': 'CERS',
                                       'cik': '0001020214',
                                       'sec_name': 'CERUS CORP',
                                       'resolution': 'verified',
                                       'evidence': 'https://data.sec.gov/submissions/CIK0001020214.json',
                                       'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 8-K, ARS, CORRESP, DEF '
                                                         '14A, DEFA14A, EFFECT, POS AM, POSASR, PRE 14A, '
                                                         'S-3, S-8, SC 13G/A, SCHEDULE 13G/A, SD, UPLOAD'},
 ('CMPS', '20451W101', 'COMPASS PATHWAYS PLC'): {'ticker': 'CMPS',
                                                 'cik': '0001816590',
                                                 'sec_name': 'COMPASS Pathways plc',
                                                 'resolution': 'verified',
                                                 'evidence': 'https://data.sec.gov/submissions/CIK0001816590.json',
                                                 'observed_forms': '10-K, 10-Q, 144, 20-F, 3, 4, 4/A, 424B3, '
                                                                   '424B4, 424B5, 6-K, 8-K, ARS, CORRESP, '
                                                                   'DEF 14A, DRS, EFFECT, F-1, F-1/A, '
                                                                   'F-1MEF, F-3ASR, F-6EF, POS AM, POSASR, '
                                                                   'PRE 14A, S-3, S-8, SC 13D, SC 13D/A, SC '
                                                                   '13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE '
                                                                   '13G, SCHEDULE 13G/A, UPLOAD'},
 ('COIN', '19260Q107', 'COINBASE GLOBAL INC -CLASS A'): {'ticker': 'COIN',
                                                         'cik': '0001679788',
                                                         'sec_name': 'Coinbase Global, Inc.',
                                                         'resolution': 'verified',
                                                         'evidence': 'https://data.sec.gov/submissions/CIK0001679788.json',
                                                         'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 3/A, '
                                                                           '4, 4/A, 424B3, 424B4, 424B7, 5, '
                                                                           '8-A12B, 8-K, 8-K/A, ARS, CERT, '
                                                                           'CORRESP, DEF 14A, DEF 14C, '
                                                                           'DEFA14A, DRS/A, DRSLTR, EFFECT, '
                                                                           'FWP, POS AM, PRE 14C, S-1, '
                                                                           'S-1/A, S-3ASR, S-8, SC 13G, SC '
                                                                           '13G/A, SCHEDULE 13G, SCHEDULE '
                                                                           '13G/A, UPLOAD'},
 ('CRCL', '172573107', 'CIRCLE INTERNET GROUP INC'): {'ticker': 'CRCL',
                                                      'cik': '0001876042',
                                                      'sec_name': 'Circle Internet Group, Inc.',
                                                      'resolution': 'verified',
                                                      'evidence': 'https://data.sec.gov/submissions/CIK0001876042.json',
                                                      'observed_forms': '10-Q, 144, 3, 3/A, 4, 424B4, 425, '
                                                                        '8-A12B, 8-K, CERT, CORRESP, DRS, '
                                                                        'DRS/A, DRSLTR, EFFECT, RW, S-1, '
                                                                        'S-1/A, S-1MEF, S-4, S-4/A, S-8, '
                                                                        'SCHEDULE 13G, SCHEDULE 13G/A, '
                                                                        'UPLOAD'},
 ('CRSP', 'H17182108', 'CRISPR THERAPEUTICS AG'): {'ticker': 'CRSP',
                                                   'cik': '0001674416',
                                                   'sec_name': 'CRISPR Therapeutics AG',
                                                   'resolution': 'verified',
                                                   'evidence': 'https://data.sec.gov/submissions/CIK0001674416.json',
                                                   'observed_forms': '10-K, 10-Q, 144, 3, 3/A, 4, 4/A, '
                                                                     '424B5, 8-K, ARS, CORRESP, DEF 14A, '
                                                                     'DEFA14A, PRE 14A, S-3ASR, S-8, SC '
                                                                     '13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, '
                                                                     'SCHEDULE 13G/A, UPLOAD'},
 ('CRWD', '22788C105', 'CROWDSTRIKE HOLDINGS INC - A'): {'ticker': 'CRWD',
                                                         'cik': '0001535527',
                                                         'sec_name': 'CrowdStrike Holdings, Inc.',
                                                         'resolution': 'verified',
                                                         'evidence': 'https://data.sec.gov/submissions/CIK0001535527.json',
                                                         'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, '
                                                                           '4/A, 424B5, 8-K, ARS, DEF 14A, '
                                                                           'DEFA14A, FWP, S-3ASR, S-8, SC '
                                                                           '13G, SC 13G/A'},
 ('CRWV', '21873S108', 'COREWEAVE INC-CL A'): {'ticker': 'CRWV',
                                               'cik': '0001769628',
                                               'sec_name': 'CoreWeave, Inc.',
                                               'resolution': 'verified',
                                               'evidence': 'https://data.sec.gov/submissions/CIK0001769628.json',
                                               'observed_forms': '10-Q, 144, 3, 3/A, 4, 4/A, 424B3, 424B4, '
                                                                 '425, 8-A12B, 8-K, 8-K/A, CERT, CORRESP, D, '
                                                                 'DRS, DRS/A, DRSLTR, EFFECT, S-1, S-1/A, '
                                                                 'S-4, S-4/A, S-8, SC 13D, SC 13D/A, '
                                                                 'SCHEDULE 13G, SCHEDULE 13G/A, SEC STAFF '
                                                                 'LETTER, UPLOAD'},
 ('DASH', '25809K105', 'DOORDASH INC - A'): {'ticker': 'DASH',
                                             'cik': '0001792789',
                                             'sec_name': 'DoorDash, Inc.',
                                             'resolution': 'verified',
                                             'evidence': 'https://data.sec.gov/submissions/CIK0001792789.json',
                                             'observed_forms': '10-K, 10-Q, 144, 144/A, 25, 3, 3/A, 4, 4/A, '
                                                               '425, 8-A12B, 8-K, ARS, CERT, CORRESP, DEF '
                                                               '14A, DEFA14A, EFFECT, PRE 14A, PX14A6G, S-4, '
                                                               'S-4/A, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, '
                                                               'SCHEDULE 13G/A, UPLOAD'},
 ('DDOG', '23804L103', 'DATADOG INC - CLASS A'): {'ticker': 'DDOG',
                                                  'cik': '0001561550',
                                                  'sec_name': 'Datadog, Inc.',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0001561550.json',
                                                  'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, 4/A, 5, '
                                                                    '8-K, ARS, CORRESP, DEF 14A, DEFA14A, '
                                                                    'PRE 14A, S-8, SC 13G, SC 13G/A, '
                                                                    'SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD'},
 ('DE', '244199105', 'DEERE & CO'): {'ticker': 'DE',
                                     'cik': '0000315189',
                                     'sec_name': 'DEERE & CO',
                                     'resolution': 'verified',
                                     'evidence': 'https://data.sec.gov/submissions/CIK0000315189.json',
                                     'observed_forms': '10-K, 10-Q, 11-K, 13F-HR, 13F-HR/A, 144, 25-NSE, 3, '
                                                       '4, 4/A, 424B2, 424B3, 8-K, ARS, CORRESP, DEF 14A, '
                                                       'DEFA14A, FWP, IRANNOTICE, PX14A6G, S-3ASR, SC 13D/A, '
                                                       'SC 13G, SC 13G/A, SD, UPLOAD'},
 ('DKNG UW', '26142V105', 'DRAFTKINGS INC-CL A'): {'ticker': 'DKNG',
                                                   'cik': '0001883685',
                                                   'sec_name': 'DraftKings Inc.',
                                                   'resolution': 'verified',
                                                   'evidence': 'https://data.sec.gov/submissions/CIK0001883685.json',
                                                   'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B3, '
                                                                     '424B7, 8-K, 8-K/A, 8-K12B, ARS, '
                                                                     'CORRESP, D, DEF 14A, DEFA14A, EFFECT, '
                                                                     'POS AM, PX14A6G, S-3ASR, S-4, S-4/A, '
                                                                     'S-8, SC 13G, SC 13G/A, SCHEDULE 13G, '
                                                                     'SCHEDULE 13G/A, UPLOAD'},
 ('DSY', '6177878', 'DISCOVERY LTD'): {'ticker': 'DSY',
                                       'cik': '',
                                       'sec_name': '',
                                       'resolution': 'no_verified_sec_match',
                                       'evidence': 'https://www.discovery.co.za/corporate/investor-listing-info',
                                       'observed_forms': ''},
 ('DSY FP', 'BM8H5Y5', 'DASSAULT SYSTEMES SE'): {'ticker': 'DSY',
                                                 'cik': '0001016118',
                                                 'sec_name': 'DASSAULT SYSTEMES SE',
                                                 'resolution': 'verified',
                                                 'evidence': 'https://data.sec.gov/submissions/CIK0001016118.json',
                                                 'observed_forms': ''},
 ('ESLT', 'M3760D101', 'ELBIT SYSTEMS LTD'): {'ticker': 'ESLT',
                                              'cik': '0001027664',
                                              'sec_name': 'ELBIT SYSTEMS LTD',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001027664.json',
                                              'observed_forms': '20-F, 424B5, 6-K, CORRESP, F-3ASR, S-8, SC '
                                                                '13G, SC 13G/A, SCHEDULE 13D/A, SD, UPLOAD'},
 ('ETHQ/U', 'BQ84B35', '3IQ ETHER STAKING ETF'): {'ticker': 'ETHQ/U',
                                                  'cik': '',
                                                  'sec_name': '',
                                                  'resolution': 'fund_holding',
                                                  'evidence': 'Frozen holdings: fund security; outside '
                                                              'operating-company sample',
                                                  'observed_forms': ''},
 ('ETOR', 'G32089107', 'ETORO GROUP LTD-A'): {'ticker': 'ETOR',
                                              'cik': '0001493318',
                                              'sec_name': 'eToro Group Ltd.',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001493318.json',
                                              'observed_forms': '144, 424B4, 425, 6-K, 8-A12B, CERT, '
                                                                'CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, '
                                                                'F-1, F-1/A, F-1MEF, F-4, F-4/A, RW, S-8, '
                                                                'SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, '
                                                                'UPLOAD'},
 ('FIG', '316841105', 'FIGMA INC-CL A'): {'ticker': 'FIG',
                                          'cik': '0001579878',
                                          'sec_name': 'Figma, Inc.',
                                          'resolution': 'verified',
                                          'evidence': 'https://data.sec.gov/submissions/CIK0001579878.json',
                                          'observed_forms': '10-Q, 144, 3, 4, 424B4, 8-A12B, 8-K, CERT, '
                                                            'CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, S-1, '
                                                            'S-1/A, S-8, SCHEDULE 13D, SCHEDULE 13G, UPLOAD'},
 ('FRNM', '35661P100', 'FREENOME INC'): {'ticker': 'FRNM',
                                         'cik': '0002017526',
                                         'sec_name': 'Freenome, Inc.',
                                         'resolution': 'verified',
                                         'evidence': 'https://data.sec.gov/submissions/CIK0002017526.json',
                                         'observed_forms': '10-K, 10-Q, 3, 4, 424B4, 425, 8-A12B, 8-K, '
                                                           '8-K/A, CERT, CORRESP, DRS, EFFECT, S-1, S-1/A, '
                                                           'SC 13G, SCHEDULE 13D, UPLOAD'},
 ('FUTU', '36118L106', 'FUTU HOLDINGS LTD-ADR'): {'ticker': 'FUTU',
                                                  'cik': '0001754581',
                                                  'sec_name': 'Futu Holdings Ltd',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0001754581.json',
                                                  'observed_forms': '144, 144/A, 20-F, 424B3, 424B5, 6-K, '
                                                                    'CORRESP, SC 13D/A, SC 13G, SC 13G/A, '
                                                                    'SCHEDULE 13G, UPLOAD'},
 ('GENB', '370920100', 'GENERATE BIOMEDICINES INC'): {'ticker': 'GENB',
                                                      'cik': '0002100782',
                                                      'sec_name': 'Generate Biomedicines, Inc.',
                                                      'resolution': 'verified',
                                                      'evidence': 'https://data.sec.gov/submissions/CIK0002100782.json',
                                                      'observed_forms': 'DRS'},
 ('GENI', 'G3934V109', 'GENIUS SPORTS LTD'): {'ticker': 'GENI',
                                              'cik': '0001834489',
                                              'sec_name': 'Genius Sports Ltd',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001834489.json',
                                              'observed_forms': '144, 144/A, 20-F, 20-F/A, 25-NSE, 424B3, '
                                                                '424B4, 424B5, 425, 6-K, 6-K/A, 8-A12B, '
                                                                'CERT, CORRESP, D, DRS, DRSLTR, EFFECT, F-1, '
                                                                'F-1/A, F-1MEF, F-3, F-3ASR, F-4, F-4/A, POS '
                                                                'AM, POS EX, RW, S-8, SC 13G, SC 13G/A, SC '
                                                                'TO-I, SC TO-I/A, SCHEDULE 13G, SCHEDULE '
                                                                '13G/A, UPLOAD'},
 ('GH', '40131M109', 'GUARDANT HEALTH INC'): {'ticker': 'GH',
                                              'cik': '0001576280',
                                              'sec_name': 'Guardant Health, Inc.',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001576280.json',
                                              'observed_forms': '10-K, 10-Q, 144, 3, 3/A, 4, 4/A, 424B5, 5, '
                                                                '8-K, ARS, CT ORDER, DEF 14A, DEFA14A, FWP, '
                                                                'S-3ASR, S-8, SC 13D/A, SC 13G, SC 13G/A, '
                                                                'SCHEDULE 13G/A'},
 ('GLBE', 'M5216V106', 'GLOBAL-E ONLINE LTD'): {'ticker': 'GLBE',
                                                'cik': '0001835963',
                                                'sec_name': 'Global-E Online Ltd.',
                                                'resolution': 'verified',
                                                'evidence': 'https://data.sec.gov/submissions/CIK0001835963.json',
                                                'observed_forms': '144, 20-F, 424B4, 6-K, 6-K/A, 8-A12B, '
                                                                  'CERT, CORRESP, DRS, DRS/A, DRSLTR, '
                                                                  'EFFECT, F-1, F-1/A, S-8, SC 13G, SC '
                                                                  '13G/A, SCHEDULE 13G/A, SEC STAFF LETTER, '
                                                                  'UPLOAD'},
 ('GOOG', '02079K107', 'ALPHABET INC-CL C'): {'ticker': 'GOOG',
                                              'cik': '0001652044',
                                              'sec_name': 'Alphabet Inc.',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001652044.json',
                                              'observed_forms': '10-K, 10-Q, 13F-HR, 144, 144/A, 3, 3/A, 4, '
                                                                '4/A, 424B2, 424B5, 5, 5/A, 8-A12B, 8-K, '
                                                                'ARS, CERT, DEF 14A, DEFA14A, FWP, '
                                                                'IRANNOTICE, N-PX, PRE 14A, PX14A6G, S-3ASR, '
                                                                'S-8, S-8 POS, SC 13G, SC 13G/A, SCHEDULE '
                                                                '13G/A, SD'},
 ('GOOGL', '02079K305', 'ALPHABET INC-CL A'): {'ticker': 'GOOGL',
                                               'cik': '0001652044',
                                               'sec_name': 'Alphabet Inc.',
                                               'resolution': 'verified',
                                               'evidence': 'https://data.sec.gov/submissions/CIK0001652044.json',
                                               'observed_forms': '10-K, 10-Q, 13F-HR, 144, 144/A, 3, 3/A, 4, '
                                                                 '4/A, 424B2, 424B5, 5, 5/A, 8-A12B, 8-K, '
                                                                 'ARS, CERT, DEF 14A, DEFA14A, FWP, '
                                                                 'IRANNOTICE, N-PX, PRE 14A, PX14A6G, '
                                                                 'S-3ASR, S-8, S-8 POS, SC 13G, SC 13G/A, '
                                                                 'SCHEDULE 13G/A, SD'},
 ('GRMN UN', 'B3Z5T14', 'GARMIN LTD'): {'ticker': 'GRMN',
                                        'cik': '0001121788',
                                        'sec_name': 'GARMIN LTD',
                                        'resolution': 'verified',
                                        'evidence': 'https://data.sec.gov/submissions/CIK0001121788.json',
                                        'observed_forms': '10-K, 10-K/A, 10-Q, 10-Q/A, 11-K, 144, 25, 3, '
                                                          '3/A, 4, 4/A, 5, 8-A12B, 8-K, 8-K/A, ARS, CERT, '
                                                          'DEF 14A, DEFA14A, DEFR14A, PRE 14A, S-8, SC 13G, '
                                                          'SC 13G/A, SCHEDULE 13G/A, SD'},
 ('GTLB', '37637K108', 'GITLAB INC-CL A'): {'ticker': 'GTLB',
                                            'cik': '0001653482',
                                            'sec_name': 'Gitlab Inc.',
                                            'resolution': 'verified',
                                            'evidence': 'https://data.sec.gov/submissions/CIK0001653482.json',
                                            'observed_forms': '10-K, 10-Q, 144, 3, 3/A, 4, 4/A, 424B4, 5, '
                                                              '8-A12B, 8-K, 8-K/A, ARS, CERT, CORRESP, DEF '
                                                              '14A, DEFA14A, DRS, DRS/A, DRSLTR, EFFECT, NT '
                                                              '10-Q, PRE 14A, S-1, S-1/A, S-3ASR, S-8, SC '
                                                              '13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, '
                                                              'UPLOAD'},
 ('HEI', '422806109', 'HEICO CORP'): {'ticker': 'HEI',
                                      'cik': '0000046619',
                                      'sec_name': 'HEICO CORP',
                                      'resolution': 'verified',
                                      'evidence': 'https://data.sec.gov/submissions/CIK0000046619.json',
                                      'observed_forms': '10-K, 10-Q, 144, 3, 4, 424B5, 5, 8-K, 8-K/A, ARS, '
                                                        'CORRESP, D, DEF 14A, DEFA14A, FWP, S-3ASR, S-8, SC '
                                                        '13G, SC 13G/A, SCHEDULE 13G/A, SD, UPLOAD'},
 ('HO', '4162791', 'THALES SA'): {'ticker': 'HO',
                                  'cik': '0001884735',
                                  'sec_name': 'Thales S.A.',
                                  'resolution': 'verified',
                                  'evidence': 'https://data.sec.gov/submissions/CIK0001884735.json',
                                  'observed_forms': '3'},
 ('HON', '438516106', 'HONEYWELL INTERNATIONAL INC'): {'ticker': 'HON',
                                                       'cik': '0000773840',
                                                       'sec_name': 'HONEYWELL INTERNATIONAL INC',
                                                       'resolution': 'verified',
                                                       'evidence': 'https://data.sec.gov/submissions/CIK0000773840.json',
                                                       'observed_forms': '10-K, 10-Q, 11-K, 144, 25, 25-NSE, '
                                                                         '3, 3/A, 4, 424B3, 424B5, 5, '
                                                                         '8-A12B, 8-K, 8-K/A, ARS, CERT, '
                                                                         'CORRESP, DEF 14A, DEFA14A, '
                                                                         'DEFR14A, FWP, PRE 14A, PX14A6G, '
                                                                         'S-3ASR, SC 13D, SC 13D/A, SC 13G, '
                                                                         'SC 13G/A, SD, UPLOAD'},
 ('HOOD', '770700102', 'ROBINHOOD MARKETS INC - A'): {'ticker': 'HOOD',
                                                      'cik': '0001783879',
                                                      'sec_name': 'Robinhood Markets, Inc.',
                                                      'resolution': 'verified',
                                                      'evidence': 'https://data.sec.gov/submissions/CIK0001783879.json',
                                                      'observed_forms': '10-K, 10-Q, 144, 3, 3/A, 4, 4/A, '
                                                                        '424B3, 424B4, 5, 8-A12B, 8-K, '
                                                                        '8-K/A, ARS, CERT, CORRESP, DEF 14A, '
                                                                        'DEFA14A, DRS, DRS/A, DRSLTR, '
                                                                        'EFFECT, POS AM, S-1, S-1/A, S-8, '
                                                                        'S-8 POS, SC 13D, SC 13D/A, SC 13G, '
                                                                        'SC 13G/A, SCHEDULE 13G, SCHEDULE '
                                                                        '13G/A, UPLOAD'},
 ('ICE', '45866F104', 'INTERCONTINENTAL EXCHANGE IN'): {'ticker': 'ICE',
                                                        'cik': '0001571949',
                                                        'sec_name': 'Intercontinental Exchange, Inc.',
                                                        'resolution': 'verified',
                                                        'evidence': 'https://data.sec.gov/submissions/CIK0001571949.json',
                                                        'observed_forms': '10-K, 10-K/A, 10-Q, 144, 3, 4, '
                                                                          '4/A, 424B2, 424B3, 424B5, 425, 5, '
                                                                          '8-A12B, 8-K, 8-K/A, ARS, ARS/A, '
                                                                          'CERT, CORRESP, DEF 14A, DEFA14A, '
                                                                          'EFFECT, FWP, POS AM, PRE 14A, '
                                                                          'S-3ASR, S-4, S-4/A, S-8, S-8 POS, '
                                                                          'SC 13D, SC 13D/A, SC 13G/A, '
                                                                          'SCHEDULE 13D/A, SCHEDULE 13G/A, '
                                                                          'UPLOAD'},
 ('ILMN', '452327109', 'ILLUMINA INC'): {'ticker': 'ILMN',
                                         'cik': '0001110803',
                                         'sec_name': 'ILLUMINA, INC.',
                                         'resolution': 'verified',
                                         'evidence': 'https://data.sec.gov/submissions/CIK0001110803.json',
                                         'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B2, 424B3, 424B5, '
                                                           '425, 8-A12G, 8-K, 8-K/A, ARS, CORRESP, DEF 14A, '
                                                           'DEFA14A, DEFC14A, DEFR14A, DFAN14A, EFFECT, FWP, '
                                                           'PRE 14A, PREC14A, PRER14A, PRRN14A, S-3ASR, '
                                                           'S-4/A, S-4MEF, S-8, SC 13G, SC 13G/A, SC TO-I, '
                                                           'SC TO-I/A, SCHEDULE 13G/A, SD, UPLOAD'},
 ('INTU', '461202103', 'INTUIT INC'): {'ticker': 'INTU',
                                       'cik': '0000896878',
                                       'sec_name': 'INTUIT INC.',
                                       'resolution': 'verified',
                                       'evidence': 'https://data.sec.gov/submissions/CIK0000896878.json',
                                       'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, 4/A, 424B5, 424B7, '
                                                         '8-K, ARS, CORRESP, DEF 14A, DEFA14A, FWP, PRE 14A, '
                                                         'PX14A6G, S-3ASR, S-8, S-8 POS, SC 13G/A, SCHEDULE '
                                                         '13G/A, SD, UPLOAD'},
 ('IONS', '462222100', 'IONIS PHARMACEUTICALS INC'): {'ticker': 'IONS',
                                                      'cik': '0000874015',
                                                      'sec_name': 'IONIS PHARMACEUTICALS INC',
                                                      'resolution': 'verified',
                                                      'evidence': 'https://data.sec.gov/submissions/CIK0000874015.json',
                                                      'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 3/A, 4, '
                                                                        '4/A, 424B5, 5, 8-K, 8-K/A, ARS, '
                                                                        'CORRESP, DEF 14A, DEFA14A, S-3ASR, '
                                                                        'S-8, SC 13G, SC 13G/A, SCHEDULE '
                                                                        '13G, SCHEDULE 13G/A, UPLOAD'},
 ('IRDM', '46269C102', 'IRIDIUM COMMUNICATIONS INC'): {'ticker': 'IRDM',
                                                       'cik': '0001418819',
                                                       'sec_name': 'Iridium Communications Inc.',
                                                       'resolution': 'verified',
                                                       'evidence': 'https://data.sec.gov/submissions/CIK0001418819.json',
                                                       'observed_forms': '10-K, 10-K/A, 10-Q, 144, 3, 4, '
                                                                         '4/A, 5, 8-K, 8-K/A, ARS, DEF 14A, '
                                                                         'DEFA14A, PRE 14A, S-8, SC 13D/A, '
                                                                         'SC 13G, SC 13G/A, SCHEDULE 13D/A, '
                                                                         'SCHEDULE 13G/A, SD'},
 ('ISRG', '46120E602', 'INTUITIVE SURGICAL INC'): {'ticker': 'ISRG',
                                                   'cik': '0001035267',
                                                   'sec_name': 'INTUITIVE SURGICAL INC',
                                                   'resolution': 'verified',
                                                   'evidence': 'https://data.sec.gov/submissions/CIK0001035267.json',
                                                   'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 8-K, ARS, '
                                                                     'CORRESP, DEF 14A, DEFA14A, PRE 14A, '
                                                                     'PX14A6G, S-8, SC 13G/A, SD, UPLOAD'},
 ('JOBY', 'G65163100', 'JOBY AVIATION INC'): {'ticker': 'JOBY',
                                              'cik': '0001819848',
                                              'sec_name': 'Joby Aviation, Inc.',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001819848.json',
                                              'observed_forms': '10-K, 10-K/A, 10-Q, 144, 25-NSE, 3, 4, 4/A, '
                                                                '424B3, 424B5, 424B7, 425, 8-K, 8-K/A, ARS, '
                                                                'CORRESP, D, DEF 14A, DEFA14A, EFFECT, POS '
                                                                'AM, POS EX, PRE 14A, S-1, S-3, S-3ASR, S-4, '
                                                                'S-4/A, S-4MEF, S-8, SC 13D, SC 13D/A, SC '
                                                                '13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE '
                                                                '13G/A, UPLOAD'},
 ('KDK', '500081104', 'KODIAK AI INC'): {'ticker': 'KDK',
                                         'cik': '0001853138',
                                         'sec_name': 'Kodiak AI, Inc.',
                                         'resolution': 'verified',
                                         'evidence': 'https://data.sec.gov/submissions/CIK0001853138.json',
                                         'observed_forms': '10-K, 10-Q, 25, 3, 4, 4/A, 424B3, 424B4, 425, '
                                                           '8-A12B, 8-K, 8-K/A, CERT, CORRESP, D, DEF 14A, '
                                                           'DEFA14A, DRS, DRS/A, EFFECT, POS AM, PRE 14A, '
                                                           'S-1, S-1/A, S-1MEF, S-4, S-4/A, S-8, SC 13G, SC '
                                                           '13G/A, SCHEDULE 13D, SCHEDULE 13G, SCHEDULE '
                                                           '13G/A, UPLOAD'},
 ('KLAR', 'G5279N105', 'KLARNA GROUP PLC'): {'ticker': 'KLAR',
                                             'cik': '0002003292',
                                             'sec_name': 'Klarna Group plc',
                                             'resolution': 'verified',
                                             'evidence': 'https://data.sec.gov/submissions/CIK0002003292.json',
                                             'observed_forms': '424B4, 6-K, 8-A12B, CERT, CORRESP, D, D/A, '
                                                               'DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, S-8, '
                                                               'SCHEDULE 13G, UPLOAD'},
 ('KMTUY', '500458401', 'KOMATSU LTD -SPONS ADR'): {'ticker': 'KMTUY',
                                                    'cik': '0000056594',
                                                    'sec_name': 'KOMATSU LTD',
                                                    'resolution': 'verified',
                                                    'evidence': 'https://data.sec.gov/submissions/CIK0000056594.json',
                                                    'observed_forms': ''},
 ('KSPI', 'BJY21K1', 'JSC KASPI.KZ ADR'): {'ticker': 'KSPI',
                                           'cik': '0001985487',
                                           'sec_name': 'Joint Stock Co Kaspi.kz',
                                           'resolution': 'verified',
                                           'evidence': 'https://data.sec.gov/submissions/CIK0001985487.json',
                                           'observed_forms': '144, 20-F, 424B4, 6-K, 8-A12B, CERT, CORRESP, '
                                                             'DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, '
                                                             'F-1MEF, S-8, SC 13G, SCHEDULE 13D, SCHEDULE '
                                                             '13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD'},
 ('KTOS', '50077B207', 'KRATOS DEFENSE & SECURITY'): {'ticker': 'KTOS',
                                                      'cik': '0001069258',
                                                      'sec_name': 'KRATOS DEFENSE & SECURITY SOLUTIONS, INC.',
                                                      'resolution': 'verified',
                                                      'evidence': 'https://data.sec.gov/submissions/CIK0001069258.json',
                                                      'observed_forms': '10-K, 10-Q, 10-Q/A, 144, 3, 4, 4/A, '
                                                                        '424B3, 424B5, 8-K, ARS, ARS/A, '
                                                                        'CORRESP, DEF 14A, DEFA14A, POSASR, '
                                                                        'S-3ASR, S-8, SC 13G, SC 13G/A, '
                                                                        'SCHEDULE 13G, SCHEDULE 13G/A, SD, '
                                                                        'UPLOAD'},
 ('LHX', '502431109', 'L3HARRIS TECHNOLOGIES INC'): {'ticker': 'LHX',
                                                     'cik': '0000202058',
                                                     'sec_name': 'L3HARRIS TECHNOLOGIES, INC. /DE/',
                                                     'resolution': 'verified',
                                                     'evidence': 'https://data.sec.gov/submissions/CIK0000202058.json',
                                                     'observed_forms': '10-K, 10-Q, 11-K, 144, 144/A, '
                                                                       '15-12G, 3, 4, 4/A, 424B5, 8-K, '
                                                                       '8-K/A, ARS, CORRESP, DEF 14A, '
                                                                       'DEFA14A, FWP, PRE 14A, PX14A6G, '
                                                                       'S-3ASR, S-8, S-8 POS, SC 13D, SC '
                                                                       '13G, SC 13G/A, SCHEDULE 13G/A, SD, '
                                                                       'UPLOAD'},
 ('LLY', '532457108', 'ELI LILLY & CO'): {'ticker': 'LLY',
                                          'cik': '0000059478',
                                          'sec_name': 'ELI LILLY & Co',
                                          'resolution': 'verified',
                                          'evidence': 'https://data.sec.gov/submissions/CIK0000059478.json',
                                          'observed_forms': '10-K, 10-Q, 11-K, 144, 25-NSE, 3, 3/A, 4, '
                                                            '424B2, 5, 8-A12B, 8-K, CERT, CORRESP, CT ORDER, '
                                                            'DEF 14A, DEFA14A, FWP, PRE 14A, PX14A6G, '
                                                            'S-3ASR, S-8, SC 13D, SC 13D/A, SC 13G, SC '
                                                            '13G/A, SC TO-C, SC TO-T, SC TO-T/A, SCHEDULE '
                                                            '13G/A, SD, UPLOAD'},
 ('LMT', '539830109', 'LOCKHEED MARTIN CORP'): {'ticker': 'LMT',
                                                'cik': '0000936468',
                                                'sec_name': 'LOCKHEED MARTIN CORP',
                                                'resolution': 'verified',
                                                'evidence': 'https://data.sec.gov/submissions/CIK0000936468.json',
                                                'observed_forms': '10-K, 10-Q, 11-K, 13F-HR, 144, 3, 3/A, 4, '
                                                                  '4/A, 424B2, 424B5, 8-K, ARS, CORRESP, DEF '
                                                                  '14A, DEFA14A, DEFR14A, FWP, POSASR, '
                                                                  'PX14A6G, S-3ASR, S-8, SC 13D, SC 13D/A, '
                                                                  'SC 13G, SC 13G/A, SD, UPLOAD'},
 ('LUNR', '46125A100', 'INTUITIVE MACHINES INC'): {'ticker': 'LUNR',
                                                   'cik': '0001844452',
                                                   'sec_name': 'Intuitive Machines, Inc.',
                                                   'resolution': 'verified',
                                                   'evidence': 'https://data.sec.gov/submissions/CIK0001844452.json',
                                                   'observed_forms': '10-K, 10-Q, 144, 25-NSE, 3, 4, 4/A, '
                                                                     '424B2, 424B3, 424B4, 425, 8-A12B, 8-K, '
                                                                     '8-K/A, ARS, CERT, CORRESP, DEF 14A, '
                                                                     'DEF 14C, DEFA14A, DEL AM, DRS, EFFECT, '
                                                                     'NT 10-K, NT 10-Q, POS AM, PRE 14C, '
                                                                     'S-1, S-1/A, S-3, S-4, S-4/A, S-8, SC '
                                                                     '13D, SC 13D/A, SC 13G, SC 13G/A, '
                                                                     'SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE '
                                                                     '13G/A, UPLOAD'},
 ('MASS', '65443P102', '908 DEVICES INC'): {'ticker': 'MASS',
                                            'cik': '0001555279',
                                            'sec_name': '908 Devices Inc.',
                                            'resolution': 'verified',
                                            'evidence': 'https://data.sec.gov/submissions/CIK0001555279.json',
                                            'observed_forms': '10-K, 10-Q, 144, 3, 3/A, 4, 4/A, 424B4, 5, '
                                                              '8-K, 8-K/A, ARS, CORRESP, DEF 14A, DEFA14A, '
                                                              'DRS, EFFECT, S-1, S-3, S-8, SC 13G, SC 13G/A, '
                                                              'SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD'},
 ('MELI', '58733R102', 'MERCADOLIBRE INC'): {'ticker': 'MELI',
                                             'cik': '0001099590',
                                             'sec_name': 'MERCADOLIBRE INC',
                                             'resolution': 'verified',
                                             'evidence': 'https://data.sec.gov/submissions/CIK0001099590.json',
                                             'observed_forms': '10-K, 10-Q, 144, 3, 4, 424B2, 424B5, 5, '
                                                               '8-A12B, 8-K, 8-K/A, CERT, CORRESP, DEF 14A, '
                                                               'DEFA14A, FWP, PRE 14A, S-3ASR, SC 13D, SC '
                                                               '13D/A, SC 13G, SC 13G/A, SCHEDULE 13G/A, '
                                                               'UPLOAD'},
 ('META', '30303M102', 'META PLATFORMS INC-CLASS A'): {'ticker': 'META',
                                                       'cik': '0001326801',
                                                       'sec_name': 'Meta Platforms, Inc.',
                                                       'resolution': 'verified',
                                                       'evidence': 'https://data.sec.gov/submissions/CIK0001326801.json',
                                                       'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B2, '
                                                                         '424B3, 5, 8-K, 8-K/A, ARS, '
                                                                         'CORRESP, DEF 14A, DEF 14C, '
                                                                         'DEFA14A, DEFA14C, EFFECT, FWP, PRE '
                                                                         '14A, PRE 14C, PX14A6G, S-3ASR, '
                                                                         'S-4, S-8, S-8 POS, SC 13G/A, '
                                                                         'SCHEDULE 13G/A, SD, UPLOAD'},
 ('NET', '18915M107', 'CLOUDFLARE INC - CLASS A'): {'ticker': 'NET',
                                                    'cik': '0001477333',
                                                    'sec_name': 'Cloudflare, Inc.',
                                                    'resolution': 'verified',
                                                    'evidence': 'https://data.sec.gov/submissions/CIK0001477333.json',
                                                    'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 40-APP, '
                                                                      '8-K, 8-K/A, APP NTC, APP ORDR, ARS, '
                                                                      'DEF 14A, DEFA14A, PRE 14A, S-8, SC '
                                                                      '13G, SC 13G/A, SCHEDULE 13G/A'},
 ('NFLX', '64110L106', 'NETFLIX INC'): {'ticker': 'NFLX',
                                        'cik': '0001065280',
                                        'sec_name': 'NETFLIX INC',
                                        'resolution': 'verified',
                                        'evidence': 'https://data.sec.gov/submissions/CIK0001065280.json',
                                        'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 3/A, 4, 4/A, 424B2, '
                                                          '424B5, 425, 8-K, 8-K/A, ARS, DEF 14A, DEFA14A, '
                                                          'FWP, PRE 14A, PX14A6G, S-3ASR, SC 13G, SC 13G/A, '
                                                          'SCHEDULE 13G/A'},
 ('NRIX', '67080M103', 'NURIX THERAPEUTICS INC'): {'ticker': 'NRIX',
                                                   'cik': '0001549595',
                                                   'sec_name': 'Nurix Therapeutics, Inc.',
                                                   'resolution': 'verified',
                                                   'evidence': 'https://data.sec.gov/submissions/CIK0001549595.json',
                                                   'observed_forms': '10-K, 10-Q, 144, 3, 4, 424B4, 424B5, '
                                                                     '8-K, ARS, CORRESP, DEF 14A, DEFA14A, '
                                                                     'DRS, EFFECT, FWP, POS AM, POS EX, '
                                                                     'POSASR, S-1, S-3ASR, S-8, SC 13G, SC '
                                                                     '13G/A, SCHEDULE 13G, SCHEDULE 13G/A, '
                                                                     'UPLOAD'},
 ('NTLA', '45826J105', 'INTELLIA THERAPEUTICS INC'): {'ticker': 'NTLA',
                                                      'cik': '0001652130',
                                                      'sec_name': 'Intellia Therapeutics, Inc.',
                                                      'resolution': 'verified',
                                                      'evidence': 'https://data.sec.gov/submissions/CIK0001652130.json',
                                                      'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B5, '
                                                                        '8-K, ARS, DEF 14A, DEFA14A, PRE '
                                                                        '14A, S-3ASR, S-8, SC 13D/A, SC 13G, '
                                                                        'SC 13G/A, SCHEDULE 13G, SCHEDULE '
                                                                        '13G/A'},
 ('NTRA', '632307104', 'NATERA INC'): {'ticker': 'NTRA',
                                       'cik': '0001604821',
                                       'sec_name': 'Natera, Inc.',
                                       'resolution': 'verified',
                                       'evidence': 'https://data.sec.gov/submissions/CIK0001604821.json',
                                       'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B5, 5, 8-K, ARS, '
                                                         'CORRESP, DEF 14A, DEFA14A, POSASR, RW, S-3, '
                                                         'S-3ASR, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, '
                                                         'SCHEDULE 13G/A, UPLOAD'},
 ('NU UN', 'G6683N103', 'NU HOLDINGS LTD/CAYMAN ISL-A'): {'ticker': 'NU',
                                                          'cik': '0001691493',
                                                          'sec_name': 'Nu Holdings Ltd.',
                                                          'resolution': 'verified',
                                                          'evidence': 'https://data.sec.gov/submissions/CIK0001691493.json',
                                                          'observed_forms': '144, 144/A, 20-F, 424B1, 6-K, '
                                                                            '6-K/A, 8-A12B, CERT, CORRESP, '
                                                                            'D, DRS, DRS/A, DRSLTR, EFFECT, '
                                                                            'F-1, F-1/A, S-8, SC 13G, SC '
                                                                            '13G/A, SCHEDULE 13G, SCHEDULE '
                                                                            '13G/A, UPLOAD'},
 ('NVDA', '67066G104', 'NVIDIA CORP'): {'ticker': 'NVDA',
                                        'cik': '0001045810',
                                        'sec_name': 'NVIDIA CORP',
                                        'resolution': 'verified',
                                        'evidence': 'https://data.sec.gov/submissions/CIK0001045810.json',
                                        'observed_forms': '10-K, 10-Q, 13F-HR, 144, 144/A, 3, 4, 4/A, 424B5, '
                                                          '5, 5/A, 8-K, ARS, CORRESP, DEF 14A, DEFA14A, '
                                                          'EFFECT, FWP, N-PX, PRE 14A, PX14A6G, S-3, S-3/A, '
                                                          'S-3ASR, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, '
                                                          'SCHEDULE 13G/A, SD, UPLOAD'},
 ('OKLO', '02156V109', 'OKLO INC'): {'ticker': 'OKLO',
                                     'cik': '0001849056',
                                     'sec_name': 'Oklo Inc.',
                                     'resolution': 'verified',
                                     'evidence': 'https://data.sec.gov/submissions/CIK0001849056.json',
                                     'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B3, 424B4, 424B5, '
                                                       '425, 8-A12B, 8-K, ARS, CERT, CORRESP, DEF 14A, '
                                                       'DEFA14A, DRS, EFFECT, NT 10-Q, POS AM, POS EX, PRE '
                                                       '14A, S-1, S-1/A, S-1MEF, S-3, S-3/A, S-4, S-4/A, '
                                                       'S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE '
                                                       '13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, '
                                                       'SEC STAFF LETTER, UPLOAD'},
 ('P', '74624M102', 'EVERPURE INC-A'): {'ticker': 'P',
                                        'cik': '0001474432',
                                        'sec_name': 'Everpure, Inc.',
                                        'resolution': 'verified',
                                        'evidence': 'https://data.sec.gov/submissions/CIK0001474432.json',
                                        'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 5, 8-K, ARS, CORRESP, '
                                                          'DEF 14A, DEFA14A, S-8, SC 13G, SC 13G/A, SCHEDULE '
                                                          '13G/A, SD, UPLOAD'},
 ('PACB', '69404D108', 'PACIFIC BIOSCIENCES OF CALIF'): {'ticker': 'PACB',
                                                         'cik': '0001299130',
                                                         'sec_name': 'PACIFIC BIOSCIENCES OF CALIFORNIA, '
                                                                     'INC.',
                                                         'resolution': 'verified',
                                                         'evidence': 'https://data.sec.gov/submissions/CIK0001299130.json',
                                                         'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 3/A, '
                                                                           '4, 4/A, 424B5, 424B7, 8-K, '
                                                                           '8-K/A, ARS, CORRESP, D, DEF 14A, '
                                                                           'DEFA14A, EFFECT, POS AM, POSASR, '
                                                                           'PRE 14A, S-3ASR, S-8, SC 13G, SC '
                                                                           '13G/A, SCHEDULE 13G, SCHEDULE '
                                                                           '13G/A, SD, UPLOAD'},
 ('PINS', '72352L106', 'PINTEREST INC- CLASS A'): {'ticker': 'PINS',
                                                   'cik': '0001506293',
                                                   'sec_name': 'PINTEREST, INC.',
                                                   'resolution': 'verified',
                                                   'evidence': 'https://data.sec.gov/submissions/CIK0001506293.json',
                                                   'observed_forms': '10-K, 10-Q, 144, 3, 3/A, 4, 4/A, 8-K, '
                                                                     'ARS, DEF 14A, DEFA14A, PRE 14A, '
                                                                     'S-3ASR, S-8, SC 13G, SC 13G/A, '
                                                                     'SCHEDULE 13G, SCHEDULE 13G/A'},
 ('PLTR', '69608A108', 'PALANTIR TECHNOLOGIES INC-A'): {'ticker': 'PLTR',
                                                        'cik': '0001321655',
                                                        'sec_name': 'Palantir Technologies Inc.',
                                                        'resolution': 'verified',
                                                        'evidence': 'https://data.sec.gov/submissions/CIK0001321655.json',
                                                        'observed_forms': '10-K, 10-Q, 13F-HR, 144, 25, 3, '
                                                                          '4, 4/A, 8-A12B, 8-K, 8-K/A, ARS, '
                                                                          'CERT, CORRESP, DEF 14A, DEFA14A, '
                                                                          'PRE 14A, S-3ASR, S-8, SC 13G, SC '
                                                                          '13G/A, SCHEDULE 13G/A, UPLOAD'},
 ('PONY', '732908108', 'PONY AI INC'): {'ticker': 'PONY',
                                        'cik': '0001969302',
                                        'sec_name': 'Pony AI Inc.',
                                        'resolution': 'verified',
                                        'evidence': 'https://data.sec.gov/submissions/CIK0001969302.json',
                                        'observed_forms': '144, 20-F, 424B4, 6-K, 8-A12B, CERT, CORRESP, '
                                                          'DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-6, FWP, '
                                                          'S-8, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD'},
 ('PRME', '74168J101', 'PRIME MEDICINE INC'): {'ticker': 'PRME',
                                               'cik': '0001894562',
                                               'sec_name': 'Prime Medicine, Inc.',
                                               'resolution': 'verified',
                                               'evidence': 'https://data.sec.gov/submissions/CIK0001894562.json',
                                               'observed_forms': '10-K, 10-Q, 144, 3, 3/A, 4, 4/A, 424B4, '
                                                                 '424B5, 8-A12B, 8-K, 8-K/A, ARS, CERT, '
                                                                 'CORRESP, DEF 14A, DEFA14A, DRS, DRS/A, '
                                                                 'DRSLTR, EFFECT, FWP, PRE 14A, S-1, S-1/A, '
                                                                 'S-1MEF, S-3, S-3ASR, S-8, SC 13D, SC '
                                                                 '13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, '
                                                                 'SCHEDULE 13G, SCHEDULE 13G/A, SEC STAFF '
                                                                 'LETTER, UPLOAD'},
 ('PRNT', '00214Q500', 'THE 3D PRINTING ETF'): {'ticker': 'PRNT',
                                                'cik': '',
                                                'sec_name': '',
                                                'resolution': 'fund_holding',
                                                'evidence': 'Frozen holdings: fund security; outside '
                                                            'operating-company sample',
                                                'observed_forms': ''},
 ('PSNL', '71535D106', 'PERSONALIS INC'): {'ticker': 'PSNL',
                                           'cik': '0001527753',
                                           'sec_name': 'Personalis, Inc.',
                                           'resolution': 'verified',
                                           'evidence': 'https://data.sec.gov/submissions/CIK0001527753.json',
                                           'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B5, 8-K, ARS, '
                                                             'CORRESP, DEF 14A, DEFA14A, EFFECT, S-3, S-8, '
                                                             'SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE '
                                                             '13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD'},
 ('PYPL', '70450Y103', 'PAYPAL HOLDINGS INC'): {'ticker': 'PYPL',
                                                'cik': '0001633917',
                                                'sec_name': 'PayPal Holdings, Inc.',
                                                'resolution': 'verified',
                                                'evidence': 'https://data.sec.gov/submissions/CIK0001633917.json',
                                                'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, 424B2, 5, '
                                                                  '8-K, 8-K/A, ARS, CORRESP, DEF 14A, '
                                                                  'DEFA14A, FWP, PX14A6G, S-3ASR, S-8, S-8 '
                                                                  'POS, SC 13D, SC 13G/A, UPLOAD'},
 ('QSI', '74765K105', 'QUANTUM-SI INC'): {'ticker': 'QSI',
                                          'cik': '0001816431',
                                          'sec_name': 'Quantum-Si Inc',
                                          'resolution': 'verified',
                                          'evidence': 'https://data.sec.gov/submissions/CIK0001816431.json',
                                          'observed_forms': '10-K, 10-K/A, 10-Q, 10-Q/A, 144, 25-NSE, 3, 4, '
                                                            '424B3, 424B5, 425, 5, 8-K, 8-K/A, ARS, CORRESP, '
                                                            'DEF 14A, DEFA14A, DEFR14A, EFFECT, NT 10-Q, POS '
                                                            'AM, POS462B, PRE 14A, S-1, S-1/A, S-1MEF, S-3, '
                                                            'S-3/A, S-4, S-4/A, S-8, SC 13D, SC 13D/A, SC '
                                                            '13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, '
                                                            'SCHEDULE 13G/A, SD, UPLOAD'},
 ('RBLX', '771049103', 'ROBLOX CORP -CLASS A'): {'ticker': 'RBLX',
                                                 'cik': '0001315098',
                                                 'sec_name': 'Roblox Corp',
                                                 'resolution': 'verified',
                                                 'evidence': 'https://data.sec.gov/submissions/CIK0001315098.json',
                                                 'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B3, '
                                                                   '424B4, 5, 8-K, 8-K/A, ARS, CERT, '
                                                                   'CORRESP, D, D/A, DEF 14A, DEFA14A, '
                                                                   'EFFECT, POS AM, PRE 14A, S-1/A, S-8, SC '
                                                                   '13G, SC 13G/A, SCHEDULE 13G, SCHEDULE '
                                                                   '13G/A, UPLOAD'},
 ('RBRK', '781154109', 'RUBRIK INC-A'): {'ticker': 'RBRK',
                                         'cik': '0001943896',
                                         'sec_name': 'Rubrik, Inc.',
                                         'resolution': 'verified',
                                         'evidence': 'https://data.sec.gov/submissions/CIK0001943896.json',
                                         'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, 4/A, 424B4, '
                                                           '8-A12B, 8-K, ARS, CERT, CORRESP, DEF 14A, '
                                                           'DEFA14A, DRS, DRS/A, DRSLTR, EFFECT, S-1, S-1/A, '
                                                           'S-1MEF, S-8, SC 13G, SCHEDULE 13D, SCHEDULE '
                                                           '13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SEC STAFF '
                                                           'LETTER, UPLOAD'},
 ('RKLB UQ', '773121108', 'ROCKET LAB'): {'ticker': 'RKLB',
                                          'cik': '0001819994',
                                          'sec_name': 'Rocket Lab Corp',
                                          'resolution': 'verified',
                                          'evidence': 'https://data.sec.gov/submissions/CIK0001819994.json',
                                          'observed_forms': '10-K, 10-K/A, 10-Q, 144, 15-12G, 25-NSE, 3, '
                                                            '3/A, 4, 4/A, 424B3, 424B5, 424B7, 425, 8-K, '
                                                            '8-K/A, 8-K12B, ARS, CORRESP, DEF 14A, DEFA14A, '
                                                            'DRS, EFFECT, NT 10-K, NT 10-Q, POS AM, POSASR, '
                                                            'PRE 14A, S-1, S-1/A, S-3ASR, S-4, S-4/A, S-8, '
                                                            'S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, '
                                                            'SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, '
                                                            'SD, UPLOAD'},
 ('ROKU', '77543R102', 'ROKU INC'): {'ticker': 'ROKU',
                                     'cik': '0001428439',
                                     'sec_name': 'ROKU, INC',
                                     'resolution': 'verified',
                                     'evidence': 'https://data.sec.gov/submissions/CIK0001428439.json',
                                     'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B5, 8-K, 8-K/A, ARS, '
                                                       'DEF 14A, DEFA14A, S-3ASR, S-8, SC 13G, SC 13G/A, '
                                                       'SCHEDULE 13G/A, SD'},
 ('RXRX', '75629V104', 'RECURSION PHARMACEUTICALS-A'): {'ticker': 'RXRX',
                                                        'cik': '0001601830',
                                                        'sec_name': 'RECURSION PHARMACEUTICALS, INC.',
                                                        'resolution': 'verified',
                                                        'evidence': 'https://data.sec.gov/submissions/CIK0001601830.json',
                                                        'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 3/A, '
                                                                          '4, 4/A, 424B3, 424B4, 424B5, '
                                                                          '424B7, 8-A12B, 8-K, 8-K/A, ARS, '
                                                                          'CERT, CORRESP, DEF 14A, DEFA14A, '
                                                                          'DEFM14A, DRS, DRS/A, DRSLTR, '
                                                                          'EFFECT, PREM14A, S-1, S-1/A, '
                                                                          'S-1MEF, S-3ASR, S-8, SC 13D, SC '
                                                                          '13D/A, SC 13G, SC 13G/A, SCHEDULE '
                                                                          '13D/A, SCHEDULE 13G/A, SEC STAFF '
                                                                          'LETTER, UPLOAD'},
 ('SCTX', '811033109', 'SCRIBE THERAPEUTICS INC'): {'ticker': 'SCTX',
                                                    'cik': '0001853921',
                                                    'sec_name': 'Scribe Therapeutics, Inc.',
                                                    'resolution': 'verified',
                                                    'evidence': 'https://data.sec.gov/submissions/CIK0001853921.json',
                                                    'observed_forms': 'D'},
 ('SDGR', '80810D103', 'SCHRODINGER INC'): {'ticker': 'SDGR',
                                            'cik': '0001490978',
                                            'sec_name': 'Schrodinger, Inc.',
                                            'resolution': 'verified',
                                            'evidence': 'https://data.sec.gov/submissions/CIK0001490978.json',
                                            'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B5, 5, 8-K, '
                                                              '8-K/A, ARS, DEF 14A, DEFA14A, PRE 14A, '
                                                              'S-3ASR, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, '
                                                              'SCHEDULE 13G/A'},
 ('SE', '81141R100', 'SEA LTD-ADR'): {'ticker': 'SE',
                                      'cik': '0001703399',
                                      'sec_name': 'Sea Ltd',
                                      'resolution': 'verified',
                                      'evidence': 'https://data.sec.gov/submissions/CIK0001703399.json',
                                      'observed_forms': '144, 144/A, 20-F, 424B5, 6-K, CORRESP, CT ORDER, '
                                                        'F-3ASR, FWP, S-8, SC 13D/A, SC 13G, SC 13G/A, '
                                                        'SCHEDULE 13G, UPLOAD'},
 ('SHOP', '82509L107', 'SHOPIFY INC - CLASS A'): {'ticker': 'SHOP',
                                                  'cik': '0001594805',
                                                  'sec_name': 'SHOPIFY INC.',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0001594805.json',
                                                  'observed_forms': '10-K, 10-K/A, 10-Q, 144, 25, 3, 4, '
                                                                    '40-F, 6-K, 6-K/A, 8-A12B, 8-K, CERT, '
                                                                    'CORRESP, F-10, F-X, S-8, S-8 POS, SC '
                                                                    '13D, SC 13D/A, SC 13G, SC 13G/A, '
                                                                    'SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE '
                                                                    '13G/A, SD, SUPPL, UPLOAD'},
 ('SLMT', 'G13311116', 'BRERA HOLDINGS PLC-CL B'): {'ticker': 'SLMT',
                                                    'cik': '0001939965',
                                                    'sec_name': 'Brera Holdings PLC',
                                                    'resolution': 'verified',
                                                    'evidence': 'https://data.sec.gov/submissions/CIK0001939965.json',
                                                    'observed_forms': '20-F, 20-F/A, 424B3, 424B4, 424B5, '
                                                                      '6-K, 8-A12B, CERT, CORRESP, D, DRS, '
                                                                      'DRS/A, DRSLTR, EFFECT, F-1, F-1/A, '
                                                                      'F-3, F-3ASR, NT 20-F, POS AM, S-8, SC '
                                                                      '13D, SC 13D/A, SC 13G, SC 13G/A, '
                                                                      'SCHEDULE 13D, SCHEDULE 13D/A, '
                                                                      'SCHEDULE 13G, UPLOAD'},
 ('SNOW', '833445109', 'SNOWFLAKE INC'): {'ticker': 'SNOW',
                                          'cik': '0001640147',
                                          'sec_name': 'Snowflake Inc.',
                                          'resolution': 'verified',
                                          'evidence': 'https://data.sec.gov/submissions/CIK0001640147.json',
                                          'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 3/A, 4, 4/A, 5, 8-K, '
                                                            'ARS, D, DEF 14A, DEFA14A, PRE 14A, S-8, SC 13G, '
                                                            'SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A'},
 ('SNPS', '871607107', 'SYNOPSYS INC'): {'ticker': 'SNPS',
                                         'cik': '0000883241',
                                         'sec_name': 'SYNOPSYS INC',
                                         'resolution': 'verified',
                                         'evidence': 'https://data.sec.gov/submissions/CIK0000883241.json',
                                         'observed_forms': '10-K, 10-Q, 144, 3, 4, 424B3, 424B5, 425, 8-K, '
                                                           '8-K/A, ARS, CORRESP, D, DEF 14A, DEFA14A, '
                                                           'EFFECT, FWP, PX14A6G, S-3ASR, S-4, S-4/A, S-8, '
                                                           'SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, '
                                                           'SD, UPLOAD'},
 ('SOFI', '83406F102', 'SOFI TECHNOLOGIES INC'): {'ticker': 'SOFI',
                                                  'cik': '0001818874',
                                                  'sec_name': 'SoFi Technologies, Inc.',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0001818874.json',
                                                  'observed_forms': '10-K, 10-K/A, 10-Q, 144, 144/A, 25, '
                                                                    '25-NSE, 3, 3/A, 4, 4/A, 424B3, 425, '
                                                                    '8-A12B, 8-K, 8-K/A, ARS, CERT, CORRESP, '
                                                                    'D, DEF 14A, DEFA14A, EFFECT, FWP, NT '
                                                                    '10-Q, POS AM, PRE 14A, S-1, S-1/A, S-3, '
                                                                    'S-3ASR, S-4, S-4/A, S-8, SC 13D, SC '
                                                                    '13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, '
                                                                    'SCHEDULE 13G/A, UPLOAD'},
 ('SOLQ/U', 'BTRDQ40', '3IQ SOLANA STAKING ETF'): {'ticker': 'SOLQ/U',
                                                   'cik': '',
                                                   'sec_name': '',
                                                   'resolution': 'fund_holding',
                                                   'evidence': 'Frozen holdings: fund security; outside '
                                                               'operating-company sample',
                                                   'observed_forms': ''},
 ('SPCX', '84615Q103', 'SPACE EXPLORATION TECHN-CL A'): {'ticker': 'SPCX',
                                                         'cik': '0001181412',
                                                         'sec_name': 'SPACE EXPLORATION TECHNOLOGIES CORP',
                                                         'resolution': 'verified',
                                                         'evidence': 'https://data.sec.gov/submissions/CIK0001181412.json',
                                                         'observed_forms': 'D, D/A'},
 ('SPOT', 'L8681T102', 'SPOTIFY TECHNOLOGY SA'): {'ticker': 'SPOT',
                                                  'cik': '0001639920',
                                                  'sec_name': 'Spotify Technology S.A.',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0001639920.json',
                                                  'observed_forms': '144, 144/A, 20-F, 6-K, S-8, S-8 POS, SC '
                                                                    '13G, SC 13G/A, SCHEDULE 13G, SCHEDULE '
                                                                    '13G/A'},
 ('SRTA', '092667104', 'STRATA CRITICAL MEDICAL INC'): {'ticker': 'SRTA',
                                                        'cik': '0001779128',
                                                        'sec_name': 'Strata Critical Medical, Inc.',
                                                        'resolution': 'verified',
                                                        'evidence': 'https://data.sec.gov/submissions/CIK0001779128.json',
                                                        'observed_forms': '10-K, 10-K/A, 10-Q, 10-QT, 144, '
                                                                          '25-NSE, 3, 3/A, 4, 4/A, 424B3, '
                                                                          '425, 8-K, 8-K/A, CORRESP, DEF '
                                                                          '14A, DEFA14A, EFFECT, NT 10-Q, '
                                                                          'POS AM, S-1, S-4, S-4/A, S-8, SC '
                                                                          '13D, SC 13D/A, SC 13G, SC 13G/A, '
                                                                          'SCHEDULE 13G, SCHEDULE 13G/A, '
                                                                          'UPLOAD'},
 ('SYM UQ', '87151X101', 'SYMBOTIC INC'): {'ticker': 'SYM',
                                           'cik': '0001837240',
                                           'sec_name': 'Symbotic Inc.',
                                           'resolution': 'verified',
                                           'evidence': 'https://data.sec.gov/submissions/CIK0001837240.json',
                                           'observed_forms': '10-K, 10-Q, 10-Q/A, 144, 144/A, 3, 4, 4/A, '
                                                             '424B3, 424B4, 424B5, 425, 8-A12B, 8-K, 8-K/A, '
                                                             'ARS, CERT, CORRESP, CT ORDER, DEF 14A, '
                                                             'DEFA14A, EFFECT, NT 10-K, POS AM, S-1, S-1/A, '
                                                             'S-3, S-3/A, S-3ASR, S-4, S-4/A, S-8, SC 13D, '
                                                             'SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, '
                                                             'SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, '
                                                             'UPLOAD'},
 ('TDY', '879360105', 'TELEDYNE TECHNOLOGIES INC'): {'ticker': 'TDY',
                                                     'cik': '0001094285',
                                                     'sec_name': 'TELEDYNE TECHNOLOGIES INC',
                                                     'resolution': 'verified',
                                                     'evidence': 'https://data.sec.gov/submissions/CIK0001094285.json',
                                                     'observed_forms': '10-K, 10-Q, 11-K, 144, 144/A, 3, 4, '
                                                                       '424B3, 424B5, 425, 5, 8-K, 8-K/A, '
                                                                       'ARS, CORRESP, DEF 14A, DEFA14A, '
                                                                       'DEFM14A, EFFECT, FWP, PRE 14A, '
                                                                       'PX14A6G, S-3ASR, S-4, S-4/A, SC 13G, '
                                                                       'SC 13G/A, SCHEDULE 13G/A, SD, '
                                                                       'UPLOAD'},
 ('TEM', '88023B103', 'TEMPUS AI INC-CL A'): {'ticker': 'TEM',
                                              'cik': '0001717115',
                                              'sec_name': 'Tempus AI, Inc.',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001717115.json',
                                              'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B3, 424B4, '
                                                                '424B7, 8-A12B, 8-K, ARS, CERT, CORRESP, D, '
                                                                'DEF 14A, DEF 14C, DEFA14A, DRS, DRS/A, '
                                                                'DRSLTR, EFFECT, PRE 14A, PRE 14C, S-1, '
                                                                'S-1/A, S-3ASR, S-8, S-8 POS, SC 13D, SC '
                                                                '13D/A, SC 13G, SCHEDULE 13D/A, SCHEDULE '
                                                                '13G, SCHEDULE 13G/A, UPLOAD'},
 ('TER', '880770102', 'TERADYNE INC'): {'ticker': 'TER',
                                        'cik': '0000097210',
                                        'sec_name': 'TERADYNE, INC',
                                        'resolution': 'verified',
                                        'evidence': 'https://data.sec.gov/submissions/CIK0000097210.json',
                                        'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, 4/A, 5, 8-K, 8-K/A, '
                                                          'ARS, CORRESP, DEF 14A, DEFA14A, PRE 14A, S-8, S-8 '
                                                          'POS, SC 13G, SC 13G/A, SCHEDULE 13G/A, SD, '
                                                          'UPLOAD'},
 ('TOST', '888787108', 'TOAST INC-CLASS A'): {'ticker': 'TOST',
                                              'cik': '0001650164',
                                              'sec_name': 'Toast, Inc.',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001650164.json',
                                              'observed_forms': '10-K, 10-Q, 144, 3, 3/A, 4, 424B4, 5, '
                                                                '8-A12B, 8-K, ARS, CERT, CORRESP, DEF 14A, '
                                                                'DEFA14A, DRS, DRS/A, DRSLTR, EFFECT, PRE '
                                                                '14A, S-1, S-1/A, S-8, SC 13D, SC 13D/A, SC '
                                                                '13G, SC 13G/A, SCHEDULE 13G/A, SD, SEC '
                                                                'STAFF LETTER, UPLOAD'},
 ('TRMB', '896239100', 'TRIMBLE INC'): {'ticker': 'TRMB',
                                        'cik': '0000864749',
                                        'sec_name': 'TRIMBLE INC.',
                                        'resolution': 'verified',
                                        'evidence': 'https://data.sec.gov/submissions/CIK0000864749.json',
                                        'observed_forms': '10-K, 10-K/A, 10-Q, 144, 144/A, 3, 4, 4/A, 424B5, '
                                                          '5, 8-K, 8-K/A, ARS, DEF 14A, DEFA14A, FWP, NT '
                                                          '10-K, NT 10-Q, S-3ASR, S-8, S-8 POS, SC 13G/A, '
                                                          'SCHEDULE 13G, SD'},
 ('TSLA', '88160R101', 'TESLA INC'): {'ticker': 'TSLA',
                                      'cik': '0001318605',
                                      'sec_name': 'Tesla, Inc.',
                                      'resolution': 'verified',
                                      'evidence': 'https://data.sec.gov/submissions/CIK0001318605.json',
                                      'observed_forms': '10-K, 10-K/A, 10-Q, 144, 3, 4, 4/A, 5, 5/A, 8-K, '
                                                        '8-K/A, ARS, CORRESP, CT ORDER, DEF 14A, DEFA14A, '
                                                        'PRE 14A, PX14A6G, PX14A6N, S-8, SC 13G, SC 13G/A, '
                                                        'SCHEDULE 13G/A, SD, UPLOAD'},
 ('TSM', '874039100', 'TAIWAN SEMICONDUCTOR-SP ADR'): {'ticker': 'TSM',
                                                       'cik': '0001046179',
                                                       'sec_name': 'TAIWAN SEMICONDUCTOR MANUFACTURING CO '
                                                                   'LTD',
                                                       'resolution': 'verified',
                                                       'evidence': 'https://data.sec.gov/submissions/CIK0001046179.json',
                                                       'observed_forms': '20-F, 424B2, 424B5, 6-K, 6-K/A, '
                                                                         'F-3ASR, FWP, S-8, SC 13G, SC '
                                                                         '13G/A, SCHEDULE 13G/A, SD'},
 ('TWST', '90184D100', 'TWIST BIOSCIENCE CORP'): {'ticker': 'TWST',
                                                  'cik': '0001581280',
                                                  'sec_name': 'Twist Bioscience Corp',
                                                  'resolution': 'verified',
                                                  'evidence': 'https://data.sec.gov/submissions/CIK0001581280.json',
                                                  'observed_forms': '10-K, 10-K/A, 10-Q, 144, 144/A, 3, 4, '
                                                                    '4/A, 424B5, 424B7, 8-K, 8-K/A, ARS, DEF '
                                                                    '14A, PRE 14A, S-3ASR, S-8, SC 13G, SC '
                                                                    '13G/A, SCHEDULE 13G, SCHEDULE 13G/A'},
 ('TXG', '88025U109', '10X GENOMICS INC-CLASS A'): {'ticker': 'TXG',
                                                    'cik': '0001770787',
                                                    'sec_name': '10x Genomics, Inc.',
                                                    'resolution': 'verified',
                                                    'evidence': 'https://data.sec.gov/submissions/CIK0001770787.json',
                                                    'observed_forms': '10-K, 10-K/A, 10-Q, 144, 3, 4, 5, '
                                                                      '8-K, DEF 14A, DEFA14A, PRE 14A, S-8, '
                                                                      'SC 13D/A, SC 13G, SC 13G/A, SCHEDULE '
                                                                      '13G, SCHEDULE 13G/A'},
 ('VCYT', '92337F107', 'VERACYTE INC'): {'ticker': 'VCYT',
                                         'cik': '0001384101',
                                         'sec_name': 'VERACYTE, INC.',
                                         'resolution': 'verified',
                                         'evidence': 'https://data.sec.gov/submissions/CIK0001384101.json',
                                         'observed_forms': '10-K, 10-Q, 144, 3, 4, 4/A, 424B5, 424B7, 425, '
                                                           '8-K, 8-K/A, ARS, CORRESP, DEF 14A, DEFA14A, PRE '
                                                           '14A, S-3ASR, S-8, S-8 POS, SC 13G, SC 13G/A, '
                                                           'SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD'},
 ('WGS', '81663L200', 'GENEDX HOLDINGS CORP'): {'ticker': 'WGS',
                                                'cik': '0001818331',
                                                'sec_name': 'GeneDx Holdings Corp.',
                                                'resolution': 'verified',
                                                'evidence': 'https://data.sec.gov/submissions/CIK0001818331.json',
                                                'observed_forms': '10-K, 10-K/A, 10-Q, 144, 144/A, 25-NSE, '
                                                                  '3, 4, 4/A, 424B3, 424B5, 425, 5, 8-K, '
                                                                  '8-K/A, ARS, CORRESP, DEF 14A, DEFA14A, '
                                                                  'DEFM14A, EFFECT, NT 10-Q, POS AM, POS EX, '
                                                                  'PRE 14A, PREM14A, PRER14A, S-1, S-3, '
                                                                  'S-3ASR, S-8, S-8 POS, SC 13D, SC 13D/A, '
                                                                  'SC 13G, SC 13G/A, SCHEDULE 13D/A, '
                                                                  'SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD'},
 ('WRD', '950915108', 'WERIDE INC-ADR'): {'ticker': 'WRD',
                                          'cik': '0001867729',
                                          'sec_name': 'WeRide Inc.',
                                          'resolution': 'verified',
                                          'evidence': 'https://data.sec.gov/submissions/CIK0001867729.json',
                                          'observed_forms': '20-F, 424B4, 424B5, 6-K, 8-A12B, CERT, CORRESP, '
                                                            'DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, '
                                                            'F-3ASR, F-6, FWP, RW, S-8, SC 13D, SCHEDULE '
                                                            '13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SEC STAFF '
                                                            'LETTER, UPLOAD'},
 ('XE', '98386P102', 'X-ENERGY INC'): {'ticker': 'XE',
                                       'cik': '0002088896',
                                       'sec_name': 'X-Energy, Inc.',
                                       'resolution': 'verified',
                                       'evidence': 'https://data.sec.gov/submissions/CIK0002088896.json',
                                       'observed_forms': 'DRS'},
 ('XYZ', '852234103', 'BLOCK INC'): {'ticker': 'XYZ',
                                     'cik': '0001512673',
                                     'sec_name': 'Block, Inc.',
                                     'resolution': 'verified',
                                     'evidence': 'https://data.sec.gov/submissions/CIK0001512673.json',
                                     'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, 4/A, 425, 8-K, 8-K/A, '
                                                       'ARS, CORRESP, D, DEF 14A, DEFA14A, DEFM14A, PREM14A, '
                                                       'PX14A6G, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, '
                                                       'SCHEDULE 13G/A, SD, UPLOAD'},
 ('Z', '98954M200', 'ZILLOW GROUP INC - C'): {'ticker': 'Z',
                                              'cik': '0001617640',
                                              'sec_name': 'ZILLOW GROUP, INC.',
                                              'resolution': 'verified',
                                              'evidence': 'https://data.sec.gov/submissions/CIK0001617640.json',
                                              'observed_forms': '10-K, 10-Q, 144, 144/A, 3, 4, 4/A, 424B5, '
                                                                '5, 8-K, ARS, D, DEF 14A, DEFA14A, S-3ASR, '
                                                                'S-8, SC 13G, SC 13G/A, SCHEDULE 13D/A, '
                                                                'SCHEDULE 13G, SCHEDULE 13G/A'}}

VERIFIED_FILING_COUNTS = {'0000002488': (5, 15),
 '0000018230': (5, 15),
 '0000046619': (5, 15),
 '0000056594': (0, 0),
 '0000059478': (5, 15),
 '0000097210': (5, 15),
 '0000202058': (5, 15),
 '0000315189': (5, 15),
 '0000773840': (5, 15),
 '0000864749': (5, 15),
 '0000874015': (5, 15),
 '0000883241': (5, 15),
 '0000896878': (5, 15),
 '0000936468': (5, 15),
 '0001009001': (0, 0),
 '0001016118': (0, 0),
 '0001018724': (5, 15),
 '0001020214': (5, 15),
 '0001027664': (0, 0),
 '0001035267': (5, 15),
 '0001045810': (5, 15),
 '0001046179': (0, 0),
 '0001065280': (5, 15),
 '0001069258': (5, 15),
 '0001094285': (5, 15),
 '0001099590': (5, 15),
 '0001110803': (5, 15),
 '0001121788': (5, 15),
 '0001181412': (0, 0),
 '0001217234': (5, 15),
 '0001299130': (5, 15),
 '0001315098': (4, 15),
 '0001318605': (5, 15),
 '0001321655': (5, 15),
 '0001326801': (5, 15),
 '0001329099': (0, 0),
 '0001368622': (5, 15),
 '0001384101': (5, 15),
 '0001418819': (5, 15),
 '0001428439': (5, 15),
 '0001445162': (0, 0),
 '0001474432': (5, 15),
 '0001477333': (5, 15),
 '0001478320': (5, 15),
 '0001486957': (5, 15),
 '0001490978': (5, 15),
 '0001493318': (0, 0),
 '0001506293': (5, 15),
 '0001512673': (5, 15),
 '0001527753': (5, 15),
 '0001535527': (5, 15),
 '0001549595': (5, 15),
 '0001555279': (5, 15),
 '0001559720': (5, 15),
 '0001561550': (5, 15),
 '0001571949': (5, 15),
 '0001576280': (5, 15),
 '0001577552': (0, 0),
 '0001579878': (0, 2),
 '0001581280': (5, 15),
 '0001594805': (1, 3),
 '0001601830': (4, 15),
 '0001604821': (5, 15),
 '0001617640': (5, 15),
 '0001633917': (5, 15),
 '0001639920': (0, 0),
 '0001640147': (5, 15),
 '0001650164': (4, 13),
 '0001652044': (5, 15),
 '0001652130': (5, 15),
 '0001653482': (4, 13),
 '0001672688': (4, 14),
 '0001674416': (5, 15),
 '0001679788': (4, 15),
 '0001691493': (0, 0),
 '0001697546': (0, 0),
 '0001703399': (0, 0),
 '0001717115': (1, 5),
 '0001730168': (5, 15),
 '0001745999': (5, 15),
 '0001754581': (0, 0),
 '0001768224': (5, 15),
 '0001769628': (0, 3),
 '0001770787': (5, 15),
 '0001779128': (5, 14),
 '0001783879': (4, 14),
 '0001788707': (0, 0),
 '0001792789': (5, 15),
 '0001804176': (5, 15),
 '0001816431': (5, 15),
 '0001816590': (4, 12),
 '0001818331': (5, 15),
 '0001818874': (5, 15),
 '0001819848': (5, 15),
 '0001819994': (5, 15),
 '0001824502': (5, 15),
 '0001828108': (4, 15),
 '0001829311': (5, 14),
 '0001834489': (0, 0),
 '0001835963': (0, 0),
 '0001837240': (5, 14),
 '0001844452': (4, 13),
 '0001849056': (4, 14),
 '0001853138': (2, 9),
 '0001853921': (0, 0),
 '0001867729': (0, 0),
 '0001872195': (0, 0),
 '0001876042': (0, 2),
 '0001883685': (3, 12),
 '0001884735': (0, 0),
 '0001894562': (3, 10),
 '0001939965': (0, 0),
 '0001943896': (1, 6),
 '0001969302': (0, 0),
 '0001985487': (0, 0),
 '0002003292': (0, 0),
 '0002017526': (1, 5),
 '0002021728': (0, 0),
 '0002088896': (0, 0),
 '0002100782': (0, 0),
 '0002104204': (0, 0)}
