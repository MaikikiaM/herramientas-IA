# Protocolo Operativo: Herramientas-IA (Infraestructura Global y Utilidades)

Este proyecto opera bajo el Protocolo Global definido en `~/.gemini/config/AGENTS.md` y actúa como repositorio maestro de reglas, skills, hooks y plantillas compartidas.

---

## 1. Cabecera Temporal Obligatoria
Toda respuesta del asistente debe iniciar con:
```markdown
⏱️ **[Prompt: HH:MM:SS | Respuesta: HH:MM:SS]**
```

---

## 2. Memoria en Dos Niveles
- `docs/ia/ESTADO.md`: Resumen ejecutivo vivo de máximo 50 líneas (leer al inicio de cada sesión).
- `registro.txt`: Bitácora continua indexable e inmutable en la raíz del proyecto (`SESIÓN: DD/MM/AAAA - TÍTULO`).
  - **Regla obligatoria de prompts literales:** Cada entrada DEBE comenzar por `- Prompts literales del usuario:` copiando **palabra por palabra y sin resumir** cada mensaje enviado por el usuario con su fecha/hora (`  * [DD/MM/AAAA HH:MM]: "<texto literal exacto>"`).
  - **Prohibido sustituir por objetivos:** Nunca parafrasear ni reemplazar el prompt del usuario por `- Objetivo:`. Si se incluye un `- Objetivo:`, sólo puede aparecer *después* de `- Prompts literales del usuario:`. Tras compactación, recuperar los mensajes literales desde `transcript_full.jsonl` / `transcript.jsonl`.

---

## 3. Reglas Específicas de Herramientas-IA
- **Sincronización global:** Cualquier cambio en protocolos, skills o hooks de `global/` debe mantenerse sincronizado con `~/.gemini/config/` (y `plantillas/`), sin introducir referencias ni accesos a directorios prohibidos.
- **Herramientas:** Mantener `tools/Monitor-AI-Tokens/` libre de caches (`__pycache__/`, `reporte_consumo.html`) en los commits de Git y validar sintaxis/pruebas antes de confirmar.

---

## 4. Sincronización Proactiva con GitHub
- Tras concluir cada tarea funcional o corrección de bugs, ejecutar:
  ```powershell
  git add -A
  git commit -m "<tipo>(<alcance>): <descripción concisa en español>"
  git push origin main
  ```
