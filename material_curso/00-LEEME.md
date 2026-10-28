# Análisis de inversión con agentes de IA — kit de skills

**Club de Finanzas e Inversiones · material educativo · octubre 2026**

Cuatro skills que llevan a un inversionista desde "no sé qué mirar" hasta una decisión propia sobre una acción, usando solo datos gratuitos. Funcionan en cualquier modelo: Claude, ChatGPT, Gemini u otro.

> **Esto no es asesoría de inversión.** Es un ejercicio de aprendizaje. Ninguna skill recomienda comprar ni vender: entregan análisis, y la decisión es siempre de la persona.

---

## El flujo

```
01 Idea Generation  ──►  02 Research  ──►  03 Cuantitativo  ──►  04 Debate
 (industria → 5 empresas    (Porter, top-down,   (backtest 5 años,     (bajista, neutral y
  → elegir una → brief)      competencia)         Monte Carlo)          alcista → decides tú)
        │                        │                     │                      │
        └── Ficha de traspaso ───┴── Ficha de traspaso ┴── Ficha de traspaso ─┘
```

Cada skill termina con una **ficha de traspaso**: un bloque de texto que resume lo encontrado. Copias esa ficha y la pegas al iniciar la skill siguiente. Así cada etapa parte con el contexto de la anterior sin arrastrar toda la conversación, lo que también abarata el uso.

| Archivo | Qué hace | Necesita código |
|---|---|---|
| `01-idea-generation.md` | 3–4 preguntas para llegar a una industria, propone 5 empresas, y arma un brief de la elegida | No (opcional) |
| `02-research-competitivo.md` | Análisis top-down, 5 Fuerzas de Porter y comparación con competidores | No (opcional) |
| `03-analisis-cuantitativo.md` | Backtest de 5 años y simulación Monte Carlo, deterministas | **Sí** |
| `04-debate-tres-agentes.md` | Tres agentes debaten con la evidencia reunida; tú decides | No |
| `analisis_cuantitativo.py` | El script de la skill 03, listo para Google Colab | — |

---

## Cómo cargar una skill en cada modelo

| Modelo | Cómo |
|---|---|
| **Claude** | Sube el `.md` a un Proyecto como conocimiento, o adjúntalo al inicio del chat. Si usas Claude Code o el escritorio con skills, puede instalarse como skill (ya trae el encabezado `name` / `description`) |
| **ChatGPT** | Crea un GPT personalizado y pega el contenido en las instrucciones, o adjunta el archivo al inicio del chat |
| **Gemini** | Crea un Gem con el contenido como instrucciones, o adjunta el archivo |
| **Cualquier otro** | Pega el contenido completo como primer mensaje y escribe: *"Sigue estas instrucciones"* |

**Recomendación:** un chat nuevo por skill. Pega el archivo de la skill y, desde la 02 en adelante, la ficha de traspaso de la anterior.

---

## Fuentes de datos (todas gratuitas)

| Fuente | Qué aporta | Confiabilidad | Cómo se accede |
|---|---|---|---|
| **SEC EDGAR** | Reportes oficiales que las empresas entregan al regulador de EE.UU.: 10-K (anual), 10-Q (trimestral), 20-F (empresas extranjeras), 8-K (eventos) | **Máxima.** Es el documento legal | Web: `sec.gov/edgar/search` · API: `data.sec.gov` (gratis, sin llave) |
| **Yahoo Finance** | Precios históricos, múltiplos, estados financieros resumidos, perfil de la empresa | **Buena para precios; revisar los fundamentales contra EDGAR** | Web: `finance.yahoo.com` · Python: librería `yfinance` |
| **FRED** (complemento) | Tasas, inflación, PIB, desempleo. Lo publica la Reserva Federal de St. Louis | **Máxima** | Web: `fred.stlouisfed.org` |

**Tres cosas que conviene saber:**

1. **`yfinance` no es una API oficial de Yahoo.** Lee el sitio público, puede fallar sin aviso, y sirve para uso personal y educativo.
2. **La SEC exige identificarse** al usar su API desde código: un encabezado `User-Agent` con nombre y correo, y no más de 10 consultas por segundo.
3. **Muchos chats de IA no tienen internet dentro de su entorno de código.** Si el modelo no puede descargar datos, usa **Google Colab** (gratis, con internet, trae Python y Matplotlib). Es la opción recomendada para la skill 03.

---

## Reglas de oro (aplican a las cuatro skills)

1. **Ningún número sin fuente y fecha.** Cada cifra dice de dónde salió (*10-K 2025, Yahoo Finance al 22-oct-2026*).
2. **Si no encuentras un dato, se dice.** *"No encontrado: busqué en el 10-K, sección X, y en Yahoo Finance."* Nunca se inventa ni se estima en silencio.
3. **Hecho, cálculo y opinión van separados.** "Los ingresos crecieron 8%" es un hecho; "es una empresa sólida" es una opinión y debe marcarse como tal.
4. **La IA analiza; la persona decide.** Ninguna skill recomienda comprar, vender ni cuánto invertir.
5. **Lenguaje neutro en los datos.** "El margen bajó de 22% a 18%", no "el margen se desplomó".

---

## Para la clase

**Duración sugerida:** 90 minutos. 01 (20 min) · 02 (20 min) · 03 (25 min) · 04 (20 min) · cierre (5 min).

**Para que funcione en vivo:** probar el notebook de Colab de la skill 03 antes de la clase con una acción conocida, y tener a mano una ficha de traspaso ya hecha por si un grupo se atrasa.
