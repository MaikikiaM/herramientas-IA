# Script de Salvaguarda y Autoguardado Proactivo (autosave.ps1)
# Hook ejecutado al finalizar sesion o tareas operativas

$ErrorActionPreference = "Stop"

$workspaceRoot = $PSScriptRoot
if ($workspaceRoot -like "*\Herramientas-IA\global\scripts") {
    $workspaceRoot = (Get-Item $workspaceRoot).Parent.Parent.Parent.FullName
}

Write-Output "[*] Verificando estado git en proyectos de $workspaceRoot..."

$projects = Get-ChildItem -Path $workspaceRoot -Directory | Where-Object { 
    $_.Name -notin @("Archivo", ".agents", "__pycache__") 
}

foreach ($proj in $projects) {
    $projPath = $proj.FullName
    if (Test-Path "$projPath\.git") {
        Push-Location $projPath
        try {
            $status = git status --porcelain
            if ($status) {
                Write-Output "[$($proj.Name)] Detectados cambios no guardados. Verificando politicas de seguridad..."
                
                # Chequeo de secretos y archivos pesados
                $hasForbidden = $false
                $statusLines = $status -split "`r?`n"
                foreach ($line in $statusLines) {
                    if ($line -match "\.(pdf|stl|3mf|apk|jar|glb|npz|npy)$" -or $line -match "(node_modules|build|\.env)") {
                        Write-Warning "[$($proj.Name)] Archivo binario o secreto detectado en status: $line. Omitiendo stage indiscriminado."
                        $hasForbidden = $true
                        break
                    }
                }
                
                if (-not $hasForbidden) {
                    git add -A
                    $dateStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
                    git commit -m "chore(autosave): salvaguarda automatica de sesion [$dateStr]"
                    Write-Output "[$($proj.Name)] Commit de salvaguarda generado exitosamente."
                    
                    # Intentar push si hay remoto configurado
                    $remotes = git remote
                    if ($remotes -contains "origin") {
                        git push origin main 2>$null
                        Write-Output "[$($proj.Name)] Sincronizado con remoto origin/main."
                    }
                }
            }
        } catch {
            Write-Warning "[$($proj.Name)] Advertencia en autoguardado: $_"
        } finally {
            Pop-Location
        }
    }
}

Write-Output "[OK] Ciclo de autosave completado."
