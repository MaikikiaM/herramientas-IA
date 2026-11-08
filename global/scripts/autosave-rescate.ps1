# Tarea programada y rescate de emergencia (autosave-rescate.ps1)
# Verificacion periodica de arbol de trabajo

$scriptPath = Join-Path $PSScriptRoot "autosave.ps1"
if (Test-Path $scriptPath) {
    & $scriptPath
} else {
    Write-Error "No se encontro autosave.ps1 en $PSScriptRoot"
}
