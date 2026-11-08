# Habilidad: Generación de Visores 3D Interactivos Ligeros para Android

## Requisitos de Diseño
- Archivo `.html` único y autocontenido (Three.js importado vía CDN unpkg o cdnjs con fallback).
- Rendimiento móvil: Optimizado para navegadores Android (Chrome/Firefox/Samsung Internet), 60 FPS estables.
- Controles táctiles completos con `OrbitControls`: rotación con 1 dedo, zoom táctil con 2 dedos (pinch-to-zoom), paneo con 2 dedos.
- Iluminación: Iluminación de 3 puntos (Key light, Fill light, Back light) + luz ambiental suave y renderizador con `outputColorSpace = THREE.SRGBColorSpace`.
- Barra de herramientas flotante semitransparente con botones táctiles: Rotación automática (Play/Pause), Centrar vista, Selector de color/material y Modo estructura alámbrica (Wireframe).
