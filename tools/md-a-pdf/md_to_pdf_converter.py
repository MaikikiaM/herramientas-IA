import os
import sys
import json
import subprocess
import re

EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>__DOC_TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/mhchem.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.1/marked.min.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: __PAGE_MARGIN__;
    @top-left {
      content: "__HEADER_LEFT__";
      font-family: 'Segoe UI', 'Calibri', sans-serif;
      font-size: 8pt;
      color: __HEADER_COLOR__;
      font-weight: 600;
      border-bottom: 0.8pt solid __HEADER_RULE_COLOR__;
      padding-bottom: 3px;
    }
    @top-right {
      content: __HEADER_RIGHT__;
      font-family: 'Segoe UI', 'Calibri', sans-serif;
      font-size: 8pt;
      color: #64748B;
      border-bottom: 0.8pt solid __HEADER_RULE_COLOR__;
      padding-bottom: 3px;
    }
    @bottom-center {
      content: __FOOTER_CONTENT__;
      font-family: 'Segoe UI', 'Calibri', sans-serif;
      font-size: 8.5pt;
      color: #475569;
    }
  }

  @page cover-page {
    size: A4 portrait;
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
  }

  * {
    box-sizing: border-box;
    scrollbar-width: none !important;
    -ms-overflow-style: none !important;
  }

  ::-webkit-scrollbar {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
  }

  html, body {
    font-family: 'Segoe UI', 'Calibri', Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.45;
    color: #1a1a1a;
    margin: 0 !important;
    padding: 0 !important;
  }

  /* ---- PORTADA OFICIAL ESTILO PEAK ---- */
  .cover-page {
    page: cover-page;
    page-break-after: always;
    background-color: #1A3A2E;
    color: #ffffff;
    width: 210.2mm;
    height: 297.2mm;
    margin: 0;
    padding: 45mm 25mm 25mm 25mm;
    box-sizing: border-box;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
  }
  .cover-supertitle {
    font-size: 12pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #d1fae5;
    margin-bottom: 12px;
  }
  .cover-rule {
    width: 60%;
    height: 1.5pt;
    background-color: #C8921A;
    margin: 12px auto 28px auto;
    border: none;
  }
  .cover-title {
    font-size: 34pt;
    font-weight: bold;
    font-family: 'Georgia', 'Cambria', serif;
    margin: 0 0 10px 0;
  }
  .cover-tema {
    font-size: 22pt;
    font-weight: 600;
    color: #f1f5f9;
    margin: 0 0 16px 0;
  }
  .cover-type {
    font-size: 14pt;
    color: #e2e8f0;
    margin-bottom: 24px;
  }
  .cover-footer-org {
    margin-top: auto;
    margin-bottom: 25mm;
  }
  .cover-inst {
    font-size: 13pt;
    font-weight: 500;
    color: #ffffff;
  }
  .cover-course {
    font-size: 11pt;
    color: #94a3b8;
    margin-top: 6px;
  }

  /* ---- ENCABEZADOS Y SECCIONES ---- */
  h1 {
    font-size: 15.5pt;
    color: #2C5F2E;
    border-bottom: 1.5pt solid #2C5F2E;
    padding-bottom: 3px;
    margin-top: 4px;
    margin-bottom: 10px;
    font-weight: bold;
    page-break-after: avoid;
  }
  h2 {
    font-size: 12.5pt;
    color: #2C5F2E;
    border-bottom: 0.8pt solid #cbd5e1;
    padding-bottom: 2px;
    margin-top: 14px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }
  h3 {
    font-size: 11pt;
    color: #1b2a4a;
    margin-top: 12px;
    margin-bottom: 4px;
    page-break-after: avoid;
  }

  p { margin: 4px 0; }
  ul, ol { margin: 4px 0 8px 22px; padding: 0; }
  li { margin-bottom: 3px; }

  /* ---- TABLAS ESTILO BOOKTABS ---- */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
  }
  th {
    border-top: 2pt solid #1b2a4a;
    border-bottom: 1pt solid #1b2a4a;
    padding: 5px 8px;
    text-align: left;
    background-color: #f8fafc;
    color: #1b2a4a;
    font-weight: bold;
  }
  td {
    border-bottom: 0.5pt solid #e2e8f0;
    padding: 4px 8px;
    vertical-align: top;
  }
  tr:last-child td {
    border-bottom: 2pt solid #1b2a4a;
  }

  /* ---- CAJAS TCOLORBOX ESTILO EXACTO PEAK (ATTACH BOXED TITLE TO TOP LEFT) ---- */
  .tcolorbox {
    position: relative;
    margin: 14px 0 10px 0;
    padding: 11px 13px 7px 13px;
    border-radius: 0;
    page-break-inside: avoid;
  }
  .tcolorbox-title {
    position: absolute;
    top: -11px;
    left: 14px;
    color: #ffffff;
    font-family: 'Segoe UI', 'Calibri', sans-serif;
    font-size: 9pt;
    font-weight: bold;
    padding: 2px 10px;
    border-radius: 0;
    display: inline-block;
    line-height: 1.2;
  }

  /* Paleta oficial UCM */
  .box-enunciado {
    border: 1.2pt solid #4527A0;
    background-color: #EDE7F6;
  }
  .box-enunciado .tcolorbox-title { background-color: #4527A0; }

  .box-solucion {
    border: 1.2pt solid #004D40;
    background-color: #E0F2F1;
  }
  .box-solucion .tcolorbox-title { background-color: #004D40; }

  .box-resultado {
    border: 1.2pt solid #E65100;
    background-color: #FFF8E1;
  }
  .box-resultado .tcolorbox-title { background-color: #E65100; }

  .box-tutor {
    border: 1.2pt solid #880E4F;
    background-color: #FCE4EC;
  }
  .box-tutor .tcolorbox-title { background-color: #880E4F; }

  .box-def {
    border: 1.2pt solid #2C5F2E;
    background-color: #E8F5E9;
  }
  .box-def .tcolorbox-title { background-color: #2C5F2E; }

  .box-formula {
    border: 1.2pt solid #E65100;
    background-color: #FFF3E0;
  }
  .box-formula .tcolorbox-title { background-color: #E65100; }

  .box-var {
    border: 1.2pt solid #6A1B9A;
    background-color: #F3E5F5;
  }
  .box-var .tcolorbox-title { background-color: #6A1B9A; }

  .box-intu {
    border: 1.2pt solid #0277BD;
    background-color: #E1F5FE;
  }
  .box-intu .tcolorbox-title { background-color: #0277BD; }

  .box-nota {
    border: 1.2pt solid #BF360C;
    background-color: #FBE9E7;
  }
  .box-nota .tcolorbox-title { background-color: #BF360C; }

  .box-alert {
    border: 1.2pt solid #C62828;
    background-color: #FFEBEE;
  }
  .box-alert .tcolorbox-title { background-color: #C62828; }

  #content {
    max-width: 100%;
    overflow: hidden;
  }
  .katex-display {
    max-width: 100%;
    margin: 7px 0 !important;
    overflow: hidden;
  }
  .tcolorbox .katex-display {
    font-size: 0.94em;
  }
  table {
    max-width: 100%;
  }
  img {
    max-width: 100%;
  }

  .page-break {
    page-break-before: always !important;
    break-before: page !important;
    height: 0;
    margin: 0;
    padding: 0;
  }
  .box-enunciado {
    page-break-inside: avoid;
  }
  /* ---- ESTILOS ESPECÍFICOS PARA FORMULARIO (2 CARAS ULTRA-COMPACTO) ---- */
  body.is-formulario {
    font-size: 8pt;
    line-height: 1.22;
  }
  body.is-formulario h1 {
    font-size: 11pt;
    margin: 0 0 4px 0;
    padding-bottom: 2px;
  }
  body.is-formulario h2 {
    font-size: 9.2pt;
    margin: 6px 0 2px 0;
    padding-bottom: 1px;
  }
  body.is-formulario h3 {
    font-size: 8.4pt;
    margin: 4px 0 1px 0;
  }
  body.is-formulario p {
    margin: 1.5px 0;
  }
  body.is-formulario ul, body.is-formulario ol {
    margin: 1px 0 3px 14px;
  }
  body.is-formulario li {
    margin-bottom: 0.5px;
  }
  body.is-formulario table {
    margin: 3px 0;
    font-size: 7.6pt;
  }
  body.is-formulario th, body.is-formulario td {
    padding: 1.5px 4px;
  }
  body.is-formulario .katex-display {
    margin: 2px 0 !important;
    font-size: 0.88em;
  }
  body.is-formulario .tcolorbox {
    margin: 5px 0 3px 0;
    padding: 6px 8px 3px 8px;
  }
  body.is-formulario .tcolorbox-title {
    top: -8px;
    font-size: 7.2pt;
    padding: 1px 5px;
  }
  body.is-formulario hr {
    margin: 4px 0;
    border-top: 0.5pt solid #cbd5e1;
  }

  /* ---- GRID Y CAJAS TEMABOX (ESTILO FORMULARIO CANÓNICO) ---- */
  .tcbraster {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3.5mm;
    width: 100%;
    box-sizing: border-box;
    padding-top: 8px;
    margin-bottom: 0;
  }
  .temaBox {
    position: relative;
    background-color: #FFF3E0;
    border: 1.2pt solid #E65100;
    border-radius: 0;
    margin-top: 8px;
    padding: 7px 8px 4px 8px;
    font-size: 7.6pt;
    line-height: 1.20;
    box-sizing: border-box;
    break-inside: avoid;
    page-break-inside: avoid;
  }
  .temaBox-title {
    position: absolute;
    top: -8px;
    left: 8px;
    background-color: #E65100;
    color: #ffffff;
    font-family: 'Segoe UI', 'Calibri', 'Liberation Sans', sans-serif;
    font-size: 7.5pt;
    font-weight: bold;
    padding: 1px 7px;
    border-radius: 0;
    line-height: 1.2;
    white-space: nowrap;
    z-index: 10;
  }
  .temaBox p {
    margin: 1.5px 0;
  }
  .temaBox strong {
    color: #000000;
    font-weight: 700;
  }
  .temaBox .katex-display {
    margin: 2px 0 !important;
    font-size: 0.88em;
  }
  .temaBox table {
    margin: 2px 0;
    font-size: 7.2pt;
    border-collapse: collapse;
  }
  .temaBox th, .temaBox td {
    padding: 1px 3px;
    border-bottom: 0.5pt solid #d97706;
  }
  .temaBox th {
    border-top: 1pt solid #E65100;
    border-bottom: 1pt solid #E65100;
  }
  .temaBox ul, .temaBox ol {
    margin: 1px 0 2px 12px;
    padding: 0;
  }
  .temaBox li {
    margin-bottom: 1px;
  }

</style>
</head>
<body __BODY_CLASS__>

__COVER_HTML__

<div style="padding-top: 5px;">
  <div id="content"></div>
</div>

<script>
const rawMd = __MARKDOWN_JSON__;

function transformAlerts(html) {
  // Enunciado / Nota / Tip / Warning / Important
  return html.replace(/<blockquote>\s*<p>\[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION)\]([\s\S]*?)<\/blockquote>/gi, function(match, type, content) {
    type = type.toUpperCase();
    let boxClass = 'box-def';
    let defaultTitle = 'Definición';

    // 1. Extraer título personalizado si la caja empieza con <strong>...</strong>
    let customTitle = '';
    const titleMatch = content.match(/^\s*<strong>\s*(.*?)\s*<\/strong>\s*:?\s*(?:<br\s*\/?>)?/i);
    if (titleMatch) {
      customTitle = titleMatch[1].trim();
      // Eliminar el <strong> completo del contenido para no duplicar
      content = content.replace(titleMatch[0], '');
      // Limpiar prefijos de etiquetas internas si estuvieran presentes
      customTitle = customTitle.replace(/^(?:formulaBox|varBox|intuBox|defBox|alertBox|tutorBox|tutorialBox|resultadoBox|enunciadoBox)\s*:?\s*/i, '');
    }

    // 2. Determinar la clase de caja y título por defecto
    const textToCheck = (type + ' ' + customTitle + ' ' + content).toLowerCase();

    if (textToCheck.includes('enunciado')) {
      boxClass = 'box-enunciado';
      defaultTitle = 'Enunciado';
    } else if (type === 'IMPORTANT' || textToCheck.includes('resultado')) {
      boxClass = 'box-resultado';
      defaultTitle = 'Resultado';
    } else if (type === 'WARNING' || textToCheck.includes('alert') || textToCheck.includes('atención') || textToCheck.includes('trampa') || textToCheck.includes('cuidado') || textToCheck.includes('error')) {
      boxClass = 'box-alert';
      defaultTitle = '¡Atención!';
    } else if (textToCheck.includes('glosario') || textToCheck.includes('símbolos') || textToCheck.includes('varbox')) {
      boxClass = 'box-var';
      defaultTitle = 'Glosario de Símbolos';
    } else if (textToCheck.includes('fórmula') || textToCheck.includes('ecuación') || textToCheck.includes('formulabox')) {
      boxClass = 'box-formula';
      defaultTitle = 'Fórmula Clave';
    } else if (textToCheck.includes('intuición') || textToCheck.includes('intubox') || textToCheck.includes('¿por qué')) {
      boxClass = 'box-intu';
      defaultTitle = 'Intuición Conceptual';
    } else if (type === 'TIP' || textToCheck.includes('estrategia') || textToCheck.includes('tutor') || textToCheck.includes('orientación')) {
      boxClass = 'box-tutor';
      defaultTitle = 'Orientación y Estrategia';
    } else if (textToCheck.includes('definición') || textToCheck.includes('postulado') || textToCheck.includes('hipótesis') || textToCheck.includes('defbox')) {
      boxClass = 'box-def';
      defaultTitle = 'Definición';
    }

    // 3. Título limpio para la pestaña superior
    customTitle = customTitle.replace(/^(?:glosario(?:\s+de\s+símbolos)?|fórmula(?:\s+clave)?|definición|intuición(?:\s+conceptual)?|atención|estrategia|orientación|enunciado|resultado)\s*:\s*/i, '').trim();
    customTitle = customTitle.replace(/[:.]+$/, '').trim();

    let finalTitle = defaultTitle;
    if (customTitle && customTitle.toLowerCase() !== defaultTitle.toLowerCase()) {
      if (customTitle.length <= 32) {
        finalTitle = `${defaultTitle}: ${customTitle}`;
      } else if (customTitle.length <= 42) {
        finalTitle = customTitle;
      }
    }

    // 4. Limpieza total de cualquier residuo tipo intuBox, defBox, TutorBox, etc.
    content = content.replace(/(?:<strong>)?\s*(?:formulaBox|varBox|intuBox|defBox|alertBox|tutorBox|tutorialBox|resultadoBox|enunciadoBox):?\s*(?:<\/strong>)?/gi, '');
    content = content.replace(/^\s*:\s*/, '');
    content = content.replace(/<p>\s*<\/p>/g, '');

    return `<div class="tcolorbox ${boxClass}"><div class="tcolorbox-title">${finalTitle}</div>${content}</div>`;
  });
}

marked.setOptions({
  gfm: true,
  breaks: false
});

function protectMath(text) {
  const mathBlocks = [];
  text = text.replace(/\$\$([\s\S]*?)\$\$/g, function(match) {
    mathBlocks.push(match);
    return `%%%MATH_BLOCK_${mathBlocks.length - 1}%%%`;
  });
  text = text.replace(/\$([^\$\n]+?)\$/g, function(match) {
    mathBlocks.push(match);
    return `%%%MATH_BLOCK_${mathBlocks.length - 1}%%%`;
  });
  return { text, mathBlocks };
}

function restoreMath(html, mathBlocks) {
  return html.replace(/%%%MATH_BLOCK_(\d+)%%%/g, function(match, index) {
    return mathBlocks[parseInt(index, 10)];
  });
}

const { text: protectedMd, mathBlocks } = protectMath(rawMd);

function preprocessBoxes(mdText) {
  let res = mdText.replace(/:::\s*temaBox\s*([^\n]+)\n([\s\S]*?)\n:::\s*(?:\n|$)/g, function(match, title, content) {
    let innerHtml = marked.parse(content.trim());
    return `<div class="temaBox">\n<div class="temaBox-title">${title.trim()}</div>\n${innerHtml}\n</div>\n`;
  });
  res = res.replace(/:::\s*tcbraster\b[^\n]*/g, '<div class="tcbraster">');
  res = res.replace(/\n:::\s*(?=\n|$)/g, '\n</div>');
  return res;
}

let preprocessed = preprocessBoxes(protectedMd);
let parsed = marked.parse(preprocessed);
parsed = transformAlerts(parsed);
parsed = restoreMath(parsed, mathBlocks);
document.getElementById('content').innerHTML = parsed;

renderMathInElement(document.getElementById('content'), {
  delimiters: [
    {left: "$$", right: "$$", display: true},
    {left: "$", right: "$", display: false},
    {left: "\\\\[", right: "\\\\]", display: true},
    {left: "\\\\(", right: "\\\\)", display: false}
  ],
  throwOnError: false
});
</script>
</body>
</html>
"""

def generate_cover_html(title, doc_type, subtitle):
    return f"""
<div class="cover-page">
  <div class="cover-supertitle">Química General &nbsp;|&nbsp; Grado en Ciencias Físicas</div>
  <hr class="cover-rule">
  <div class="cover-title">Tema 1</div>
  <div class="cover-tema">Estructura Atómica y Tabla Periódica</div>
  <div class="cover-type">{doc_type}</div>
  <hr class="cover-rule">
  <div class="cover-footer-org">
    <div class="cover-inst">Universidad Complutense de Madrid</div>
    <div class="cover-course">Curso Académico 2025–2026 &nbsp;•&nbsp; Chemde</div>
  </div>
</div>
"""

def convert_md_to_pdf(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Eliminar YAML frontmatter si existe para que no se renderice en el cuerpo
    md_text = re.sub(r'^---\s*\n[\s\S]*?\n---\s*\n', '', md_text)

    base_name = os.path.splitext(os.path.basename(md_path))[0]
    
    if "Ejercicios" in base_name:
        doc_type = "Hoja de Problemas — Resuelta Paso a Paso"
        subtitle = "Tema 1: Problemas Resueltos"
        is_formulario = False
    elif "Formulario" in base_name:
        doc_type = "Formulario Oficial de Examen"
        subtitle = "Tema 1: Formulario"
        is_formulario = True
    else:
        doc_type = "Apuntes Teóricos Completos para Estudiar desde Cero"
        subtitle = "Tema 1: Apuntes de Teoría"
        is_formulario = False

    if is_formulario:
        cover_html = ""
        page_margin = "13mm 11mm 10mm 11mm"
        header_left = "Formulario Oficial: Tema 1 · Estructura Atómica — Grado en Ciencias Físicas (UCM)"
        header_right = '"Cara " counter(page) " de 2 \\A0\\A0•\\A0\\A0 Chemde"'
        header_color = "#2B4C7E"
        header_rule_color = "#2B4C7E"
        footer_content = "none"
        body_class = 'class="is-formulario"'
    else:
        cover_html = generate_cover_html("Tema 1", doc_type, subtitle)
        page_margin = "22mm 20mm 20mm 20mm"
        header_left = "Química General — Grado en Ciencias Físicas"
        header_right = f'"{subtitle}"'
        header_color = "#2C5F2E"
        header_rule_color = "#2C5F2E"
        footer_content = "counter(page)"
        body_class = ""
    
    json_md = json.dumps(md_text)
    html = (HTML_TEMPLATE
            .replace("__DOC_TITLE__", base_name.replace("_", " "))
            .replace("__DOC_SUBTITLE__", subtitle)
            .replace("__COVER_HTML__", cover_html)
            .replace("__PAGE_MARGIN__", page_margin)
            .replace("__HEADER_LEFT__", header_left)
            .replace("__HEADER_RIGHT__", header_right)
            .replace("__HEADER_COLOR__", header_color)
            .replace("__HEADER_RULE_COLOR__", header_rule_color)
            .replace("__FOOTER_CONTENT__", footer_content)
            .replace("__BODY_CLASS__", body_class)
            .replace("__MARKDOWN_JSON__", json_md))

    temp_html = md_path + ".temp.html"
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html)

    abs_html = os.path.abspath(temp_html)
    abs_pdf = os.path.abspath(pdf_path)

    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=6000",
        f"--print-to-pdf={abs_pdf}",
        f"file:///{abs_html.replace(os.sep, '/')}"
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    
    if os.path.exists(temp_html):
        os.remove(temp_html)

    if os.path.exists(abs_pdf) and os.path.getsize(abs_pdf) > 1000:
        print(f"[OK] Generado {os.path.basename(pdf_path)}: {os.path.getsize(abs_pdf)} bytes")
        return True
    else:
        print(f"[ERROR] No se pudo generar {pdf_path}. Detalle: {res.stderr}")
        return False

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        convert_md_to_pdf(sys.argv[1], sys.argv[2])
    else:
        print("Uso: python md_to_pdf_converter.py <archivo.md> <archivo.pdf>")
