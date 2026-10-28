# Revisión del material y decisiones de adaptación

Revisión del 23 de octubre de 2026. Los originales del profesor están en `material_curso/`. Se revisaron los cinco Markdown y las tres celdas del notebook, incluido el código de la celda principal.

La lógica del script coincide entre Markdown y notebook. El ejemplo del Markdown usa AAPL y el notebook venía con WMT; además cambia un comentario inicial. Esto no selecciona una empresa para Chumi. La configuración de ejemplo toma AAPL y SPY del Markdown.

## Mi evaluación

La secuencia ayuda a estudiar una empresa con un método: idea, negocio y competencia, comportamiento de la acción, y contraste de argumentos. Las fichas de traspaso son útiles y en Codex pueden leerse desde archivos. El bloque cuantitativo estudia rendimientos y riesgo, no el valor intrínseco del negocio. Para una decisión real podría faltar trabajo de valoración más profundo; esta base conserva las cuatro etapas del curso.

Colab resuelve la instalación y ofrece un entorno remoto con acceso a datos. El código principal del notebook no usa APIs exclusivas de Colab. VS Code puede ejecutar el mismo notebook con Python y Jupyter. Las carpetas por empresa son una decisión de organización que también sería posible en Colab, pero encajan con un repositorio local y control de versiones.

## Puntos que afectan la interpretación

- La tasa libre de riesgo inicial 0.04 es un supuesto docente. No se consultó una tasa de mercado vigente para esta entrega. Fuente y fecha de actualización se guardan en cada configuración.
- Los 10 años de calibración y 5 años de backtest son ventanas solicitadas. La cobertura real puede ser menor; se guarda el período efectivo y se avisa. El backtest usa 252 observaciones por año, no años calendario exactos.
- La simulación Monte Carlo describe resultados del modelo bajo sus supuestos. No convierte sus frecuencias en probabilidades ciertas del mundo real ni reemplaza investigación fundamental.
- El test de Kupiec usa parámetros estimados con toda la muestra. No rechazar la cobertura en esa muestra no prueba calidad predictiva fuera de muestra ni independencia entre excepciones.
- La deriva libre de riesgo usa una fórmula inspirada en volatilidad constante. Bajo GARCH-t y colas pesadas no debe describirse como una medida neutral al riesgo exacta ni como rendimiento esperado de la inversión.
- Se conserva el Sortino del curso, cuyo denominador es la desviación estándar de los retornos negativos. Es una variante, distinta de la raíz del promedio de los retornos en exceso negativos al cuadrado sobre toda la muestra. No compararlo sin aviso con un Sortino calculado por otra fuente.
- La volatilidad de opciones requiere conservar su captura. Precios y semilla por sí solos no congelan esa parte del informe. Una prima de volatilidad o datos de opciones poco líquidos pueden explicar diferencias frente al histórico; no prueba que el mercado anticipe un evento concreto.
- Un R² diario alto indica asociación del modelo de un factor. El residuo también puede contener otros factores omitidos. Si el comparador es otra empresa, no equivale al riesgo de todo el mercado.
- SPY ajustado incorpora ajustes por dividendos y splits. Un índice de precios puede medir algo distinto; elegir comparadores y monedas compatibles. Esta versión no incorpora FX.
- Las fechas de crisis se heredan del profesor. No se verificó independientemente que sean máximos y mínimos exactos. Se describen como ventanas del curso; la beta se estima con toda la muestra y no simula una predicción hecha antes de la crisis.
- En research, GDPC1 y CPIAUCSL son niveles: convertirlos y etiquetarlos para hablar de crecimiento e inflación. `revenueGrowth` no calcula un CAGR de tres años. Estas precisiones están incorporadas a la skill adaptada.

## Cambios concretos sobre el código de la celda principal

1. Extracción a `src/modelo_curso.py`. Los parámetros se pasan desde `config.json` con el ejecutor común; no se duplica el motor por empresa.
2. El drawdown simulado incluye el capital del día inicial. Antes podía omitir la caída del primer día al calcular el máximo previo.
3. Las ventanas de crisis requieren cobertura hasta su fecha final; una serie que termina antes no representa una crisis completa.
4. El test de Kupiec calcula el límite estadístico también con cero excepciones, en vez de fijar su p-valor en cero.
5. Se mantienen visibles las advertencias. Si el ajuste GARCH no converge o su persistencia es mayor o igual a uno, la corrida se detiene: no se presenta un supuesto nivel estacionario de largo plazo.
6. Se corrigen textos sobre R², opciones y prueba dentro de muestra. El gráfico de crecimiento usa base 100 sin atribuir una moneda que no fue comprobada.
7. El ejecutor guarda fuente real o sintética, configuración, precios, opciones, versiones, huellas, fechas efectivas y ficha. Repetir una corrida reutiliza sus datos y no consulta información actual.
8. Cada gráfico de prueba lleva una etiqueta DEMO para que tampoco se confunda al verlo fuera del resumen.

La implementación conserva los supuestos principales del profesor. Esta revisión no es una auditoría estadística completa. Las pruebas de funcionamiento y sus límites se documentan en `validacion.md`.
