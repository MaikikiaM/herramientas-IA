# Script de lanzamiento para PowerShell
param(
    [switch]$All,
    [switch]$Html
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

$argsList = @("monitor.py")
if ($All) { $argsList += "--all" }
if ($Html) { $argsList += "--html" }

python @argsList
