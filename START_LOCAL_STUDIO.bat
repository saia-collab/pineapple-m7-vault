@echo off
title M7 - START LOCAL STUDIO (delegates to LAUNCH_ALL)
color 0E
echo =============================================================
echo   M7 LOCAL STUDIO
echo   Your MASTER launcher is LAUNCH_ALL.bat on the Desktop.
echo   It starts: Agent OS (3000) + server_m7 + fcc-server (8082)
echo              + Paperclip (3100) + OmniRoute (20128)
echo   This file just runs it so there is ONE source of truth.
echo =============================================================
if exist "%USERPROFILE%\OneDrive\Desktop\LAUNCH_ALL.bat" (
  call "%USERPROFILE%\OneDrive\Desktop\LAUNCH_ALL.bat"
) else if exist "%USERPROFILE%\Desktop\LAUNCH_ALL.bat" (
  call "%USERPROFILE%\Desktop\LAUNCH_ALL.bat"
) else (
  echo [ERROR] LAUNCH_ALL.bat not found on Desktop. Tell Claude where you moved it.
  pause
)
