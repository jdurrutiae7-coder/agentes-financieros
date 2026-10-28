# Primera publicación del repositorio privado

Fecha: 28.oct.2026. Repositorio: [jdurrutiae7-coder/agentes-financieros](https://github.com/jdurrutiae7-coder/agentes-financieros). Visibilidad privada verificada mediante el conector de GitHub.

## Qué se publicó

La primera carga contiene 96 archivos: código, cuatro skills y sus referencias, material original del curso, documentación, pruebas, selección inicial y expediente de Apple. Los archivos de cada empresa permanecen en su propia carpeta. Los entornos, cachés, ZIP de respaldo, DEMO y PNG cuantitativos se excluyen según `.gitignore`.

Commits de esa carga:

- `8d1a725`: flujo de equity research y caso AAPL con datos para reproducir el análisis.
- `12ba984`: identificación de PDF, imágenes y ZIP como archivos binarios en Git.

La rama `main` se subió a `origin/main`. Esta nota se agrega después de esa carga; describe la verificación de esos 96 archivos, no un conteo fijo para versiones futuras.

## Qué se comprobó

- Siete pruebas del proyecto terminaron con `OK` en el entorno local.
- Los 104 archivos históricos protegidos conservan su SHA-256 respecto del cotejo previo de organización.
- Los blobs de los 96 archivos del primer envío coinciden byte a byte con sus archivos locales. `.gitattributes` evita conversiones de finales de línea al clonar.
- Se verificaron 63 enlaces locales de las principales portadas y documentación, sin destinos faltantes.
- Se revisaron los archivos de texto candidatos en busca de patrones de claves privadas, tokens de GitHub y claves de OpenAI; no se detectaron coincidencias. Es una comprobación acotada de patrones, no una auditoría exhaustiva de seguridad.
- El conector leyó desde `main` el README y el archivo de pruebas tras la subida. GitHub conserva el repositorio como privado.

## Continuidad

La carpeta de trabajo de Codex y la carpeta conectada a GitHub son la misma. No hay sincronización automática: un cambio local necesita un commit y un envío para quedar en el remoto. Drive conserva sus propias copias fechadas; esta publicación no actualizó esas copias ni configuró Obsidian.

La guía [recorrido.md](recorrido.md) permite presentar el alcance, el aporte de la adaptación y una demostración. Los originales del profesor mantienen su atribución. La evidencia de Apple conserva el corte del 23.oct.2026 y el debate del 24.oct.2026.
