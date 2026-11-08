# Habilidad: Seguridad Crítica en Flasheo de ROMs y Kernel (Redmi Note 9 / Merlin)

## Bloqueos Inviolables
- **PROHIBIDO** modificar o sobreescribir las siguientes particiones bajo ninguna circunstancia:
  - `preloader`: riesgo de hard-brick irreversible sin puente test-point EDL / DA autorizado.
  - `nvram` / `nvdata`: pérdida permanente de calibración RF, IMEI y dirección MAC.
  - `persist`: pérdida de sensores (giroscopio, acelerómetro, proximidad) y claves DRM Widevine L1.
- Particiones modificables seguras: `boot`, `recovery`, `super` (`system`, `vendor`, `product`).
