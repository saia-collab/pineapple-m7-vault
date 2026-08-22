@echo off
setlocal
title PM7 Gemini CLI through OmniRoute
color 0B

set "PM7_ROOT=%~dp0"

echo ============================================================
echo   PM7 - GEMINI CLI THROUGH OMNIROUTE
echo ============================================================
echo.

where omniroute.cmd >nul 2>nul
if errorlevel 1 where omniroute >nul 2>nul
if errorlevel 1 (
  echo [STOP] OmniRoute is not installed or is not on PATH.
  pause
  exit /b 1
)

where gemini.cmd >nul 2>nul
if errorlevel 1 where gemini >nul 2>nul
if errorlevel 1 (
  echo [STOP] Google Gemini CLI is not installed or is not on PATH.
  echo        Install it from Google's official Gemini CLI instructions.
  pause
  exit /b 1
)

echo [INFO] Starting Gemini CLI through OmniRoute with a temporary,
echo        isolated Gemini configuration. No key is written to this vault.
echo.
cd /d "%PM7_ROOT%"
call omniroute run gemini --model auto/best-chat
set "PM7_EXIT=%ERRORLEVEL%"
if not "%PM7_EXIT%"=="0" pause
exit /b %PM7_EXIT%
