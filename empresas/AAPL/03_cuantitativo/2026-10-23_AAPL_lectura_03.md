# Apple | Análisis cuantitativo real | Skill 03

Corte: 2026-10-23. Seis tablas y seis gráficos. Comparador principal SPY; sensibilidad XLK.

## 1. Rendimiento y caídas: AAPL frente a SPY y XLK

Datos reales de Yahoo Finance, ajustados por dividendos y splits. Corte: 2026-10-23. Backtest efectivo: 2021-10-18 a 2026-10-23, 1260 precios, aproximadamente cinco años bursátiles. Se usa 252 sesiones por año, no años calendario exactos. Sin costos, impuestos ni conversión a pesos chilenos.

| Métrica anualizada o acumulada | AAPL | SPY | XLK |
| --- | --- | --- | --- |
| CAGR: retorno anual compuesto | 19,5% | 12,7% | 19,3% |
| Volatilidad anual | 27,9% | 17,1% | 26,0% |
| Sharpe, tasa constante 4,0% | 0,63 | 0,55 | 0,66 |
| Sortino, variante del curso | 0,91 | 0,76 | 0,97 |
| Máximo drawdown | -33,4% | -24,5% | -33,6% |

Lectura: AAPL rindió más que SPY en esta ventana, con más volatilidad y mayor caída máxima. Frente a XLK, la diferencia de CAGR es pequeña y el Sharpe de Apple (0,63) queda por debajo del sector (0,66). Opinión: el resultado histórico no muestra una ventaja clara de Apple por unidad de riesgo frente a XLK.

![Gráfico 1. Crecimiento de una base común. La comparación principal del gráfico es SPY.](2026-10-23_230246_610362_SPY_REAL/AAPL_2026-10-23_1_crecimiento.png)

Gráfico 1. Crecimiento de una base común. La comparación principal del gráfico es SPY.

![Gráfico 2. Caída desde el máximo previo. El peor tramo de AAPL fue 2024-12-26 a 2025-04-08.](2026-10-23_230246_610362_SPY_REAL/AAPL_2026-10-23_2_drawdown.png)

Gráfico 2. Caída desde el máximo previo. El peor tramo de AAPL fue 2024-12-26 a 2025-04-08.

Sharpe compara el exceso de retorno simple contra una tasa fija con la volatilidad. Se aplicó 4% a toda la ventana, no una serie histórica de tasas. Sortino usa la desviación estándar de los retornos negativos del curso, una variante que no debe compararse sin ajuste con otros proveedores.

## 2. Régimen de volatilidad: calma reciente, riesgo latente

GJR-GARCH con innovaciones t, calibrado con retornos desde 2016-10-25 a 2026-10-23. La dispersión estimada para la próxima sesión es 18,7% anualizada, en el percentil 11,7 de su historia condicional.

| Indicador de AAPL | Resultado | Cómo leerlo |
| --- | --- | --- |
| Próxima sesión, anualizada | 18,7% | Predicción de dispersión, no de dirección |
| Percentil histórico | 11,7 | Escala 0 a 100 de volatilidades condicionales |
| Largo plazo del modelo | 31,7% | Nivel estacionario estimado, no techo |
| Persistencia | 0,975 | Los shocks tardan en disiparse |
| Asimetría gamma | 0,135 | Caídas elevan más la varianza estimada |
| Grados de libertad t | 4,53 | Colas más pesadas que una normal |
| Opción cercana a un mes | 28,0% | Vence 2026-11-20, 28 días calendario; modelo aprox. 22,5% |
| Opción cercana a un año | 27,8% | Vence 2027-09-17, 329 días calendario; modelo aprox. 33,4% |

![Gráfico 3. Serie condicional histórica. El punto «Hoy» del gráfico es la última sesión ajustada; la tabla distingue la proyección de la próxima sesión.](2026-10-23_230246_610362_SPY_REAL/AAPL_2026-10-23_3_regimen_volatilidad.png)

Gráfico 3. Serie condicional histórica. El punto «Hoy» del gráfico es la última sesión ajustada; la tabla distingue la proyección de la próxima sesión.

Lectura: el régimen actual está en la zona baja de su historia. Eso no indica que la acción deba subir ni que no pueda caer. La persistencia cercana a uno y gamma positivo describen agrupación de volatilidad y mayor reacción ante shocks negativos dentro del modelo.

Opciones: captura guardada, promedio de volatilidades implícitas de calls y puts cercanos al spot. No es una superficie completa ni un filtro de liquidez. La volatilidad implícita y la histórica se miden de forma distinta; su diferencia puede incluir prima de riesgo y calidad de cotizaciones, sin identificar un evento concreto.

Horizontes: los vencimientos son días calendario; la simulación usa días bursátiles. El punto de un año de opciones disponible vence antes del año completo y la comparación con el modelo es aproximada, sin interpolación. No se toma esa brecha como una señal de inversión.

## 3. Monte Carlo: escenarios de pérdida y trayectoria

Se ejecutaron 10.000 caminos a 252 sesiones, con semilla 42. Nivel inicial de cierre ajustado: USD 347,73. Deriva «libre_de_riesgo» con tasa anual fija de 4,0%. La dirección que aparece en las medianas depende del supuesto de deriva.

| Resultado al horizonte, salvo indicación | GARCH-t | Volatilidad constante |
| --- | --- | --- |
| Nivel terminal P5, escala de cierre ajustado USD | 208,64 | 217,25 |
| Nivel terminal mediano, misma escala | 353,76 | 345,17 |
| Nivel terminal P95, misma escala | 520,57 | 561,82 |
| Retorno percentil 5, VaR con signo | -40,0% | -37,5% |
| Retorno medio del peor 5%, CVaR con signo | -51,7% | -44,5% |
| Frecuencia de bajar 20% desde el inicio en algún día | 38,8% | 43,2% |
| Frecuencia de pérdida al final | 47,4% | 51,0% |
| Máximo drawdown mediano dentro del camino | -23,8% | -27,1% |

![Gráfico 4. Abanicos simulados. Percentiles y medianas son resultados del modelo; no son precios objetivo ni probabilidades garantizadas.](2026-10-23_230246_610362_SPY_REAL/AAPL_2026-10-23_4_montecarlo.png)

Gráfico 4. Abanicos simulados. Percentiles y medianas son resultados del modelo; no son precios objetivo ni probabilidades garantizadas.

Lectura: 38,8% de los caminos GARCH-t bajó al menos 20% desde el valor inicial en algún día. Esto es distinto del máximo drawdown, que mide la caída desde cualquier máximo alcanzado durante el camino. El CVaR de -51,7% es el retorno terminal promedio del peor 5%, no una pérdida máxima posible.

GARCH parte de una volatilidad reciente baja y la deja cambiar; el modelo simple usa volatilidad histórica constante. Aunque GARCH genera menos caminos que cruzan el umbral de caída, sus peores retornos terminales son más severos en esta corrida. La distribución de cola importa, además de la volatilidad inicial.

## 4. Mercado y empresa: asociación y escenarios conjuntos

Beta frente a SPY: 1,20. R² diario: 54,7%; volatilidad residual anual: 19,6%. Es una regresión de retornos diarios en toda la muestra. R² describe asociación en este modelo de un factor, no causalidad ni el porcentaje de todo el riesgo que «pertenece» al mercado.

| SPY al final de un año simulado | Frecuencia | Mediana AAPL | P5 AAPL | P95 AAPL |
| --- | --- | --- | --- | --- |
| SPY cae más de 15% | 9,5% | -30,5% | -62,5% | -1,0% |
| SPY cae 0-15% | 27,1% | -9,4% | -37,0% | 26,5% |
| SPY sube 0-15% | 43,0% | 5,8% | -25,6% | 47,8% |
| SPY sube más de 15% | 20,3% | 22,9% | -12,8% | 76,2% |

![Gráfico 5. Escenarios conjuntos a un año: benchmark GARCH y residuo de Apple remuestreado en bloques. No son el mismo experimento que el Monte Carlo univariado de la página anterior.](2026-10-23_230246_610362_SPY_REAL/AAPL_2026-10-23_5_escenarios_condicionales.png)

Gráfico 5. Escenarios conjuntos a un año: benchmark GARCH y residuo de Apple remuestreado en bloques. No son el mismo experimento que el Monte Carlo univariado de la página anterior.

Si SPY termina con una caída superior a 15%, la mediana condicional de AAPL es -30,5%; ese escenario aparece en 9,5% de las simulaciones. La condición se refiere al retorno final de SPY, no a haber tocado ese nivel durante el año.

Sensibilidad con XLK: beta 0,89, R² 58,7% y mediana de AAPL -27,8% cuando XLK termina cayendo más de 15%. Sus betas usan comparadores distintos y no se ordenan como una escala universal de riesgo. Ambos ETF incluyen Apple y XLK mezcla hardware, software y semiconductores.

## 5. Ventanas de crisis: qué ocurrió en precios

Estas fechas se heredan del curso y se presentan como ventanas fijas. No se afirma que sean los máximos y mínimos exactos de AAPL, SPY o XLK. Cada fila usa los mismos extremos de fecha para acción y benchmark. La crisis de 2008 queda fuera de los datos disponibles.

| Ventana del curso | SPY | AAPL | Beta x SPY, referencia |
| --- | --- | --- | --- |
| Venta masiva Q4 2018<br>2018-09-20 a 2018-12-24 | -19,3% | -33,0% | -23,2% |
| COVID 2020<br>2020-02-19 a 2020-03-23 | -33,7% | -30,7% | -40,3% |
| Alza de tasas 2022<br>2022-01-03 a 2022-10-12 | -24,5% | -23,7% | -29,3% |
| Shock arancelario 2025<br>2025-02-19 a 2025-04-08 | -18,8% | -29,6% | -22,4% |

![Gráfico 6. Retornos en las ventanas del curso. La referencia «máximo al mínimo» del título original identifica las ventanas docentes; no verifica extremos exactos de cada instrumento.](2026-10-23_230246_610362_SPY_REAL/AAPL_2026-10-23_6_crisis.png)

Gráfico 6. Retornos en las ventanas del curso. La referencia «máximo al mínimo» del título original identifica las ventanas docentes; no verifica extremos exactos de cada instrumento.

En la ventana arancelaria de 2025, AAPL cayó -29,6% frente a -18,8% de SPY. Beta x SPY habría dado -22,4%, pero la beta se estimó después con toda la muestra: es una referencia retrospectiva, no una predicción que existía antes del evento.

Conexión con el research: el desempeño de precios hace relevante examinar exposición de suministro y aranceles. La diferencia frente a beta no demuestra que toda la caída adicional haya sido causada por esos factores. Noticias y resultados concretos requieren evidencia fundamental aparte.

La experiencia no fue uniforme: en COVID y en la ventana de tasas de 2022 Apple cayó menos que SPY. Por eso, una sola beta o una sola crisis no basta para anticipar cómo se comportará en la próxima caída.

## 6. Validación, límites y traspaso al debate

| Control | Resultado observado | Alcance |
| --- | --- | --- |
| Días de retornos en calibración | 2513 | Toda la muestra; no hay holdout |
| Excepciones VaR diario 95% | 138 / 2513 = 5,49% | Referencia nominal 5,0% |
| Kupiec, p-valor | 0,2655 | No se rechaza cobertura al umbral 0,05 |
| Excepciones con volatilidad normal constante | 4,74% | Frecuencia cercana al nominal no prueba superioridad |
| GARCH: convergencia y estacionariedad | Convergió; persistencia 0,975 | El ejecutor se detiene si fallan estos requisitos |
| Repetición de SPY con precios y opciones guardados | Resultados numéricos exactamente iguales | Sin nueva descarga; misma configuración y entorno |
| Monedas y huellas | USD en todos los instrumentos; SHA-256 verificados | No se mezclaron monedas ni datos DEMO |

Lectura: 5,49% de excepciones y p = 0,2655 no permiten rechazar la cobertura nominal en esta muestra. No demuestran independencia entre excepciones, estabilidad futura, severidad de cola correcta ni capacidad predictiva fuera de muestra. El modelo normal también tiene una frecuencia cercana a 5%; este control no prueba que GARCH sea superior.

Opinión para el debate: la rentabilidad histórica de Apple fue mayor que la del mercado amplio, con más riesgo; la comparación sectorial reduce la impresión de excepcionalidad. La calma reciente contrasta con colas simuladas severas. El research sigue siendo necesario para decidir si Servicios, márgenes y regulación sostienen el negocio; este modelo no estima valor intrínseco.

## Supuestos y límites que acompañan los resultados

La simulación cuantifica riesgo bajo supuestos; no predice dirección. La deriva es el supuesto más débil: «libre_de_riesgo» conserva la fórmula docente y no equivale a una medida neutral al riesgo exacta bajo GARCH-t. Se mantienen diez años de calibración, cinco de backtest, 252 sesiones de horizonte, 10.000 simulaciones, semilla 42 y tasa 4%.

Referencia consultada: FRED DTB3 del 22.oct.2026 = 4,04%, publicada el 23.oct.2026. Es una cotización anual sobre base de descuento; no se convierte ni sustituye por una tasa efectiva en el motor. El 4% usado sigue siendo un supuesto docente, no una rentabilidad futura asegurada.

Diez años no abarcan todas las crisis; no incluyen 2008. Los parámetros se ajustaron dentro de muestra. El motor no conoce próximos resultados, competencia, deuda o cambios regulatorios. Los precios ajustados incorporan dividendos y splits según Yahoo y pueden revisarse; se congelaron CSV y opciones de cada corrida. No se incorporan costos, impuestos, impacto de ejecución ni CLP/USD.

Integridad: las dos descargas de AAPL tienen diferencias submilésimas de USD por ajuste/redondeo del proveedor; no cambian las métricas de backtest a la precisión presentada. La lectura principal usa exclusivamente la captura SPY identificada. Los avisos de deprecación de pandas se conservan en los manifiestos y no impidieron la ejecución.

## Archivos para continuar

La ficha 03 consolidada contiene cifras, fuentes, supuestos y pendientes para la skill 04. El paquete reproducible incluye las dos corridas, captura de opciones, CSV, resultados JSON, manifiestos, versiones, motor y ejecutor utilizados, junto con un registro de verificación. No necesita volver a descargar precios para repetir la corrida principal.

Fuentes: Yahoo Finance mediante yfinance, cierre de 23.oct.2026. Tasa de referencia: https://fred.stlouisfed.org/series/DTB3. Método y límites del curso: docs/revision.md y skill de análisis cuantitativo. Fecha de elaboración: 23.oct.2026, hora de Santiago.

## Capturas y reproducción

Corrida principal: `2026-10-23_230246_610362_SPY_REAL`. Sensibilidad: `2026-10-23_230327_336531_XLK_REAL`. Repetición verificada: `2026-10-23_230431_784331_SPY_REAL`.

[Referencia FRED DTB3](https://fred.stlouisfed.org/series/DTB3). Precios: [AAPL](https://finance.yahoo.com/quote/AAPL/history/), [SPY](https://finance.yahoo.com/quote/SPY/history/), [XLK](https://finance.yahoo.com/quote/XLK/history/).
