@echo off
setlocal
title PM7 Claude Subscription Mode
color 09

set "ANTHROPIC_BASE_URL="
set "ANTHROPIC_API_KEY="
set "ANTHROPIC_AUTH_TOKEN="
set "OPENAI_BASE_URL="
set "OPENAI_API_KEY="
set "PM7_ROOT=%~dp0"

echo ============================================================
echo   PINEAPPLE M7 - CLAUDE SUBSCRIPTION MODE
echo   OmniRoute variables are cleared for this process only.
echo ============================================================
echo.

where claude.cmd >nul 2>nul
if errorlevel 1 where claude >nul 2>nul
if errorlevel 1 (
  echo [STOP] Claude Code is not installed or is not on PATH.
  pause
  exit /b 1
)

cd /d "%PM7_ROOT%"
call claude
set "PM7_EXIT=%ERRORLEVEL%"
if not "%PM7_EXIT%"=="0" pause
exit /b %PM7_EXIT%
