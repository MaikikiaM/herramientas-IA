# Habilidad: Gestión de Memoria Dual (ESTADO.md + registro.txt)

## Protocolo
1. **Nivel 1 — `docs/ia/ESTADO.md`:**
   - Resumen ejecutivo vivo (< 50 líneas).
   - Componentes activos, arquitectura, estado de tests y prioridades inmediatas.
   - Leído obligatoriamente al inicio de cada conversación.
2. **Nivel 2 — `registro.txt`:**
   - Bitácora cronológica acumulativa e inmutable en la raíz del proyecto (`SESIÓN: DD/MM/AAAA - TÍTULO`).
   - **Regla inviolable de Prompts Literales:** Cada sesión DEBE abrir con `- Prompts literales del usuario:`, copiando palabra por palabra y con marca horaria `[DD/MM/AAAA HH:MM]: "..."` todos los mensajes originales del usuario (con sus faltas, coloquialismos o comandos slash intactos). Si la sesión fue compactada, recuperar el texto exacto desde `transcript_full.jsonl` / `transcript.jsonl`.
   - **PROHIBIDO sustituir o parafrasear** los prompts literales por un resumen u objetivo; `- Objetivo:` es estrictamente opcional y sólo puede ir *debajo* de `- Prompts literales del usuario:`.
   - Tras los prompts literales, detallar acciones técnicas aplicadas, ficheros creados/modificados y resultados verificados.
   - Al inicio de sesión se leen las últimas 80 líneas. Para consultas históricas, se ejecutan búsquedas puntuales con ripgrep o `Select-String`.
