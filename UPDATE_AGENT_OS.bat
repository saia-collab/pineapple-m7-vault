@echo off
title Pineapple M7 - Safe Agent OS Update
echo ============================================================
echo   Backs up, applies the newest pack, preserves your M7
echo   customizations, rebuilds, restarts, verifies :3000.
echo   (Drop the new agent-os-pack .zip in Downloads first.)
echo ============================================================
echo.
pause
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp004_Tech_Lab\update_agent_os.ps1"
echo.
echo Done. Hard-refresh http://localhost:3000
pause
