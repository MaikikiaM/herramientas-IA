# Habilidad: Despliegue y Validación en Servidores Paper 1.21.x

## Protocolo de Actualización
1. Compilar plugin Java con Gradle: `./gradlew shadowJar`.
2. Verificar que el artefacto generado es `teams-totems-0.1.0-SNAPSHOT.jar` (sin `-all`).
3. Detener el proceso del servidor si está corriendo.
4. Eliminar el directorio `server/plugins/.paper-remapped/` para evitar que Paper cargue bytecode desactualizado en caché.
5. Copiar el nuevo JAR a `server/plugins/teams-totems.jar`.
6. Comprobar que el hash SHA256 (`Get-FileHash`) del origen y destino coincide.
7. Arrancar servidor y verificar en consola `[PluginRemapper] Done remapping...`.
