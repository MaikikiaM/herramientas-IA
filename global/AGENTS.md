# Protocolo Operativo Global de Asistencia y Agentes IA

Este documento rige el comportamiento de todos los agentes y sesiones en este espacio de trabajo.

---

## 1. Cabecera Temporal Obligatoria en Cada Respuesta
Toda respuesta del asistente DEBE comenzar exactamente con el encabezado temporal en la primera línea:
```markdown
⏱️ **[Prompt: HH:MM:SS | Respuesta: HH:MM:SS]**
```
- **Hora del Prompt:** Obtenida directamente de los metadatos reales de la interacción (`<ADDITIONAL_METADATA>` o `transcript.jsonl`), NUNCA del resumen de contexto (`<CONTEXT_SUMMARY>`).
- **Hora de Respuesta:** Hora exacta del sistema al momento de emitir la contestación (`Get-Date -Format 'HH:mm:ss'`).
- **Estilo directo:** No emitir saludos genéricos, disculpas de relleno ni introducciones innecesarias tras la cabecera.

---

## 2. Protocolo de Memoria en Dos Niveles
Cada proyecto mantendrá dos niveles de contexto persistente:
1. **`docs/ia/ESTADO.md` (Nivel 1 — Estado Vivo):**
   - Archivo conciso (~30-40 líneas) que resume la misión, arquitectura, estado actual de componentes, compilación y próximas tareas prioritarias.
   - El agente lo lee siempre al inicio de cada sesión para adquirir contexto instantáneo.
2. **`registro.txt` (Nivel 2 — Historial Continuo Infinito):**
   - Bitácora cronológica e inmutable en la raíz de cada proyecto.
   - Contiene bloques fechados (`SESIÓN: DD/MM/AAAA - TÍTULO`) con prompts del usuario, decisiones técnicas tomadas, archivos creados/modificados y resultados de pruebas.
   - Al abrir sesión, el agente lee las últimas 80 líneas para contexto inmediato y utiliza búsquedas específicas (`Select-String` / `grep`) sobre el histórico completo cuando necesita recordar decisiones pasadas.

---

## 3. Protocolo de Sincronización Automática con GitHub (`git-sync`)
Tras finalizar con éxito cualquier tarea funcional, implementación, corrección de bugs o reorganización, el agente debe ejecutar proactivamente:
```powershell
git add -A
git commit -m "<tipo>(<alcance>): <descripción clara del cambio en español>"
git push origin main
```
- **Convención de commits:** `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.
- **Filtro estricto de seguridad:** Antes de confirmar, verificar que ningún archivo supere los 50 MB y que no se incluyan secretos (`ghp_`, tokens, claves de API, `.env`) ni binarios vetados (`*.pdf`, `*.stl`, `*.3mf`, `*.apk`, `build/`, `node_modules/`).

---

## 4. Directorios Estrictamente Prohibidos
Bajo ninguna circunstancia ni petición, el asistente podrá leer, copiar, listar, modificar ni indexar en repositorios los siguientes directorios privados:
- `C:\Users\migue\Marta`
- `C:\Users\migue\Zomboid`
- `C:\Users\migue\Copia de seguridad antiguo ordenador`

Cualquier intento o comando que involucre estas rutas debe ser bloqueado inmediatamente por el guardia de seguridad (`guardia-rutas.ps1`).

---

## 5. Arquitectura de Proyectos y Repositorios Git
Todos los proyectos residen en `C:\Users\migue\Antigravity\<Proyecto>\`.
Para evitar corrupciones y desacoplar la sincronización de archivos de los metadatos de Git, los directorios `.git` se gestionan enlazados en `C:\Users\migue\.repos\<proyecto>.git` mediante `--separate-git-dir`.
