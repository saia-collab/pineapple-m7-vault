@echo off
setlocal
title PM7 Local Studio
color 0B

set "PM7_ROOT=%~dp0"
set "PM7_LAUNCHER=%PM7_ROOT%04_Tech_Lab\Pineapple_Agent_OS\START-PINEAPPLE-AGENT-OS.ps1"
if not exist "%PM7_LAUNCHER%" set "PM7_LAUNCHER=%PM7_ROOT%04_Tech_Lab\scripts\agentos_launcher_fixes_2026-08-16\START-PINEAPPLE-AGENT-OS.ps1"

echo ============================================================
echo   PINEAPPLE M7 - START LOCAL STUDIO
echo ============================================================
echo.

if not exist "%PM7_LAUNCHER%" (
  echo [STOP] The Local Studio PowerShell launcher is missing.
  echo        Expected under 04_Tech_Lab\Pineapple_Agent_OS or scripts.
  pause
  exit /b 1
)

powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%PM7_LAUNCHER%"
set "PM7_EXIT=%ERRORLEVEL%"
if not "%PM7_EXIT%"=="0" (
  echo.
  echo [FAILED] Local Studio did not become ready. Error %PM7_EXIT%.
  pause
)
exit /b %PM7_EXIT%
