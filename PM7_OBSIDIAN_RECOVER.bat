@echo off
setlocal
title PM7 Obsidian Memory Recovery
color 0B
set "PM7_ROOT=%~dp0"
set "PM7_SCRIPT=%PM7_ROOT%04_Tech_Lab\scripts\PM7_OBSIDIAN_MEMORY_RECOVERY.ps1"

if not exist "%PM7_SCRIPT%" (
  echo [STOP] Missing recovery script: %PM7_SCRIPT%
  pause
  exit /b 1
)

powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%PM7_SCRIPT%" -VaultRoot "%PM7_ROOT:~0,-1%" -RestartObsidian
set "PM7_EXIT=%ERRORLEVEL%"
echo.
if "%PM7_EXIT%"=="0" (
  echo [DONE] Obsidian recovery checks completed.
) else (
  echo [ATTENTION] One or more checks need action.
)
echo Open the newest PM7_OBSIDIAN_MEMORY_RECOVERY receipt in:
echo   01_Command_Center\Outbox_Drafts
echo.
echo SECURITY: rotate the Local REST credential inside Obsidian settings.
echo Never paste it into this window, Git, Markdown, or a launcher.
pause
exit /b %PM7_EXIT%
