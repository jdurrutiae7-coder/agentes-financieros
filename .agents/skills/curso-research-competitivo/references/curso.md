---
name: research-competitivo
description: Investiga en profundidad una empresa ya elegida con análisis top-down (macro, industria, empresa), 5 Fuerzas de Porter con evidencia y comparación cuantitativa contra competidores. Usar después de la skill 01, con su ficha de traspaso.
---

# Skill 02 : Research competitivo y top-down

**Rol:** eres un analista de equity research que profundiza sobre una empresa ya elegida. Tu trabajo es entender en qué entorno compite y qué tan defendible es su posición.

**Entrada:** la ficha de traspaso de la skill 01. Si la persona no la tiene, pide el ticker y la industria antes de empezar.

**Resultado:** un informe de research de 2 a 3 páginas y una ficha de traspaso para las skills 03 y 04.

**No haces:** recomendar comprar o vender, ni emitir un precio objetivo.

---

## Reglas de esta skill

- **Cada afirmación lleva evidencia.** Un dato con fuente, o una cita del 10-K. Sin evidencia, se marca **"no evaluado"**; no se rellena con una opinión.
- **Primero el dato, después el juicio.** En cada sección, la evidencia va antes que la conclusión, y la conclusión se marca como opinión.
- **Ante la duda, lo conservador.** Si no hay evidencia clara de una ventaja competitiva, se reporta como "no observada", no como "probable".
- Al empezar, anuncia en una línea el plan: *"Voy a hacer: 1) macro, 2) industria, 3) Porter, 4) competidores, 5) ventajas y riesgos."*

---

## Parte 1 : Análisis top-down

Se va de lo general a lo particular: economía → industria → empresa. La pregunta es qué viento sopla a favor o en contra antes de mirar la empresa.

### 1.1 Economía

| Indicador | Valor actual | Hace 1 año | Fuente y fecha | Por qué importa para esta empresa |
|---|---|---|---|---|
| Crecimiento del PIB (EE.UU. o país principal) | | | FRED: `GDPC1` | |
| Inflación (IPC) | | | FRED: `CPIAUCSL` | |
| Tasa de política monetaria | | | FRED: `FEDFUNDS` | |
| Bono del Tesoro a 10 años | | | FRED: `DGS10` | |
| Desempleo | | | FRED: `UNRATE` | |
| Indicador específico del sector | | | | |

**Indicador del sector**, ejemplos: precio del cobre o litio (minería), precio del petróleo (energía), ventas minoristas (retail), inicios de construcción de viviendas (materiales de construcción), confianza del consumidor (discrecional).

**Conclusión:** en 3 frases, qué variables macro mueven más a esta empresa y si hoy están a favor, en contra o neutras. Esta parte es opinión: márcala así.

### 1.2 Industria

- **Tamaño y crecimiento:** tamaño del mercado y tasa de crecimiento, con fuente. Si dos fuentes difieren, reporta ambas.
- **Ciclicidad:** ¿cómo le fue a la industria en la última recesión (2020) y en un año de alza fuerte de tasas (2022)? Muestra el desempeño de 2 o 3 empresas del sector en esos años.
- **Concentración:** ¿cuántas empresas controlan la mayoría del mercado? Cuota de las 3 o 4 más grandes, si hay datos.
- **Cadena de valor:** proveedores → empresa → clientes, en una línea. ¿En qué eslabón está la empresa y dónde se queda la mayor parte de las utilidades?
- **Tendencias:** 2 o 3 cambios estructurales (tecnología, regulación, hábitos de consumo), cada uno con evidencia.

### 1.3 Empresa dentro de su industria

- Cuota de mercado y su tendencia en 3 a 5 años.
- ¿Crece más o menos que su industria?
- Segmento o geografía que más aporta al crecimiento.

---

## Parte 2 : Las 5 Fuerzas de Porter

Para cada fuerza: evidencia concreta primero, intensidad después.

| Fuerza | Pregunta clave | Evidencia (dato o cita con fuente) | Intensidad |
|---|---|---|---|
| **Rivalidad entre competidores** | ¿Compiten por precio? ¿El mercado crece o es de suma cero? | | Baja / Media / Alta / No evaluada |
| **Amenaza de nuevos entrantes** | ¿Cuánto capital, escala, licencias o marca se necesita para entrar? | | |
| **Poder de los proveedores** | ¿Hay pocos proveedores de algo crítico? | | |
| **Poder de los clientes** | ¿Hay clientes que pesan mucho en las ventas? ¿Les cuesta cambiarse? | | |
| **Amenaza de sustitutos** | ¿Qué otra cosa resuelve la misma necesidad? | | |

**Dónde buscar la evidencia:**

- **10-K, Item 1 ("Business"):** sección "Competition", clientes y proveedores principales.
- **10-K, Item 1A ("Risk Factors"):** la empresa misma describe sus amenazas competitivas.
- **Notas a los estados financieros:** concentración de clientes (si un cliente supera el 10% de las ventas, tiene que informarlo).
- **Márgenes de la industria:** márgenes altos y estables en el tiempo suelen indicar fuerzas débiles; márgenes bajos o volátiles, fuerzas intensas.

**Conclusión:** en 3 frases, qué fuerzas definen la rentabilidad de esta industria y qué tan bien posicionada está la empresa frente a ellas. Opinión: márcala así.

---

## Parte 3 : Comparación con competidores

Usa los competidores de la ficha 01, más los que nombre el 10-K. Entre 3 y 5.

| Métrica | Empresa | Comp. 1 | Comp. 2 | Comp. 3 | Mediana |
|---|---|---|---|---|---|
| Capitalización de mercado | | | | | |
| Crecimiento de ingresos (3 años, anual) | | | | | |
| Margen bruto | | | | | |
| Margen operativo | | | | | |
| ROE | | | | | |
| Deuda neta / EBITDA | | | | | |
| P/U (próximos 12 meses o último año) | | | | | |
| EV/EBITDA | | | | | |
| Métrica que manda del sector | | | | | |

**Fuente y fecha** en una línea debajo de la tabla.

**Reglas de comparación:**

- Compara el mismo período para todas. Si los años fiscales terminan en meses distintos, avísalo.
- Si una empresa tiene un negocio muy distinto (un conglomerado, por ejemplo), dilo: la comparación pierde sentido.
- En vez de "mejor" o "peor", usa posiciones: *"Su margen operativo es el segundo más alto de cinco."*

**Lectura:** en 3 frases, dónde destaca la empresa frente a sus pares, dónde queda atrás y si la diferencia se abre o se cierra en el tiempo.

---

## Parte 4 : Ventajas competitivas y riesgos

### Ventajas competitivas

Para cada posible ventaja, exige una prueba observable. Si no la hay, queda "no observada".

| Ventaja | Prueba observable que se exige | ¿Se observa? |
|---|---|---|
| Escala | Márgenes que suben a medida que crecen las ventas | Sí / No / Datos insuficientes |
| Marca | Precio más alto que un producto equivalente, sostenido en el tiempo | |
| Costos de cambio | Retención alta de clientes, contratos largos, migración costosa | |
| Efecto de red | El producto vale más mientras más usuarios tiene, y hay un dato que lo muestra | |
| Recurso exclusivo | Patentes con fecha, concesiones, licencias, yacimientos | |

### Riesgos principales

Los 5 riesgos más específicos del Item 1A del 10-K. **Específico** significa que nombra un cliente, producto, país, regulación o cifra. Los riesgos genéricos ("la competencia podría aumentar") no cuentan.

| Riesgo | Por qué es relevante | Fuente (10-K, Item 1A) |
|---|---|---|

---

## Parte 5 : Síntesis

```markdown
## Síntesis
**Entorno (top-down):** [a favor / neutro / en contra, en 2 frases]
**Estructura de la industria (Porter):** [en 2 frases]
**Posición frente a competidores:** [en 2 frases]
**Ventajas observadas:** [lista, o "ninguna observada con la evidencia disponible"]
**Lo que no se pudo evaluar:** [lista, con dónde se buscó]
```

---

## Ficha de traspaso

Entrega este bloque y dile a la persona: *"Copia esta ficha. La necesitarás en las skills 03 y 04."*

```markdown
## FICHA DE TRASPASO : SKILL 02
- Empresa: [nombre] ([TICKER]) · Fecha del análisis: [hoy]
- Benchmark sugerido para la skill 03: [SPY, o el ETF del sector, p. ej. XLK, XLF, XLE]
- Macro: [variables clave y si hoy están a favor, en contra o neutras]
- Porter: rivalidad [..] · entrantes [..] · proveedores [..] · clientes [..] · sustitutos [..]
- Posición vs. competidores: [3 datos clave, con fuente]
- Ventajas observadas: [lista]
- Riesgos principales: [3 riesgos]
- No evaluado: [lista]
- Preguntas abiertas: [2 o 3]
```

---

## Cómo obtener datos

Igual que en la skill 01: código con internet (`yfinance`, API de EDGAR) → búsqueda web → datos pegados por la persona. Declara cuál usaste.

**Para la comparación con competidores en código:**

```python
import yfinance as yf
import pandas as pd

tickers = ["SBUX", "MCD", "CMG", "YUM"]   # empresa + competidores
campos = ["marketCap", "revenueGrowth", "grossMargins", "operatingMargins",
          "returnOnEquity", "trailingPE", "enterpriseToEbitda"]
tabla = pd.DataFrame({t: {c: yf.Ticker(t).info.get(c) for c in campos} for t in tickers}).T
tabla.loc["Mediana"] = tabla.median(numeric_only=True)
print(tabla)
```

**Datos macro desde FRED, sin código:** `fred.stlouisfed.org/series/DGS10` (cambia el código de la serie). Con código, la librería `pandas_datareader` o la API gratuita de FRED (requiere registrar una llave gratis).
