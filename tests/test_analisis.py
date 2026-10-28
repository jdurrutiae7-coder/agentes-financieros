"""Verifica correcciones estadísticas y protección de configuraciones."""
import json
import shutil
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analisis as app
import numpy as np
import pandas as pd
from src import modelo_curso as model


class ProjectTests(unittest.TestCase):
    def config(self):
        return json.loads((app.ROOT / "config" / "ejemplo.json").read_text(encoding="utf-8"))

    def test_drawdown_captures_loss_on_first_day(self):
        _, summary = model.resumen(np.array([[np.log(0.8), 0.0]]), 100.0)
        self.assertAlmostEqual(summary["drawdown_mediano_en_el_ano"], -0.2)

    def test_no_incomplete_crisis(self):
        dates = pd.bdate_range("2020-02-17", "2020-03-02")
        prices = pd.DataFrame({model.TICKER: np.arange(len(dates)) + 100,
                               model.BENCHMARK: np.arange(len(dates)) + 200}, index=dates)
        self.assertEqual(model.crisis_historicas(prices, 1.0), [])

    def test_kupiec_zero_exceptions_has_nonzero_probability(self):
        dates = pd.bdate_range("2024-01-01", periods=10)
        returns = pd.Series(np.linspace(0.01, 0.02, 10), index=dates)
        g = {"vol_condicional_hist": pd.Series(0.2, index=dates), "nu": 5, "mu_pct": 0}
        result = model.backtest_var(returns, g)
        self.assertEqual(result["excepciones"], 0)
        self.assertGreater(result["p_valor_kupiec"], 0.05)
        self.assertLess(result["p_valor_kupiec"], 1.0)

    def test_create_never_overwrites_company_config(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as temp:
            root = Path(temp)
            (root / "config").mkdir()
            (root / "config" / "ejemplo.json").write_text(json.dumps(self.config()), encoding="utf-8")
            shutil.copytree(app.ROOT / "docs" / "plantillas", root / "docs" / "plantillas")
            with patch.object(app, "ROOT", root):
                config_path = app.create("AAPL", "SPY")
                cfg = json.loads(config_path.read_text(encoding="utf-8"))
                cfg["semilla"] = 99
                app.dump(config_path, cfg)
                (config_path.parent / "Inicio.md").write_text("Mi tesis guardada", encoding="utf-8")
                (config_path.parent / "Bitacora.md").write_text("Mi registro guardado", encoding="utf-8")
                app.create("AAPL", "MSFT")
                saved = json.loads(config_path.read_text(encoding="utf-8"))
                self.assertEqual(saved["semilla"], 99)
                self.assertEqual(saved["benchmark"], "SPY")
                self.assertEqual((config_path.parent / "Inicio.md").read_text(encoding="utf-8"), "Mi tesis guardada")
                self.assertEqual((config_path.parent / "Bitacora.md").read_text(encoding="utf-8"), "Mi registro guardado")

    def test_company_notes_are_separate_and_use_saved_comparator(self):
        cfg = self.config()
        templates = app.ROOT / "docs" / "plantillas"
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as temp:
            root = Path(temp)
            (root / "config").mkdir()
            (root / "config" / "ejemplo.json").write_text(json.dumps(cfg), encoding="utf-8")
            shutil.copytree(templates, root / "docs" / "plantillas")
            with patch.object(app, "ROOT", root):
                first = app.create("AAPL", "SPY").parent
                second = app.create("MSFT", "XLK").parent
                self.assertNotEqual(first, second)
                self.assertIn("`AAPL`", (first / "Inicio.md").read_text(encoding="utf-8"))
                self.assertIn("`XLK`", (second / "Inicio.md").read_text(encoding="utf-8"))
                self.assertNotIn("{{", (second / "Bitacora.md").read_text(encoding="utf-8"))
                self.assertTrue(all((second / stage).is_dir() for stage in app.STAGES))
                # Recuperar solo la nota faltante debe usar XLK, aunque la llamada indique SPY.
                (second / "Inicio.md").unlink()
                app.create("MSFT", "SPY")
                recreated = (second / "Inicio.md").read_text(encoding="utf-8")
                self.assertIn("`XLK`", recreated)
                self.assertNotIn("`SPY`", recreated)

    def test_reject_same_symbol_or_unsafe_path(self):
        cfg = self.config()
        cfg["benchmark"] = cfg["ticker"]
        with self.assertRaises(ValueError):
            app.validate(cfg)
        for bad in ("../AAPL", "C:\\AAPL", "CON", "AAPL SPY"):
            with self.assertRaises(ValueError):
                app.symbol(bad)

    def test_reject_horizon_not_covered_by_tables(self):
        cfg = self.config()
        cfg["horizonte_dias"] = 21
        with self.assertRaises(ValueError):
            app.validate(cfg)


if __name__ == "__main__":
    unittest.main()
