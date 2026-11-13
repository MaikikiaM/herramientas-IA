# ESTADO DEL PROYECTO: Herramientas-IA

**Última actualización:** 13/11/2026
**Responsable:** MaikikiaM / Antigravity AI

## 1. Misión y Alcance
Repositorio central de herramientas, habilidades globales, scripts de seguridad, automatización de autoguardado y plantillas base de Antigravity. Proporciona la infraestructura operativa que comparten todos los demás proyectos.

## 2. Arquitectura y Componentes
- `global/`: Protocolo maestro `AGENTS.md`, configuración `hooks.json`, scripts de seguridad (`guardia-rutas.ps1`, `autosave.ps1`) y catálogo de 8 habilidades (`skills/`).
- `tools/`:
  - `Monitor-AI-Tokens/`: Monitor de consumo de tokens y costes de IA en tiempo real con dashboard HTML (soporte para Gemini 3.8 Flash, Pro, 4 Argon y 4 Hydrogen).
  - `md-a-pdf/`: Motor de compilación headless Markdown a PDF.
  - `visor-3d-html/`: Generador de visores 3D Three.js táctiles para Android.
  - `precios-ia/`: Calculadoras de precios de modelos Gemini y consumo.
- `plantillas/`: Plantillas base (`AGENTS.md`, `ESTADO.md`, `registro.txt`, `.gitignore`).

## 3. Estado de Compilación y Automatización
- Hooks `PreToolUse` y `Stop` validados y activos.
- Accesos directos de escritorio apuntando a `Herramientas-IA\tools\Monitor-AI-Tokens`.
- Scripts de sincronización Git con verificación estricta de secretos y binarios pesados.

## 4. Tareas Prioritarias Inmediatas
- [x] Configuración inicial e instalación en `~/.gemini/config/`.
- [x] Enlace remoto con repositorio de GitHub (`Herramientas-IA`).
