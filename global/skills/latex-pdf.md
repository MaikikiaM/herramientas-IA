# Habilidad: Compilación LaTeX a PDF de Alta Fidelidad

## Directrices de Compilación
- Motor preferente: `pdflatex -interaction=nonstopmode -halt-on-error <fichero.tex>`
- Para fórmulas matemáticas avanzadas y química: usar paquetes `amsmath`, `amssymb`, `chemformula` o `mhchem`.
- Tipografía académica estándar: Computer Modern / Latin Modern (`lmodern`).
- Márgenes de página: `\usepackage[a4paper, margin=20mm]{geometry}`.
- Limpieza tras compilación: mantener `.tex` y `.pdf`; eliminar auxiliares volátiles (`.aux`, `.log`, `.out`, `.toc`) si no se requieren para depuración.
