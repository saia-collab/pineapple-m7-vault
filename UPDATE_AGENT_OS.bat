@echo off
chcp 65001 >nul
title Pineapple M7 - Safe Agent OS Update
echo.
echo   🍍 PINEAPPLE M7 — ONE-BUTTON AGENT OS UPDATE
echo   ============================================
echo   Backs up, applies the newest pack, preserves your
echo   M7 branding + SEO customizations, rebuilds, restarts.
echo.
echo   (Drop the new agent-os-pack .zip in your Downloads first.)
echo.
pause
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp004_Tech_Lab\update_agent_os.ps1"
echo.
echo   Done. Press any key to close.
pause >nul
