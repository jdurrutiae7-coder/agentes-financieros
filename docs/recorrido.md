# Cómo recorrer y explicar el proyecto

Preparado el 28.oct.2026. Este documento describe lo implementado. Los datos del primer caso tienen su propia fecha de corte.

## Descripción breve

Adapté un flujo de equity research del curso a un proyecto de Python y agentes de IA. Separé las empresas y sus parámetros, documenté fuentes y límites, y conservé los datos y versiones necesarios para repetir una corrida de riesgo cuantitativo. Apliqué el flujo a Apple y contrasté los argumentos en un debate con roles asignados.

El material del profesor es la base metodológica. La contribución de esta adaptación se puede revisar en los archivos y en [la revisión técnica](revision.md); no se presenta el modelo completo del curso como una creación original propia.

## Qué mostrar

| Pregunta | Archivo que permite revisarla |
| --- | --- |
| ¿Cómo se organiza una investigación? | [Portada de Apple](../empresas/AAPL/Inicio.md), con cuatro etapas y sus fichas. |
| ¿Dónde están las fórmulas? | [Motor común](../src/modelo_curso.py). |
| ¿Cómo cambian empresa y comparador? | [Ejecutor](../analisis.py), [configuración de Apple](../empresas/AAPL/config.json) y plantillas por empresa. |
| ¿Qué datos y supuestos se usaron? | [Manifiesto de la corrida principal](../empresas/AAPL/03_cuantitativo/2026-10-23_230246_610362_SPY_REAL/manifest.json), junto con CSV, opciones y configuración de esa misma carpeta. |
| ¿Qué se comprobó? | [Pruebas](../tests/test_analisis.py), [verificación del caso cuantitativo](../empresas/AAPL/03_cuantitativo/2026-10-23_AAPL_verificacion_03.json) y [validación de organización](2026-10-28_validacion_organizacion.md). |
| ¿Cómo se contrastan interpretaciones? | [Paquete E#](../empresas/AAPL/04_debate/2026-10-24_AAPL_paquete_evidencia.md) y [debate](../empresas/AAPL/04_debate/2026-10-24_AAPL_debate.md). |

## Demostración desde la carpeta del proyecto

En una copia nueva, preparar Python y el entorno según [README](../README.md). En la terminal de VS Code, ubicada en la carpeta que contiene `analisis.py`, ejecutar el siguiente comando completo:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Criterio de término: las pruebas terminan con `OK`. Para repetir el cálculo principal de Apple con los datos históricos guardados, sin descargar datos nuevos:

```powershell
.\.venv\Scripts\python.exe analisis.py ejecutar --repetir "empresas\AAPL\03_cuantitativo\2026-10-23_230246_610362_SPY_REAL"
```

Criterio de término: se crea otra carpeta de corrida con resumen, ficha y manifiesto. Usar las versiones y el Python del manifiesto para comparar resultados. La igualdad numérica observada en la repetición histórica documentada no garantiza igualdad en cualquier computador, versión futura o cambio de código.

Si aparece `No such file or directory`, revisar la carpeta actual antes de modificar el comando. Si falta una librería, instalar las dependencias en `.venv`, el mismo entorno que ejecutará el código. No hace falta pegar funciones sueltas ni modificar fórmulas para esta demostración.

## Límites que hay que poder explicar

- El bloque cuantitativo modela retorno y riesgo; no valora el negocio ni determina un precio objetivo.
- La deriva y la tasa del curso son supuestos documentados. Las probabilidades simuladas dependen del modelo.
- La prueba de cobertura de VaR está dentro de muestra. No acredita predicción fuera de muestra.
- Los subagentes del debate comparten fuentes y modelo. Sus contextos separados no aportan validación externa de los datos.
- La fecha de corte de Apple es 23.oct.2026. Presentar ese caso como histórico, sin tratar sus cifras como actuales.
- La hoja de decisión de Chumi sigue separada de los resultados del modelo.

## Uso en una entrevista

Conviene explicar una decisión de implementación, abrir el archivo que la respalda y reconocer su límite. Por ejemplo: mostrar cómo se conserva la configuración al crear de nuevo una empresa y la prueba que lo verifica; después recorrer la cadena fuente, cálculo e interpretación de Apple.

El repositorio se prepara como privado. Compartir una demostración o una selección de archivos permite mostrar el trabajo sin cambiar la visibilidad de todo el material del curso.
