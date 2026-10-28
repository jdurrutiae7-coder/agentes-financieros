## FICHA DE TRASPASO: SKILL 03

- Ticker: AAPL · Comparador: XLK · Moneda declarada: USD
- Modo: REAL. Datos históricos de Yahoo Finance.
- Período del modelo: 2016-10-25 a 2026-10-23
- Período efectivo de backtest: 2021-10-18 a 2026-10-23, 1260 precios
- Semilla: 42 · Deriva: libre_de_riesgo · Tasa: 4.00%
- Fuente de la tasa: Supuesto del profesor, no verificado como tasa vigente · Fecha: no verificada
- CAGR: 19.48% vs. 19.34% · Volatilidad: 27.90% vs. 25.96%
- Sharpe: 0.632 · Máximo drawdown: -33.36%, de 2024-12-26 a 2025-04-08
- Régimen: volatilidad próxima sesión anualizada 18.65%, percentil 11.74 · Largo plazo 31.73%
- Opciones, captura guardada: {"1_mes": {"vencimiento": "2026-11-20", "dias": 28, "iv": 0.27973132385253907}, "1_ano": {"vencimiento": "2027-09-17", "dias": 329, "iv": 0.27849155963897704}}
- Monte Carlo a 252 días: P5 208.64, mediana 353.76, P95 520.56 · Probabilidad simulada de caer 20% en el camino 38.80% · CVaR 95% -51.74%
- Beta frente al comparador: 0.888 · R²: 58.69%
- Escenarios condicionales: ver resultados JSON y resumen.
- Ventanas de crisis completas disponibles: 4. Ver tabla en resumen.
- VaR: excepciones 5.49% · Kupiec p = 0.2655. Prueba dentro de muestra.
- Avisos: La tasa libre de riesgo es un supuesto sin fecha vigente verificada.; The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.; The inplace keyword in DataFrame.set_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.; The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.; The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
- Limitaciones: probabilidades condicionadas al modelo y sus supuestos; no son predicciones ni precios objetivo.
