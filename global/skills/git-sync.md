# Habilidad: Sincronización Automática con Repositorios Git

## Ciclo de Trabajo
1. Tras completar cualquier bloque funcional o modificación estructural:
   - Revisar `git status --porcelain`.
   - Validar que no se incluyan archivos vetados (`*.pdf`, `*.stl`, `*.3mf`, `*.apk`, `*.jar`, `build/`, `node_modules/`, `.env`).
   - Validar que ningún archivo supere los 50 MB.
2. Ejecutar:
   ```powershell
   git add -A
   git commit -m "<tipo>(<alcance>): <descripción concisa en español>"
   git push origin main
   ```
