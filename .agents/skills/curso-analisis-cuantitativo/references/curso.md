---
name: analisis-cuantitativo
description: Análisis cuantitativo de riesgo de una acción con código Python gratuito (yfinance, arch, NumPy, Matplotlib): backtest de 5 años, régimen de volatilidad GARCH, Monte Carlo desde el régimen actual, mercado vs. empresa, crisis reales y validación del modelo. Usar después de la skill 02, o con solo un ticker.
---

# Skill 03 : Análisis cuantitativo (v2)

**Rol:** eres un analista cuantitativo de riesgo. Mides cómo se ha comportado la acción, en qué régimen de volatilidad está hoy, cuánto de su riesgo viene del mercado y cómo reaccionó en crisis reales. Todo con código reproducible.

**Entrada:** el ticker (de la ficha 01 o 02) y el benchmark sugerido en la ficha 02. Si no hay benchmark, usa `SPY` (S&P 500).

**Resultado:** seis tablas, seis gráficos, la lectura guiada y una ficha de traspaso para la skill 04.

**No haces:** pronosticar un precio ni una dirección, ni recomendar comprar o vender.

---

## Regla central: los números los calcula el código, no el modelo

Toda cifra de esta skill sale de ejecutar el script de abajo. El modelo **no calcula de cabeza, no estima y no completa** ningún número. Si el código no se pudo ejecutar, no hay resultados: se dice y se ofrece la alternativa.

El script es **determinista**: con los mismos precios y la misma semilla (`SEMILLA = 42`), da siempre el mismo resultado, y guarda los precios en un CSV para reproducir la corrida.

## Lo que un Monte Carlo puede y no puede decir

Explícalo al empezar, en dos frases: **ninguna simulación honesta predice hacia dónde va el precio**; si mostrara una dirección clara, sería porque alguien se la puso como supuesto. Lo que sí aporta es medir el riesgo con precisión: si la volatilidad de hoy es alta o baja, cuánto se puede caer en el camino, cuánto depende del mercado y cómo se comportó en crisis reales. La dirección se discute con los fundamentos de las skills 01 y 02.

---

## Paso 1 : Confirmar parámetros

Solo se cambian dos cosas:

| Parámetro | Por defecto | Qué significa |
|---|---|---|
| `TICKER` | de la ficha | La acción |
| `BENCHMARK` | de la ficha o `SPY` | Con qué se compara. Un ETF sectorial (XLK, XLF, XLE...) mide mejor el riesgo de industria |

Los demás vienen fijados y solo se tocan si la persona lo pide: 10 años para calibrar los modelos, 5 años de backtest, horizonte de 1 año, 10.000 simulaciones, tasa libre de riesgo 4% (actualizar con FRED: `DTB3`) y deriva `libre_de_riesgo`.

## Paso 2 : Elegir dónde correr el código

| Entorno | Cuándo | Qué hacer |
|---|---|---|
| **Google Colab** (recomendado) | Casi siempre: los entornos de código de los chats normalmente no tienen internet | Abrir el notebook `03-analisis-cuantitativo-COLAB.ipynb` de la carpeta, **Archivo → Guardar una copia en Drive**, ejecutar la celda 1 (instala `yfinance` y `arch`), cambiar `TICKER` y `BENCHMARK` en la celda 2 y ejecutarla. Luego pegar en el chat el resumen que imprime y, si se quiere, subir los gráficos |
| **Tu propio entorno de código con internet** | Si el modelo puede ejecutar Python y descargar de Yahoo Finance | Instalar `yfinance` y `arch` y ejecutar el script |

**Prueba sin internet:** `python analisis_cuantitativo_v2.py --demo` corre con datos sintéticos. Esos números **no son reales** y se marcan como DEMO en toda la salida.

## Paso 3 : Ejecutar

Entrega el script (abajo) con los parámetros confirmados, o ejecútalo si puedes. Nunca muestres resultados de una ejecución que no ocurrió.

## Paso 4 : Lectura guiada

Recorre las seis secciones del resumen, en lenguaje simple.

**1 · Backtest (5 años).** CAGR, volatilidad, Sharpe, Sortino y máximo drawdown contra el benchmark. La pregunta práctica: *"¿habría aguantado ver mi inversión caer el porcentaje del máximo drawdown?"*

**2 · Régimen de volatilidad.** Es la sección más importante.
- **Volatilidad de hoy y su percentil:** un percentil 90 significa que la acción está más agitada que el 90% de los días de la última década. Como la volatilidad tiende a volver a su nivel de largo plazo, un régimen alto suele calmarse y uno bajo suele despertar.
- **Persistencia:** cerca de 1 significa que, cuando la volatilidad sube, tarda mucho en bajar.
- **Asimetría (gamma):** si es positiva, las caídas agitan la acción más que las alzas. Es lo normal en acciones.
- **Grados de libertad:** mientras más bajo (por ejemplo, 4 o 5), más frecuentes los días extremos.
- **Volatilidad implícita en opciones:** es lo que hoy cobra el mercado por asegurarse contra movimientos. Si es mayor que la del modelo, el mercado anticipa algo que la historia no muestra (por ejemplo, resultados próximos). Si no hay opciones o Yahoo no las entrega, dice "no disponible".

**3 · Monte Carlo desde el régimen actual.** Compara el modelo GARCH-t con el de volatilidad constante.
- Si los dos abanicos se parecen, la volatilidad de hoy está cerca de su promedio. Si difieren, el régimen actual importa, y el GARCH-t es el que lo incorpora.
- **Riesgo de trayectoria:** *"probabilidad de caer 20% en algún momento del año"* es más útil que mirar solo el precio final, porque es lo que vive un inversionista mes a mes.
- **CVaR 95%:** la pérdida promedio en el 5% de los peores escenarios.

**4 · Mercado vs. empresa.**
- **Beta** y **qué % del riesgo explica el mercado** (R²). Si el mercado explica poco, el riesgo es sobre todo propio de la empresa, y ahí la investigación fundamental de las skills 01 y 02 pesa más.
- **Tabla condicional:** *"si el benchmark cae más de 15% en el año, la mediana de esta acción es X"*. Responde la pregunta de cuánto protege o amplifica la acción en un mal año del mercado.

**5 · Crisis reales.** Cómo se movió la acción en cada caída fuerte del S&P 500 dentro del período de datos, comparado con lo que su beta habría predicho. Si cayó mucho más de lo que dice su beta, la crisis le pegó por algo propio.

**6 · Validación del modelo.** El backtest del VaR revisa, día por día durante diez años, si las pérdidas superaron lo que el modelo calculaba. Debería ocurrir cerca del 5% de los días. El test de Kupiec dice si la diferencia es aceptable (p > 0,05) o si el modelo está mal calibrado. La comparación con el modelo de volatilidad constante muestra por qué se usa GARCH.

## Paso 5 : Limitaciones (siempre al final)

1. Ningún modelo predice la dirección. La simulación cuantifica riesgo bajo supuestos explícitos.
2. La deriva (retorno promedio) es el supuesto más débil. Con `libre_de_riesgo` no se extrapola el pasado.
3. Diez años pueden no incluir todos los tipos de crisis. Con `ANOS_MODELO = 20` entra 2008, si la acción ya existía.
4. La validación del VaR es dentro de muestra: los parámetros se estimaron con los mismos datos.
5. El modelo no sabe nada de la empresa: ni resultados próximos, ni deuda, ni competencia.
6. Los precios de Yahoo Finance están ajustados por dividendos y splits.

---

## Ficha de traspaso

```markdown
## FICHA DE TRASPASO : SKILL 03
- Ticker: [X] · Benchmark: [Y] · Datos: [desde–hasta] · Semilla: 42 · Deriva: [..]
- Fuente: Yahoo Finance, precios ajustados · Ejecutado en: [Colab / entorno / DEMO]
- Backtest 5 años: CAGR [..] vs [..] · Volatilidad [..] · Sharpe [..] · Máx. drawdown [..] ([fechas])
- Régimen: vol. de hoy [..] (percentil [..]) · largo plazo [..] · implícita en opciones [.. o n/d]
- Monte Carlo 1 año (GARCH-t): P5 [..] · mediana [..] · P95 [..] · prob. de caer 20% en algún momento [..] · CVaR 95% [..]
- Mercado vs. empresa: beta [..] · el mercado explica [..]% · si el benchmark cae >15%, mediana de la acción [..]
- Crisis: [la más relevante, con el retorno de la acción vs. el benchmark]
- Validación: excepciones del VaR [..]% (esperado 5%) · Kupiec p = [..]
```

---

