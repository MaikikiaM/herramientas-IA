# Guardia de Seguridad de Rutas Privadas
# PreToolUse Hook para bloquear accesos a directorios vetados

param (
    [string]$CommandText = "",
    [string]$TargetPath = ""
)

$forbidden = @(
    "C:\Users\migue\Marta",
    "C:\Users\migue\Zomboid",
    "C:\Users\migue\Copia de seguridad antiguo ordenador",
    "Marta",
    "Zomboid",
    "Copia de seguridad antiguo ordenador"
)

$inputToCheck = "$CommandText $TargetPath"

foreach ($pattern in $forbidden) {
    if ($inputToCheck -match [regex]::Escape($pattern)) {
        Write-Error "ACCESO DENEGADO POR SEGURIDAD: La ruta o término '$pattern' corresponde a un directorio privado estrictamente prohibido."
        exit 1
    }
}

exit 0
