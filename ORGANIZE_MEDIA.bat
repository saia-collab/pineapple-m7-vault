@echo off
REM ============================================================
REM  ORGANIZE_MEDIA.bat — one-click: rename + file your reels
REM  Move-only. Nothing deleted. Safe to re-run.
REM ============================================================
title Pineapple M7 - Organize Media
color 0E
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp004_Tech_Lab\scripts\ORGANIZE_MEDIA.ps1"
echo.
echo  Your reels are now in 02_Media_Vault (03_BY_CITY / 02_READY_TO_POST / 05_TEAM_BRAND).
echo  Post first: WhyPineappleRoofing + PropertyManagers.
echo.
pause
