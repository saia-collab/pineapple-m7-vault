@echo off
setlocal
title Configure PM7 AI Clients through OmniRoute
color 0B

echo ============================================================
echo   PM7 - CONFIGURE CLAUDE, CODEX, OPENCODE, AND CURSOR
echo ============================================================
echo.
echo This uses OmniRoute's current model catalog and credential context.
echo Cursor will print manual in-app steps because Cursor stores model
echo configuration in its private application database.
echo.

where omniroute.cmd >nul 2>nul
if errorlevel 1 where omniroute >nul 2>nul
if errorlevel 1 (
  echo [STOP] OmniRoute CLI is not installed or is not on PATH.
  pause
  exit /b 1
)

call omniroute setup-claude
if errorlevel 1 goto :failed
call omniroute setup-codex
if errorlevel 1 goto :failed
call omniroute setup-opencode
if errorlevel 1 goto :failed
call omniroute setup-cursor
if errorlevel 1 goto :failed
call omniroute doctor

echo.
echo [DONE] Client profiles were generated from the live catalog.
echo        Complete the printed Cursor Settings steps, then run
echo        CONFIGURE_PM7_GOOGLE_AI.bat for Gemini/Antigravity, then
echo        PM7_REPAIR_AND_VERIFY.bat.
pause
exit /b 0

:failed
echo.
echo [FAILED] A setup command stopped. Start OmniRoute, confirm an active
echo          endpoint/token in its dashboard, and run this launcher again.
pause
exit /b 1
