@echo off
setlocal
title PM7 Google AI and Antigravity Setup
color 0B

echo ============================================================
echo   PM7 - GOOGLE AI / ANTIGRAVITY SAFE SETUP
echo ============================================================
echo.
echo This opens OmniRoute Providers for the required human login.
echo It does not store credentials in Git and does not enable paid
echo Antigravity credit overages or traffic interception.
echo.

where omniroute.cmd >nul 2>nul
if errorlevel 1 where omniroute >nul 2>nul
if errorlevel 1 (
  echo [STOP] OmniRoute is not installed or is not on PATH.
  pause
  exit /b 1
)

set "ANTIGRAVITY_CREDITS=off"
start "" "http://127.0.0.1:20128/dashboard/providers"

echo In the OmniRoute browser page:
echo   1. Connect Google Gemini or add a Google AI Studio API key.
echo   2. Connect Antigravity only through its normal OAuth button.
echo   3. Keep Antigravity paid-credit overages OFF.
echo   4. Do not enable MITM, stealth, or forced-credit options.
echo.
echo After the provider shows connected, close this window and run:
echo   PM7_REPAIR_AND_VERIFY.bat
echo.
call omniroute doctor
pause
exit /b 0
