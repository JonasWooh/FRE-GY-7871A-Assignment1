import importlib.util
from pathlib import Path

import pandas as pd

spec = importlib.util.spec_from_file_location("market_script", Path(__file__).parents[1] / "scripts/03_get_market_data.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_exact_accession_latest_date_and_conflict_exclusion():
    facts = [
        {"accn": "A", "end": "2023-01-01", "val": 100},
        {"accn": "A", "end": "2022-01-01", "val": 90},
        {"accn": "A", "end": "2024-01-01", "val": 200},
        {"accn": "B", "end": "2023-01-01", "val": 300},
        {"accn": "B", "end": "2023-01-01", "val": 400},
    ]

    class Response:
        def json(self):
            return {"facts": {"dei": {"EntityCommonStockSharesOutstanding": {"units": {"shares": facts}}}}}

    class Client:
        def _get(self, url):
            return Response()

    meta = pd.DataFrame({"cik": ["0000000001"] * 4, "accession": ["A", "B", "C", "A"],
                         "filing_date": ["2023-02-01"] * 4})
    result = module.get_shares(Client(), meta)
    assert result["accession"].tolist() == ["A"]
    assert result["shares_outstanding"].tolist() == [100]
