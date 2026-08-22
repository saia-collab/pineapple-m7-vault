@echo off
setlocal
title PM7 Repair and Verification
color 0B
set "PM7_SCRIPT=%~dp004_Tech_Lab\scripts\PM7_OMNIROUTE_REPAIR_AND_VERIFY.ps1"

if not exist "%PM7_SCRIPT%" (
  echo [STOP] Missing verifier: %PM7_SCRIPT%
  pause
  exit /b 1
)

powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%PM7_SCRIPT%" -StartServices -RunModelTests
set "PM7_EXIT=%ERRORLEVEL%"
echo.
if "%PM7_EXIT%"=="0" (
  echo [DONE] Core checks passed. The receipt is in Outbox_Drafts.
) else (
  echo [ATTENTION] One or more core checks failed. Open the newest
  echo             PM7_LOCAL_VERIFY receipt in Outbox_Drafts.
)
pause
exit /b %PM7_EXIT%
