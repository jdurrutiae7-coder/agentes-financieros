# Corrida REAL: AAPL vs. SPY

Backtest efectivo: 2021-10-18 a 2026-10-23, 1260 precios.

Supuestos y avisos:

- La tasa libre de riesgo es un supuesto sin fecha vigente verificada.
- The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
- The inplace keyword in DataFrame.set_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
- The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
- The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.

## RESULTADOS CUANTITATIVOS v2 : AAPL vs SPY
Fuente: Yahoo Finance, cierre ajustado por dividendos y splits · Modelos calibrados con 2016-10-25 a 2026-10-23 · Semilla 42 · Deriva: libre_de_riesgo

### 1. Backtest (5 años)

| Métrica | AAPL | SPY |
|---|---|---|
| CAGR | 19.5% | 12.7% |
| Volatilidad anual | 27.9% | 17.1% |
| Máx. drawdown | -33.4% | -24.5% |
| Sharpe | 0.63 | 0.55 |
| Sortino | 0.91 | 0.76 |

Máx. drawdown de AAPL entre 2024-12-26 y 2025-04-08.

### 2. Régimen de volatilidad

- Volatilidad de hoy (GARCH): **18.7%** anualizada → percentil 12 de los últimos 10 años (0 = la más baja, 100 = la más alta).
- Nivel de largo plazo al que tiende: 31.7% · Persistencia: 0.975 (cercana a 1 = los shocks de volatilidad duran mucho).
- Asimetría: las caídas suben la volatilidad más que las alzas (gamma = 0.135). Colas: t-Student con 4.5 grados de libertad (menos = colas más gordas).
- Volatilidad implícita en opciones (28 días, venc. 2026-11-20): 28.0% vs. modelo 22.5% → la volatilidad cotizada en opciones es MÁS riesgo que la volatilidad del modelo histórico.
- Volatilidad implícita en opciones (329 días, venc. 2027-09-17): 27.8% vs. modelo 33.4% → la volatilidad cotizada en opciones es MENOS riesgo que la volatilidad del modelo histórico.

### 3. Monte Carlo a 252 días hábiles · precio inicial 347.73

| Modelo | P5 | Mediana | P95 | VaR 95% | CVaR 95% | Prob. caer 20% en algún momento | Prob. subir 20% en algún momento | Drawdown mediano en el año |
|---|---|---|---|---|---|---|---|---|
| GARCH-t (régimen actual) | 208.64 | 353.76 | 520.57 | -40.0% | -51.7% | 38.8% | 44.0% | -23.8% |
| Volatilidad constante | 217.25 | 345.17 | 561.82 | -37.5% | -44.5% | 43.2% | 49.8% | -27.1% |

### 4. Mercado vs. empresa

- Beta: 1.20 · El comparador se asocia con el 55% de la variación diaria; el 45% restante no lo explica este modelo de un factor (vol. idiosincrática 19.6%).

| Escenario a 1 año | Frecuencia simulada | Mediana de AAPL | P5 | P95 |
|---|---|---|---|---|
| Benchmark cae más de 15% | 10% | -30.5% | -62.5% | -1.0% |
| Benchmark cae 0–15% | 27% | -9.4% | -37.0% | 26.5% |
| Benchmark sube 0–15% | 43% | 5.8% | -25.6% | 47.8% |
| Benchmark sube más de 15% | 20% | 22.9% | -12.8% | 76.2% |

### 5. Crisis reales (del máximo al mínimo del S&P 500)

| Crisis | SPY | AAPL real | AAPL según su beta |
|---|---|---|---|
| Venta masiva Q4 2018 (2018-09-20 a 2018-12-24) | -19.3% | -33.0% | -23.2% |
| COVID 2020 (2020-02-19 a 2020-03-23) | -33.7% | -30.7% | -40.3% |
| Alza de tasas 2022 (2022-01-03 a 2022-10-12) | -24.5% | -23.7% | -29.3% |
| Shock arancelario 2025 (2025-02-19 a 2025-04-08) | -18.8% | -29.6% | -22.4% |

### 6. Validación del modelo (VaR diario 95%)

- En 2,513 días, la pérdida superó el VaR del modelo GARCH-t en 5.5% de los días (lo esperado es 5,0%). Test de Kupiec: p = 0.27 (no se rechaza la cobertura dentro de muestra).
- Un modelo de volatilidad constante con distribución normal falla en 4.7% de los días.
- Nota: los parámetros se estiman con toda la muestra, así que es una validación dentro de muestra.

Archivos: AAPL_2026-10-23_1_crecimiento.png, AAPL_2026-10-23_2_drawdown.png, AAPL_2026-10-23_3_regimen_volatilidad.png, AAPL_2026-10-23_4_montecarlo.png, AAPL_2026-10-23_5_escenarios_condicionales.png, AAPL_2026-10-23_6_crisis.png, AAPL_2026-10-23_resultados.json, AAPL_2026-10-23_precios.csv

Ninguna simulación predice la dirección del precio. Cuantifica riesgo bajo supuestos explícitos. No es una recomendación.
