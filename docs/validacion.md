# Validación de la base

Nota de continuidad del 28.oct.2026: este documento conserva el registro de pruebas de la base inicial del 23.oct.2026. Las frases sobre análisis aún no ejecutados describen ese momento. El avance posterior de AAPL se consulta en [su expediente](../empresas/AAPL/Inicio.md); la organización actual se verifica en [el registro del 28.oct.2026](2026-10-28_validacion_organizacion.md).

Pruebas realizadas el 23 de octubre de 2026 con Python 3.12.14 en Windows. Las librerías de prueba se instalaron en la carpeta de trabajo de Codex, no en una instalación personal de Python de Chumi.

- Las seis copias del profesor coinciden por SHA-256 con los archivos de Downloads.
- Las cuatro skills pasan el validador de Skill Creator.
- El notebook de VS Code pasa la validación de formato de nbformat. Sus celdas Python y los scripts compilan.
- Pasaron seis pruebas: drawdown del primer día, exclusión de crisis incompletas, Kupiec sin excepciones, conservación de configuración existente, rechazo de símbolos o rutas inválidas y rechazo de un horizonte que las tablas no cubren.
- Se ejecutó el análisis completo en modo DEMO con los parámetros del curso, incluidos 10.000 caminos y horizonte de 252 días. Se generaron los seis gráficos y todos los archivos esperados.
- Una segunda corrida reutilizó el CSV y las opciones guardadas. Los resultados numéricos coincidieron exactamente.
- Cambiar el CSV guardado hizo fallar la comprobación de huellas, como corresponde.

Estas pruebas verifican funcionamiento y correcciones puntuales. No se consultaron datos reales de una empresa, no se probó la descarga de Yahoo y no se ejecutaron investigaciones ni el debate. El notebook se validó por formato y por el motor común; queda pendiente probar su ejecución desde la interfaz de VS Code y seleccionar el kernel del entorno personal.

Para correr las pruebas desde la raíz del proyecto, una vez preparado `.venv`:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

La prueba DEMO y sus datos técnicos quedaron fuera de las carpetas de empresas de la entrega. No hay una empresa elegida ni investigada todavía.
