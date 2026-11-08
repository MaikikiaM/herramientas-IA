# Habilidad: Conversión de Markdown a PDF con KaTeX

## Arquitectura de Renderizado
- Se procesa el archivo `.md` generando un HTML temporal con:
  - `marked.min.js` para parseo de Markdown.
  - `katex.min.js`, `auto-render.min.js` y `mhchem.min.js` para renderizado matemático y químico.
  - Tipografía Latin Modern Roman emulada en CSS (`font-family: "Latin Modern Roman", serif`).
- Compilación headless mediante Microsoft Edge:
  `msedge --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=<salida.pdf> <html_temporal>`
- Destino del PDF: Siempre en la subcarpeta correspondiente de `Apuntes-y-Ejercicios/`.
