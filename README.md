# Equity research con IA y Python

Proyecto de José Domingo Urrutia para investigar empresas con un flujo de cuatro etapas: idea, research competitivo, análisis cuantitativo de riesgo y debate de argumentos. Usa Python, VS Code y skills de Codex, con una carpeta por empresa y evidencia fechada.

El punto de partida es el material del curso del Club de Finanzas e Inversiones. Las adaptaciones del ejecutor, correcciones del modelo, estructura por empresa y controles de reproducibilidad se describen en [la revisión técnica](docs/revision.md). Los originales del profesor se conservan en `material_curso/`; el proyecto no atribuye su metodología original al autor de esta adaptación.

## Recorrido rápido

1. [Expediente de Apple](empresas/AAPL/Inicio.md): caso completo, fichas y pendientes, con evidencia al 23.oct.2026.
2. [Motor Python](src/modelo_curso.py) y [ejecutor](analisis.py): fórmulas compartidas y parámetros por empresa.
3. [Corrida principal de Apple frente a SPY](empresas/AAPL/03_cuantitativo/2026-10-23_230246_610362_SPY_REAL/resumen.md) y [manifiesto](empresas/AAPL/03_cuantitativo/2026-10-23_230246_610362_SPY_REAL/manifest.json): datos, supuestos, versiones y huellas de esa ejecución.
4. [Pruebas](tests/test_analisis.py): controles estadísticos puntuales, protección de configuraciones y separación de expedientes.
5. [Guía para presentar el proyecto](docs/recorrido.md): alcance, aportes, límites y una demostración reproducible.

El motor estudia retornos y riesgo bajo supuestos. No estima valor intrínseco ni produce señales de compra o venta. La investigación y el debate necesitan ejecución desde Codex y revisión de las fuentes; no son tareas automatizadas por el script Python.

Repositorio privado: [jdurrutiae7-coder/agentes-financieros](https://github.com/jdurrutiae7-coder/agentes-financieros). La carpeta de trabajo está registrada en Codex como **Agente Financiero**. El código y las empresas comparten el mismo repositorio; cada caso conserva sus datos y corte de evidencia.

**Entrada del proyecto:** [Inicio.md](Inicio.md). Organización local del 28.oct.2026: portadas, bitácoras, [índice de empresas](empresas/README.md), [glosario](Glosario.md) y [procedimiento de continuidad](docs/organizacion.md). Esta fecha no actualiza la evidencia de Apple.

## Qué está preparado

- Los seis archivos originales en `material_curso/`, con huellas SHA-256 para comprobar que no cambiaron.
- Cuatro skills de Codex en `.agents/skills/`: idea, research, cuantitativo y debate.
- El motor Python extraído del notebook, con las adaptaciones descritas en `docs/revision.md`.
- Un ejecutor para elegir empresa y comparador sin editar fórmulas.
- Un notebook para VS Code que usa el mismo motor.
- Resultados nuevos por cada corrida: resumen, ficha, precios, gráficos, configuración, opciones y registro de versiones.

Las primeras dos skills y el debate producen informes mediante Codex. El script Python ejecuta la etapa cuantitativa; no automatiza por sí solo la investigación web ni el debate.

## Avance de Apple al 24 de octubre de 2026 (evidencia al 23 de octubre)

| Etapa | Estado | Entregable |
|---|---|---|
| 01 Idea | Completada | `empresas/AAPL/01_idea/2026-10-23_AAPL_brief.md` y ficha 01 |
| 02 Research | Completada con faltantes declarados | `empresas/AAPL/02_research/2026-10-23_AAPL_research.pdf`, versión Markdown, ficha 02 y fuentes/cálculos JSON |
| 03 Cuantitativo | Completada con datos reales y repetición numérica exacta de la corrida SPY | SPY principal y XLK como sensibilidad; `empresas/AAPL/03_cuantitativo/2026-10-23_AAPL_lectura_03.pdf`, ficha 03 y paquete reproducible ZIP |
| 04 Debate | Debate completado; decisión personal de Chumi pendiente | `empresas/AAPL/04_debate/2026-10-24_AAPL_debate.pdf`, rondas, paquete E#, mapa, hoja de decisión y trazabilidad |

Los entregables 01, 02, 03 y 04 están respaldados en la carpeta de Apple en Drive. Son cargas realizadas por etapa, sin sincronización automática. El ZIP original conserva la base inicial; los análisis posteriores están en las carpetas del proyecto. La etapa 03 tiene un ZIP propio con código, precios, opciones, versiones, manifiestos, resultados y gráficos de las corridas reales, sin incluir `.venv`. El entorno `.venv` ya está preparado en este equipo; en otro computador se debe recrear.

## Abrir en VS Code

Abre `agentes-financieros.code-workspace`, que está en esta carpeta. Se recomienda Python 3.12. Instala las extensiones oficiales Python y Jupyter de Microsoft. VS Code es el editor; Python ejecuta el modelo; GitHub conserva las versiones que se confirman mediante commits y se suben al remoto.

El equipo de Chumi tiene VS Code, pero el lanzador `py` no detectó una instalación personal de Python al revisar esta base. Instala Python desde [python.org](https://www.python.org/downloads/windows/) si `py -0p` sigue sin mostrar intérpretes. El Python interno de Codex es un entorno aparte.

## Preparación inicial en Windows

Abre Terminal > New Terminal dentro de esta carpeta y ejecuta los siguientes comandos, uno a la vez. No necesitas activar el entorno, por lo que no deberías encontrar el bloqueo de scripts de PowerShell.

```powershell
py -3.12 -m venv .venv
```

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Criterio de término: la instalación termina sin errores y existe `.venv\Scripts\python.exe`. En VS Code selecciona ese intérprete en Python: Select Interpreter. En el notebook selecciona el mismo entorno en Select Kernel.

`requirements-modelo.txt` fija las versiones principales usadas en las pruebas. `ipykernel` agrega el soporte para ejecutar desde el notebook.

## Crear una empresa y probar

```powershell
.\.venv\Scripts\python.exe analisis.py crear
```

Te pide el ticker y el comparador. Para probar puedes usar AAPL y SPY, que ya aparecen en el material. Son ejemplos, no una selección de inversión. El script crea las cuatro carpetas, `config.json`, `Inicio.md` y `Bitacora.md` a partir de las plantillas. Conserva los archivos existentes. La portada nueva comienza con investigación pendiente; actualizar los índices generales al incorporar una empresa real.

```powershell
.\.venv\Scripts\python.exe analisis.py ejecutar --empresa AAPL --demo
```

Criterio de término: imprime la carpeta nueva y esta contiene `resumen.md`, `ficha_03.md`, un CSV de precios sintéticos, JSON de resultados, `manifest.json` y gráficos. DEMO prueba el funcionamiento y no describe a Apple ni al S&P 500.

## Correr con datos reales

Revisa `empresas/AAPL/config.json`: ticker, benchmark, moneda y supuestos. El 4% inicial es un supuesto del profesor, no una tasa vigente comprobada. Si actualizas la tasa, anota su fuente y fecha. La descarga requiere internet en el proceso de Python y puede fallar por límites de Yahoo.

```powershell
.\.venv\Scripts\python.exe analisis.py ejecutar --empresa AAPL
```

Para otro comparador en una corrida, sin cambiar la configuración guardada:

```powershell
.\.venv\Scripts\python.exe analisis.py ejecutar --empresa AAPL --benchmark MSFT
```

SPY representa un ETF del S&P 500 con precios ajustados. Un índice de precios y un ETF con dividendos ajustados no son equivalentes. Otra empresa sirve para comparación relativa, pero no representa todo el mercado. El ejecutor verifica que ambos instrumentos tengan la moneda declarada; no implementa conversión cambiaria.

## Estructura de una empresa

```text
empresas/
  AAPL/
    Inicio.md           entrada, fechas, fichas y pendientes
    Bitacora.md         avances y cambios fechados
    config.json
    01_idea/             brief y ficha 01
    02_research/         informe y ficha 02
    03_cuantitativo/
      fecha_hora_SPY_REAL/
        config.json
        resumen.md
        ficha_03.md
        manifest.json
        opciones.json
        dependencias.txt
        precios.csv y resultados.json con prefijo del ticker
        gráficos PNG
    04_debate/           evidencia, aperturas, réplicas y decisión
```

La fecha y hora evitan sobrescribir corridas del mismo día. Un comparador distinto genera otra corrida dentro de la misma empresa.

## Reproducir una corrida

En `--repetir` pega la ruta de la carpeta completa entre comillas. Se reutilizan los precios y las opciones de esa carpeta; no se descarga información nueva. Debes conservar las mismas versiones del archivo `dependencias.txt` y el mismo motor para comparar numéricamente.

```powershell
.\.venv\Scripts\python.exe analisis.py ejecutar --repetir "RUTA_COMPLETA_DE_LA_CORRIDA"
```

La repetición genera una carpeta nueva. Si cambiaste los precios, las opciones o la configuración original, el script lo detecta mediante huellas. Para trasladar la corrida a otro equipo, copia la carpeta completa, usa el mismo Python y las versiones indicadas en `dependencias.txt`.

## Usar las skills en Codex

Abre Codex con esta carpeta como proyecto de trabajo. Las skills están dentro de `.agents/skills/`, el formato por proyecto. Si no aparecen al abrir el proyecto, reinicia Codex. En este chat también se pueden leer y usar indicando su ruta.

Puedes pedir en lenguaje normal: "Usa la skill de idea generation del curso" o "Analiza cuantitativamente la empresa guardada y explica el resumen". Las cuatro skills conservan el procedimiento del profesor, con adaptaciones de almacenamiento y entorno. Las etapas 01, 02 y 03 de Apple ya se ejecutaron con datos reales. La etapa 04 contrastó esas fichas en un debate con aperturas separadas, revisión y réplicas; no se incorporaron datos nuevos y la decisión personal sigue pendiente. En la etapa 03 se mantuvo el 4% como supuesto docente; FRED DTB3 se documentó solo como referencia, sin sustituir esa tasa.

## Errores habituales

`No such file or directory`: la terminal debe estar en la carpeta que contiene `analisis.py`. Las carpetas de empresas se crean con `crear`, no a mano. `No module named`: instala las librerías en el mismo `.venv` que seleccionaste. `IndentationError`: usa estos archivos completos sin pegar funciones sueltas. Si Yahoo no devuelve datos, revisa ticker y conexión; no reemplaces datos reales por DEMO para completar una investigación.

## Propuesta para avanzar

La primera empresa ya cuenta con las cuatro etapas. La organización local del 28.oct.2026 se documenta en `docs/organizacion.md`. El repositorio privado se creó ese día y se configuró como `origin`. El siguiente paso de organización es abrir esta carpeta como vault propio de Obsidian. Los chats nuevos por empresa deben abrirse dentro del proyecto Agente Financiero. Los cambios locales y los commits no se suben solos: confirmar cada envío y registrar el estado de los respaldos de Drive por separado.

La nueva política de Git conserva archivos de auditoría y datos de corridas reales. Excluye `.venv`, cachés, secretos, ZIP, corridas DEMO y PNG cuantitativos; los archivos excluidos permanecen en disco. No se deben borrar ni reescribir las huellas históricas para ajustarlas a cambios del ejecutor.

Fuentes de configuración: [notebooks en VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), [skills de Codex](https://learn.chatgpt.com/docs/build-skills), [yfinance](https://ranaroussi.github.io/yfinance/).
