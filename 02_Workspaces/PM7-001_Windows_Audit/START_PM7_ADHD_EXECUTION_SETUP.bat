@echo off
setlocal
set "INSTALLER=%~dp0INSTALL_PM7_ADHD_COMMAND_CENTER.ps1"
set "AUDIT=%~dp0PM7_WINDOWS_STORAGE_AND_INSTALLER_AUDIT.ps1"

if not exist "%INSTALLER%" (
  echo Missing command-center installer: %INSTALLER%
  pause
  exit /b 1
)

if not exist "%AUDIT%" (
  echo Missing Windows audit script: %AUDIT%
  pause
  exit /b 1
)

echo PM7 PLAY 1 OF 1
echo.
echo This will install new PM7 planning/shared-memory files and run a read-only audit.
echo It will NOT update Agent OS, replace current, uninstall apps, delete files, or publish anything.
echo.

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%INSTALLER%"
if errorlevel 1 (
  echo.
  echo Command-center setup stopped with an error.
  echo Take a screenshot and bring it back to ChatGPT.
  pause
  exit /b 1
)

echo.
echo Command-center setup passed. Starting the read-only Windows audit.
echo The folder-size scan may take several minutes.
echo.

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%AUDIT%"
if errorlevel 1 (
  echo.
  echo The Windows audit stopped with an error.
  echo Take a screenshot and bring it back to ChatGPT.
  pause
  exit /b 1
)

echo.
echo PM7-001 audit finished.
echo Upload 00_READ_ME_FIRST.md and PM7_WINDOWS_STORAGE_AUDIT.json to ChatGPT.
echo Then STOP. Do not begin another PM7 task today.
pause
exit /b 0

