# 📊 Monitor de Tokens y Costes - Google AI Pro

Herramienta diseñada para calcular tu consumo real de tokens en Google Antigravity y comparar la equivalencia económica con respecto a las tarifas de API comerciales (Google AI Studio / Vertex AI) frente a tu cuota fija mensual de **Google AI Pro / Google One AI Premium (21,99 €/mes)**.

---

## 🚀 Cómo ejecutarlo

### Opción 1: Con doble clic (Modo Fácil)
Haz doble clic en:
```text
ejecutar_monitor.bat
```
Esto mostrará el reporte en la consola y abrirá automáticamente un **panel visual interactivo en tu navegador**.

### Opción 2: Desde PowerShell / Terminal
Abre PowerShell en esta carpeta y ejecuta:

```powershell
# Ver el consumo del mes actual en la consola:
python monitor.py

# Ver el consumo y además abrir el panel gráfico en el navegador:
python monitor.py --html

# Ver todo el histórico acumulado (todos los meses):
python monitor.py --all
```

---

## 🔎 ¿Cómo funciona?

1. **Lectura centralizada:**  
   Antigravity guarda el historial de todas las sesiones en `C:\Users\<tu-usuario>\.gemini\antigravity\brain\`.  
   El monitor lee esos ficheros locales sin importar en qué carpeta o disco se encuentren tus proyectos (`Proyectos IA varios`, `Antigravity`, etc.).
2. **Tokens contabilizados:**  
   - **Input:** Tokens de contexto, archivos leídos, prompts.
   - **Output:** Tokens generados por la IA (código, explicaciones).
   - **Cache:** Tokens reutilizados en memoria de contexto.
3. **Cálculo de ahorro (ROI):**  
   Aplica las tarifas oficiales por millón de tokens de Gemini 3.8 Flash, Gemini Pro, Gemini 4 Argon y Gemini 4 Hydrogen, calcula el coste equivalente en dólares y euros, y lo compara con tu cuota fija mensual de 21,99 €.

---

## ⚙️ Personalización de tarifas

Puedes modificar el archivo `pricing.json` en cualquier momento para:
- Ajustar el precio mensual de tu suscripción si cambia.
- Actualizar las tarifas de tokens por millón de Google Cloud.
- Cambiar la tasa de cambio USD/EUR.
