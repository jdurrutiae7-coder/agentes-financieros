# Organización y continuidad

Primera parte preparada el 28.oct.2026. Se reutiliza la carpeta existente del proyecto; no se mantienen dos copias de trabajo.

## Dónde vive cada cosa

| Archivo o carpeta | Función |
| --- | --- |
| `Inicio.md` | Portada y estado general con enlaces. |
| `AGENTS.md` | Reglas persistentes para trabajar sobre este proyecto. |
| `.agents/skills/` | Procedimientos compartidos de las cuatro etapas. |
| `src/` y `analisis.py` | Motor común y ejecutor. Las fórmulas no se copian por empresa. |
| `config/ejemplo.json` | Configuración de partida para nuevas empresas; no cambia empresas existentes. |
| `empresas/TICKER/config.json` | Configuración para nuevas corridas de esa empresa. |
| `empresas/TICKER/Inicio.md` | Índice del expediente, corte, estado y pendientes. |
| `empresas/TICKER/Bitacora.md` | Registro fechado de avances y cambios de opinión. |
| `empresas/TICKER/01_idea/` a `04_debate/` | Informes, fuentes, fichas, corridas y decisiones de esa empresa. |
| `docs/plantillas/` | Portada y bitácora para crear nuevos expedientes. |
| `material_curso/` | Originales del profesor, conservados. |

Los índices enlazan los resultados originales. No duplicar cifras o informes en un segundo resumen que pueda quedar desactualizado. Ante una diferencia, revisar el archivo fuente y corregir el índice.

## Crear una empresa

En la raíz del proyecto, el comando existente `analisis.py crear` pide ticker y comparador. Ahora crea también `Inicio.md` y `Bitacora.md`, si faltan, a partir de las plantillas. No descarga datos ni inicia una investigación. Repetir la creación conserva la configuración y las notas existentes.

La portada de una empresa nueva comienza con etapas pendientes y sin fecha de corte financiera. El ticker no acredita el nombre, la industria o la calidad del negocio: eso se investiga después. Incorporar el enlace al índice general cuando la empresa pase a formar parte del trabajo real; crear una carpeta no altera automáticamente el índice general ni marca etapas completadas.

## Trabajar y actualizar

1. Leer `Inicio.md` de la empresa y sus fichas previas. Identificar fecha de corte, comparador y faltantes.
2. Trabajar únicamente la etapa solicitada. Mantener las fuentes y períodos explícitos.
3. Guardar informes nuevos con fecha. Una revisión posterior crea otra versión; no reemplaza la evidencia histórica. Si hay dos entregas el mismo día, añadir hora o sufijo de versión.
4. Cada ejecución cuantitativa ya crea su propia carpeta con configuración, resultados y manifiesto. La configuración de esa corrida prevalece sobre la configuración para corridas futuras.
5. Actualizar los enlaces de `Inicio.md`, el índice de empresas y la bitácora. Si cambia evidencia para el debate, crear otro paquete E# fechado.
6. Mantener la hoja de decisión de Chumi sin completar hasta que él aporte sus respuestas.

## Chats

Usar este chat para mantener el sistema y un chat por empresa para investigar. Los chats deben trabajar sobre este mismo proyecto. La portada y las fichas permiten retomar sin depender del historial del chat. La separación es una convención de trabajo; no se abrieron chats nuevos en esta primera parte.

## Qué quedará en Git

Se preparó `.gitignore` para conservar código, skills, configuraciones, informes, fuentes documentadas, precios CSV, opciones JSON, resultados, versiones y manifiestos de corridas reales. Se excluyen el entorno Python, cachés, archivos de secretos, ZIP de respaldo, corridas DEMO y PNG cuantitativos regenerables.

Los PDF de lectura se pueden conservar junto con sus versiones Markdown. Los ZIP y PNG excluidos siguen en disco y pueden formar parte de los respaldos de Drive. El archivo `2026-10-28_validacion_organizacion.md` documenta la comprobación de estas reglas.

Al terminar la primera parte local, Git estaba inicializado sin commits ni remoto. En la preparación del repositorio del 28.oct.2026 se creó [agentes-financieros](https://github.com/jdurrutiae7-coder/agentes-financieros) como privado y se configuró `origin`. Los manifiestos históricos conservan sus huellas originales: cambiar la organización o el ejecutor no debe reescribirlos. `.gitattributes` conserva los bytes sin normalizar finales de línea para no alterar las huellas al clonar.

## Obsidian y Drive

La carpeta está preparada con Markdown y enlaces relativos normales para leerla como vault propio en una etapa posterior. Todavía no se configuró Obsidian. Sus archivos de disposición de ventanas quedarán fuera de Git cuando existan.

Drive contiene respaldos por etapa y no una sincronización automática. Los cambios locales de organización del 28.oct.2026 aún no están respaldados allí. Verificar y registrar una carga antes de cambiar ese estado.

## Siguientes partes

- Registrar cambios en commits y verificar cada carga al repositorio privado. La conexión no sincroniza automáticamente las ediciones.
- Abrir el proyecto en Obsidian y comprobar su navegación.
- Organizar los chats por empresa cuando Chumi pida crearlos y elegir el próximo análisis.
