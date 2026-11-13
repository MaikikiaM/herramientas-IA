$WshShell = New-Object -ComObject WScript.Shell
$DesktopPath = [Environment]::GetFolderPath("Desktop")
if (-not $DesktopPath -or -not (Test-Path $DesktopPath)) {
    $DesktopPath = "C:\Users\migue\Desktop"
}

$icoPath = "C:\Users\migue\Antigravity\Herramientas-IA\tools\Monitor-AI-Tokens\logo.ico"

# 1. Acceso directo que actualiza y abre el reporte
$Shortcut1 = $WshShell.CreateShortcut("$DesktopPath\Monitor Tokens IA (Actualizar).lnk")
$Shortcut1.TargetPath = "C:\Users\migue\Antigravity\Herramientas-IA\tools\Monitor-AI-Tokens\abrir_monitor.bat"
$Shortcut1.WorkingDirectory = "C:\Users\migue\Antigravity"
$Shortcut1.WindowStyle = 7 # Minimized
if (Test-Path $icoPath) {
    $Shortcut1.IconLocation = "$icoPath,0"
}
$Shortcut1.Description = "Actualiza los datos de consumo de IA y abre el panel en el navegador"
$Shortcut1.Save()

# 2. Acceso directo directo al archivo HTML
$Shortcut2 = $WshShell.CreateShortcut("$DesktopPath\Reporte Consumo IA.lnk")
$Shortcut2.TargetPath = "C:\Users\migue\Antigravity\Herramientas-IA\tools\Monitor-AI-Tokens\reporte_consumo.html"
$Shortcut2.WorkingDirectory = "C:\Users\migue\Antigravity\Herramientas-IA\tools\Monitor-AI-Tokens"
if (Test-Path $icoPath) {
    $Shortcut2.IconLocation = "$icoPath,0"
}
$Shortcut2.Description = "Abre el reporte HTML de consumo de IA"
$Shortcut2.Save()

Write-Output "Shortcuts updated successfully on: $DesktopPath"
