"""Exercise the notebook's actual price functions without network or UI calls."""
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

import numpy as np
import pandas as pd


class PriceTests(unittest.TestCase):
    def setUp(self):
        path = Path(__file__).resolve().parents[1] / "FTSE100_Banking_Analysis_Public_Pilot.ipynb"
        cells = json.loads(path.read_text())["cells"]
        source = next("".join(c["source"]) for c in cells
                      if c["cell_type"] == "code" and "def load_prices(" in "".join(c["source"]))
        self.ticker = Mock()
        self.functions = {"np": np, "pd": pd, "yf": SimpleNamespace(Ticker=self.ticker)}
        exec(source, self.functions)

    def load(self, values, dates=None):
        dates = dates if dates is not None else pd.date_range("2026-01-01", periods=len(values))
        self.ticker.return_value.history.return_value = pd.DataFrame({"Close": values}, index=dates)
        return self.functions["load_prices"]("BARC.L")

    def test_non_finite_missing_and_non_positive_prices_are_removed(self):
        prices = self.load([100, np.inf, -np.inf, np.nan, "bad", 0, -2, 110, 120])
        self.assertEqual(prices.Close.tolist(), [100, 110, 120])
        self.assertTrue(np.isfinite(prices.Close).all())

    def test_too_few_clean_observations_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Not enough"):
            self.load([100, np.inf, 110])

    def test_duplicate_dates_keep_last_quote_and_dates_are_sorted(self):
        dates = pd.to_datetime(["2026-01-03", "2026-01-01", "2026-01-02", "2026-01-02"])
        prices = self.load([120, 100, 105, 110], dates)
        self.assertEqual(prices.Close.tolist(), [100, 110, 120])
        self.assertEqual(len(prices), 3)

    def test_return_and_sample_volatility(self):
        prices = self.load([100, 110, 99])
        result = self.functions["summarise"](prices)
        self.assertEqual(result["Adjusted-close return (%)"], -1.0)
        self.assertEqual(result["Annualised volatility (%)"], 224.5)
        self.assertEqual(result["Observations"], 3)


if __name__ == "__main__":
    unittest.main()
