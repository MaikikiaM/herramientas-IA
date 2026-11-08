"""Generador de Visores 3D Interactivos Ligeros para Android / Navegadores Web.
Produce archivos .html autocontenidos optimizados para pantallas táctiles móviles.
"""

import os
import sys

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, maximum-scale=1.0">
  <title>{TITLE}</title>
  <style>
    body {{
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: radial-gradient(circle at 50% 50%, #20242e 0%, #0d0f12 100%);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      touch-action: none;
      -webkit-user-select: none;
      user-select: none;
    }}
    #viewer-container {{
      width: 100vw;
      height: 100vh;
      display: block;
    }}
    .ui-overlay {{
      position: absolute;
      top: 16px;
      left: 16px;
      color: #f0f0f0;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
      pointer-events: none;
    }}
    .ui-overlay h1 {{
      font-size: 1.1rem;
      margin: 0 0 4px 0;
      font-weight: 600;
      letter-spacing: 0.5px;
    }}
    .ui-overlay p {{
      font-size: 0.8rem;
      margin: 0;
      color: #9aa4b2;
    }}
    .toolbar {{
      position: absolute;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      gap: 10px;
      background: rgba(22, 27, 34, 0.75);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      padding: 8px 14px;
      border-radius: 30px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }}
    .btn {{
      background: transparent;
      border: none;
      color: #e6edf3;
      padding: 8px 12px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 500;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: background 0.2s, transform 0.1s;
    }}
    .btn:active {{
      background: rgba(255,255,255,0.15);
      transform: scale(0.96);
    }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
  <div id="viewer-container"></div>
  <div class="ui-overlay">
    <h1>{TITLE}</h1>
    <p>1 dedo: Rotar | 2 dedos: Zoom / Paneo</p>
  </div>
  <div class="toolbar">
    <button class="btn" id="btn-rotate">⏯ Auto</button>
    <button class="btn" id="btn-wireframe">🕸 Malla</button>
    <button class="btn" id="btn-reset">🎯 Centrar</button>
  </div>

  <script>
    const container = document.getElementById('viewer-container');
    const scene = new THREE.Scene();

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 40, 70);

    const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true, powerPreference: "high-performance" }});
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    container.appendChild(renderer.domElement);

    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.autoRotate = true;
    controls.autoRotateSpeed = 1.8;

    // Iluminacion estudio
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0xfff8ee, 1.2);
    keyLight.position.set(30, 60, 40);
    scene.add(keyLight);

    const fillLight = new THREE.DirectionalLight(0xddeeff, 0.6);
    fillLight.position.set(-30, 20, -30);
    scene.add(fillLight);

    // Geometria personalizada
    const group = new THREE.Group();
    {GEOMETRY_CODE}
    scene.add(group);

    // Ajuste al redimensionar
    window.addEventListener('resize', () => {{
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }});

    // Controles de barra
    document.getElementById('btn-rotate').addEventListener('click', () => {{
      controls.autoRotate = !controls.autoRotate;
    }});

    let wireframeState = false;
    document.getElementById('btn-wireframe').addEventListener('click', () => {{
      wireframeState = !wireframeState;
      group.traverse(child => {{
        if (child.isMesh && child.material) {{
          child.material.wireframe = wireframeState;
        }}
      }});
    }});

    document.getElementById('btn-reset').addEventListener('click', () => {{
      camera.position.set(0, 40, 70);
      controls.target.set(0, 0, 0);
      controls.update();
    }});

    function animate() {{
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    }}
    animate();
  </script>
</body>
</html>
"""

def build_viewer(title, geometry_code, output_path):
    html = HTML_TEMPLATE.format(TITLE=title, GEOMETRY_CODE=geometry_code)
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Visor 3D generado en: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Uso programmatico: import generar_visor_html")
