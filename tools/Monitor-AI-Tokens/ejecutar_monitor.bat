@echo off
chcp 65001 > nul
title Monitor de Tokens Google AI Pro
cd /d "%~dp0"

echo ========================================================
echo   Iniciando Monitor de Tokens y Costes Google AI Pro
echo ========================================================
echo.

python monitor.py --html

echo.
pause
