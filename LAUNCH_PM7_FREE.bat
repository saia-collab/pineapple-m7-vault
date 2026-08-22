@echo off
setlocal
title PM7 Free-Routed Claude Code
color 0E

set "PM7_ROOT=%~dp0"
echo ============================================================
echo   PINEAPPLE M7 - FREE/LOW-COST ROUTING THROUGH OMNIROUTE
echo   This mode does not use your Claude subscription login.
echo ============================================================
echo.

where omniroute.cmd >nul 2>nul
if errorlevel 1 where omniroute >nul 2>nul
if errorlevel 1 (
  echo [STOP] OmniRoute CLI is not installed or is not on PATH.
  echo        Install/update from the official project, then run this again:
  echo        npm install -g omniroute
  pause
  exit /b 1
)

powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command ^
  "$ready=$false; try { $r=Invoke-WebRequest -UseBasicParsing -Uri 'http://127.0.0.1:20128/v1/models' -TimeoutSec 4; $ready=$r.StatusCode -lt 500 } catch { if ($_.Exception.Response -and [int]$_.Exception.Response.StatusCode -in 401,403) { $ready=$true } }; if (-not $ready) { exit 1 }"

if errorlevel 1 (
  echo [INFO] OmniRoute is not running. Starting the PM7 Studio stack first...
  call "%PM7_ROOT%LAUNCH_PM7_STUDIO.bat"
  if errorlevel 1 exit /b 1
)

echo.
echo [INFO] OmniRoute will inject the correct endpoint and scoped token.
echo        No API key is stored in this launcher.
echo.
cd /d "%PM7_ROOT%"
call omniroute launch
set "PM7_EXIT=%ERRORLEVEL%"
if not "%PM7_EXIT%"=="0" (
  echo.
  echo [FAILED] OmniRoute could not launch Claude Code. Run PM7_REPAIR_AND_VERIFY.bat.
  pause
)
exit /b %PM7_EXIT%
