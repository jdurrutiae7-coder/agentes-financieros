"""Crea carpetas y ejecuta el motor cuantitativo del curso sin editar fórmulas."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.metadata
import io
import json
import math
import os
from pathlib import Path
import platform
import re
import sys
from datetime import datetime, timezone
import warnings

ROOT = Path(__file__).resolve().parent
STAGES = ("01_idea", "02_research", "03_cuantitativo", "04_debate")


def symbol(value):
    value = value.strip().upper()
    if not re.fullmatch(r"[A-Z0-9^][A-Z0-9.^=_-]{0,29}", value):
        raise ValueError("Ticker inválido. Usa el símbolo de Yahoo Finance, sin espacios ni rutas.")
    if value.rstrip(".") in {"CON", "PRN", "AUX", "NUL", *[f"COM{i}" for i in range(1, 10)], *[f"LPT{i}" for i in range(1, 10)]}:
        raise ValueError("Este símbolo coincide con un nombre reservado de Windows.")
    return value


def company_dir(ticker):
    # El prefijo evita el significado especial de ^ en algunos comandos de Windows.
    name = "INDICE_" + ticker[1:] if ticker.startswith("^") else ticker
    return ROOT / "empresas" / name


def dump(path, data):
    def clean(item):
        if isinstance(item, dict):
            return {str(k): clean(v) for k, v in item.items()}
        if isinstance(item, list):
            return [clean(v) for v in item]
        if isinstance(item, float) and not math.isfinite(item):
            return None
        return item
    path.write_text(json.dumps(clean(data), ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def create(ticker, benchmark):
    ticker, benchmark = symbol(ticker), symbol(benchmark)
    if ticker == benchmark:
        raise ValueError("La acción y el comparador deben ser distintos.")
    templates = {
        "Inicio.md": (ROOT / "docs" / "plantillas" / "empresa_inicio.md").read_text(encoding="utf-8"),
        "Bitacora.md": (ROOT / "docs" / "plantillas" / "empresa_bitacora.md").read_text(encoding="utf-8"),
    }
    folder = company_dir(ticker)
    for stage in STAGES:
        (folder / stage).mkdir(parents=True, exist_ok=True)
    path = folder / "config.json"
    if not path.exists():
        cfg = json.loads((ROOT / "config" / "ejemplo.json").read_text(encoding="utf-8"))
        cfg.update(ticker=ticker, benchmark=benchmark)
        dump(path, cfg)
        print(f"Creado: {path}")
    else:
        print(f"La empresa ya existe. Su configuración se conserva: {path}")
    saved = json.loads(path.read_text(encoding="utf-8"))
    for name, template in templates.items():
        note = folder / name
        if not note.exists():
            # Usar el comparador guardado: una segunda llamada no cambia la empresa.
            content = template.replace("{{TICKER}}", ticker).replace("{{BENCHMARK}}", saved["benchmark"])
            note.write_text(content, encoding="utf-8")
            print(f"Nota de entrada creada: {note}")
    return path


def validate(cfg):
    cfg = dict(cfg)
    cfg["ticker"], cfg["benchmark"] = symbol(cfg["ticker"]), symbol(cfg["benchmark"])
    if cfg["ticker"] == cfg["benchmark"]:
        raise ValueError("La acción y el comparador deben ser distintos.")
    for key in ("anos_modelo", "anos_backtest", "horizonte_dias", "simulaciones", "semilla"):
        if isinstance(cfg[key], bool) or not isinstance(cfg[key], int):
            raise ValueError(f"{key} debe ser un entero.")
    if cfg["anos_modelo"] < 3 or not 1 <= cfg["anos_backtest"] <= cfg["anos_modelo"]:
        raise ValueError("Se requieren al menos 3 años de modelo y un backtest dentro de esa ventana.")
    if cfg["horizonte_dias"] != 252:
        raise ValueError("Esta versión conserva el horizonte de 252 días del curso; sus tablas comparan un año.")
    if cfg["simulaciones"] <= 0 or cfg["semilla"] < 0:
        raise ValueError("Las simulaciones deben ser positivas y la semilla no negativa.")
    if not isinstance(cfg["tasa_libre_riesgo"], (int, float)) or not math.isfinite(cfg["tasa_libre_riesgo"]) or cfg["tasa_libre_riesgo"] <= -1:
        raise ValueError("La tasa debe ser un decimal finito mayor que -1; 0.04 significa 4%.")
    if cfg["deriva"] not in {"libre_de_riesgo", "historico"}:
        raise ValueError("Deriva desconocida.")
    if not cfg.get("moneda"):
        raise ValueError("Falta la moneda de comparación.")
    return cfg


@contextlib.contextmanager
def inside(path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def handoff(result, cfg, mode, period, notices):
    p = lambda x: "n/d" if x is None else f"{x:.2%}"
    a, b = (result["backtest"][cfg[k]] for k in ("ticker", "benchmark"))
    mc, g = result["montecarlo"]["garch_t"], result["regimen"]
    v = result["validacion_var"]
    iv = g.get("vol_implicita")
    crisis = result["crisis"]
    missing = "; ".join(notices) or "Sin avisos adicionales de ejecución."
    return (
        f"## FICHA DE TRASPASO: SKILL 03\n\n"
        f"- Ticker: {cfg['ticker']} · Comparador: {cfg['benchmark']} · Moneda declarada: {cfg['moneda']}\n"
        f"- Modo: {mode}. " + ("DATOS SINTÉTICOS, NO USAR PARA INVERSIÓN.\n" if mode == "DEMO" else "Datos históricos de Yahoo Finance.\n") +
        f"- Período del modelo: {result['datos_modelo'][0]} a {result['datos_modelo'][1]}\n"
        f"- Período efectivo de backtest: {period['desde']} a {period['hasta']}, {period['observaciones']} precios\n"
        f"- Semilla: {cfg['semilla']} · Deriva: {cfg['deriva']} · Tasa: {p(cfg['tasa_libre_riesgo'])}\n"
        f"- Fuente de la tasa: {cfg.get('tasa_fuente')} · Fecha: {cfg.get('tasa_fecha') or 'no verificada'}\n"
        f"- CAGR: {p(a['cagr'])} vs. {p(b['cagr'])} · Volatilidad: {p(a['volatilidad_anual'])} vs. {p(b['volatilidad_anual'])}\n"
        f"- Sharpe: {a['sharpe']:.3f} · Máximo drawdown: {p(a['max_drawdown'])}, de {a['max_drawdown_inicio']} a {a['max_drawdown_fondo']}\n"
        f"- Régimen: volatilidad próxima sesión anualizada {p(g['vol_hoy'])}, percentil {g['percentil_hoy']:.2f} · Largo plazo {p(g['vol_largo_plazo'])}\n"
        f"- Opciones, captura guardada: {json.dumps(iv, ensure_ascii=False) if iv else 'no disponible'}\n"
        f"- Monte Carlo a 252 días: P5 {mc['p5']:.2f}, mediana {mc['mediana']:.2f}, P95 {mc['p95']:.2f} · Probabilidad simulada de caer 20% en el camino {p(mc['prob_caer_20pct_en_algun_momento'])} · CVaR 95% {p(mc['cvar_95'])}\n"
        f"- Beta frente al comparador: {result['factor']['beta']:.3f} · R²: {p(result['factor']['r2'])}\n"
        f"- Escenarios condicionales: ver resultados JSON y resumen.\n"
        f"- Ventanas de crisis completas disponibles: {len(crisis)}. Ver tabla en resumen.\n"
        f"- VaR: excepciones {p(v['tasa'])} · Kupiec p = {v['p_valor_kupiec']:.4f}. Prueba dentro de muestra.\n"
        f"- Avisos: {missing}\n"
        "- Limitaciones: probabilidades condicionadas al modelo y sus supuestos; no son predicciones ni precios objetivo.\n"
    )


def execute(args):
    replay = Path(args.repetir).resolve() if args.repetir else None
    if replay:
        cfgpath = replay / "config.json"
        old_manifest = json.loads((replay / "manifest.json").read_text(encoding="utf-8"))
        mode_demo = old_manifest["modo"] == "DEMO"
    else:
        cfgpath = Path(args.config).resolve() if args.config else company_dir(symbol(args.empresa)) / "config.json"
        mode_demo = args.demo
    cfg = json.loads(cfgpath.read_text(encoding="utf-8"))
    if args.benchmark:
        cfg["benchmark"] = args.benchmark
    cfg = validate(cfg)
    # Esta importación se retrasa: crear carpetas y ver ayuda no requieren librerías externas.
    os.environ.setdefault("MPLBACKEND", "Agg")
    from src import modelo_curso as model
    import numpy as np
    import pandas as pd

    values = {"TICKER": "ticker", "BENCHMARK": "benchmark", "ANOS_MODELO": "anos_modelo",
              "ANOS_BACKTEST": "anos_backtest", "HORIZONTE_DIAS": "horizonte_dias",
              "N_SIMULACIONES": "simulaciones", "SEMILLA": "semilla",
              "TASA_LIBRE_RIESGO": "tasa_libre_riesgo", "DERIVA": "deriva"}
    for attribute, key in values.items():
        setattr(model, attribute, cfg[key])
    model.MODO_DEMO = mode_demo
    model.FUENTE_DATOS = "Datos sintéticos DEMO" if mode_demo else "Yahoo Finance, cierre ajustado por dividendos y splits"
    notices = []
    if not cfg.get("tasa_fecha"):
        notices.append("La tasa libre de riesgo es un supuesto sin fecha vigente verificada.")
    captured = {"options": None, "prices": None, "currencies": {}}

    if replay:
        if args.benchmark or args.demo:
            raise ValueError("Para reproducir una corrida conserva su configuración y modo; no uses --benchmark o --demo.")
        prices_path = replay / old_manifest["precios_archivo"]
        if sha(prices_path) != old_manifest["precios_sha256"]:
            raise ValueError("El CSV guardado cambió: su huella no coincide con el manifiesto.")
        if sha(cfgpath) != old_manifest["config_sha256"]:
            raise ValueError("La configuración guardada cambió: su huella no coincide.")
        option_path = replay / "opciones.json"
        if sha(option_path) != old_manifest["opciones_sha256"]:
            raise ValueError("La captura de opciones cambió: su huella no coincide.")
        saved_prices = pd.read_csv(prices_path, index_col=0, parse_dates=True, float_precision="round_trip")
        saved_options = json.loads(option_path.read_text(encoding="utf-8"))
        captured["currencies"] = old_manifest.get("monedas_verificadas", {})
        if old_manifest["motor_sha256"] != sha(ROOT / "src" / "modelo_curso.py"):
            notices.append("El motor cambió desde la corrida original; no se garantiza igualdad numérica.")
        model.descargar_precios = lambda: saved_prices.copy()
        model.precios_demo = lambda: saved_prices.copy()
        model.volatilidad_implicita = lambda: saved_options
    original_download = model.descargar_precios
    original_demo = model.precios_demo
    original_options = model.volatilidad_implicita

    def prices_checked(demo=False):
        frame = (original_demo() if demo else original_download()).copy()
        required = [cfg["ticker"], cfg["benchmark"]]
        if any(t not in frame for t in required):
            raise ValueError("Faltan columnas del ticker o comparador en los precios descargados.")
        frame = frame[required].dropna().sort_index()
        if frame.index.has_duplicates or not np.isfinite(frame.to_numpy()).all() or (frame <= 0).any().any():
            raise ValueError("Precios no válidos: fechas duplicadas, valores infinitos o precios no positivos.")
        if len(frame) < 3 * 252:
            raise ValueError("No hay al menos 3 años de observaciones comunes.")
        if len(frame) < cfg["anos_backtest"] * 252:
            notices.append("La cobertura es menor que el backtest solicitado; leer el período efectivo.")
        if not demo and not replay:
            import yfinance as yf
            for ticker in required:
                currency = yf.Ticker(ticker).fast_info["currency"]
                if not currency:
                    raise ValueError(f"No se pudo verificar la moneda de {ticker}.")
                captured["currencies"][ticker] = currency
            if set(captured["currencies"].values()) != {cfg["moneda"]}:
                raise ValueError("Las monedas observadas difieren entre sí o de config.json; falta una conversión explícita.")
        captured["prices"] = frame
        return frame

    def options_checked():
        captured["options"] = original_options()
        return captured["options"]

    model.descargar_precios = prices_checked
    model.precios_demo = lambda: prices_checked(demo=True)
    model.volatilidad_implicita = options_checked
    mode = "DEMO" if mode_demo else "REAL"
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S_%f")
    comparator = cfg["benchmark"].replace("^", "INDICE_")
    folder = company_dir(cfg["ticker"]) / "03_cuantitativo" / f"{stamp}_{comparator}_{mode}"
    folder.mkdir(parents=True, exist_ok=False)
    dump(folder / "config.json", cfg)
    stream = io.StringIO()
    try:
        with inside(folder), contextlib.redirect_stdout(stream), warnings.catch_warnings(record=True) as recorded:
            warnings.simplefilter("always")
            model.main()
        notices.extend(dict.fromkeys(str(item.message) for item in recorded))
        result_path = next(folder.glob("*_resultados.json"))
        prices_path = next(folder.glob("*_precios.csv"))
        result = json.loads(result_path.read_text(encoding="utf-8"))
        prices = captured["prices"]
        bt = prices.iloc[-cfg["anos_backtest"] * 252:]
        period = {"desde": str(bt.index[0].date()), "hasta": str(bt.index[-1].date()), "observaciones": len(bt)}
        versions = {package: importlib.metadata.version(package) for package in ("numpy", "pandas", "matplotlib", "scipy", "arch", "statsmodels")}
        if not mode_demo:
            versions["yfinance"] = importlib.metadata.version("yfinance")
        if replay and versions != old_manifest["versiones"]:
            notices.append("Las versiones difieren de la corrida original; no se garantiza igualdad numérica.")
        if replay and platform.python_version() != old_manifest["python"]:
            notices.append("La versión de Python difiere de la corrida original.")
        dump(folder / "opciones.json", captured["options"])
        manifest = {"modo": mode, "fuente": model.FUENTE_DATOS, "creado_utc": datetime.now(timezone.utc).isoformat(),
                    "repetida_desde": str(replay) if replay else None, "python": platform.python_version(),
                    "versiones": versions, "motor_sha256": sha(ROOT / "src" / "modelo_curso.py"),
                    "ejecutor_sha256": sha(Path(__file__)), "config_sha256": sha(folder / "config.json"),
                    "precios_archivo": prices_path.name, "precios_sha256": sha(prices_path),
                    "opciones_sha256": sha(folder / "opciones.json"), "monedas_verificadas": captured["currencies"],
                    "backtest_efectivo": period, "avisos": notices}
        result["auditoria"] = manifest
        dump(result_path, result)
        dump(folder / "manifest.json", manifest)
        preamble = f"# Corrida {mode}: {cfg['ticker']} vs. {cfg['benchmark']}\n\n"
        preamble += f"Backtest efectivo: {period['desde']} a {period['hasta']}, {period['observaciones']} precios.\n\n"
        preamble += "Supuestos y avisos:\n\n" + "\n".join("- " + x for x in notices) + "\n\n"
        if mode_demo:
            preamble += "**Toda esta corrida usa datos sintéticos. Ninguna cifra describe a una empresa real.**\n\n"
        (folder / "resumen.md").write_text(preamble + stream.getvalue(), encoding="utf-8")
        (folder / "ficha_03.md").write_text(handoff(result, cfg, mode, period, notices), encoding="utf-8")
        (folder / "dependencias.txt").write_text("\n".join(f"{k}=={v}" for k, v in versions.items()) + "\n", encoding="utf-8")
        print(f"Corrida {mode} terminada. Ver resumen.md, ficha_03.md, gráficos y manifest.json.")
        print(folder)
        return folder
    except BaseException as exc:
        (folder / "ERROR.txt").write_text(str(exc) + "\n\n" + stream.getvalue(), encoding="utf-8")
        raise


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    new = sub.add_parser("crear", help="Crea carpeta y config de una empresa sin sobrescribir la existente.")
    new.add_argument("--ticker")
    new.add_argument("--benchmark")
    run = sub.add_parser("ejecutar", help="Ejecuta el análisis con parámetros de un archivo.")
    group = run.add_mutually_exclusive_group(required=True)
    group.add_argument("--empresa")
    group.add_argument("--config")
    group.add_argument("--repetir", help="Carpeta de una corrida para reutilizar precios y opciones.")
    run.add_argument("--benchmark", help="Comparador para esta corrida, sin modificar la configuración guardada.")
    run.add_argument("--demo", action="store_true", help="Datos sintéticos; no descarga información bursátil.")
    args = parser.parse_args()
    try:
        if args.command == "crear":
            create(args.ticker or input("Ticker de la empresa: "), args.benchmark or input("Comparador [SPY]: ").strip() or "SPY")
        else:
            execute(args)
    except (ValueError, KeyError, FileNotFoundError, ImportError) as exc:
        print(f"No se completó: {exc}", file=sys.stderr)
        print("Revisa README.md: carpeta, configuración y librerías del entorno .venv.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
