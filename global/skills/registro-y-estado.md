# Habilidad: Gestión de Memoria Dual (ESTADO.md + registro.txt)

## Protocolo
1. **Nivel 1 — `docs/ia/ESTADO.md`:**
   - Resumen ejecutivo vivo (< 50 líneas).
   - Componentes activos, arquitectura, estado de tests y prioridades inmediatas.
   - Leído obligatoriamente al inicio de cada conversación.
2. **Nivel 2 — `registro.txt`:**
   - Bitácora cronológica acumulativa en la raíz del proyecto.
   - Cada entrada contiene fecha, sesión, prompts del usuario, acciones técnicas aplicadas y lista de ficheros modificados.
   - Al inicio de sesión se leen las últimas 80 líneas. Para consultas históricas, se ejecutan búsquedas puntuales con ripgrep o `Select-String`.
