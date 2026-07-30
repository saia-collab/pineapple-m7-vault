@echo off
REM ============================================================
REM  M7_DOCTOR.bat — checks every connection (non-human checklist)
REM  Verifies: folders, core files, firewall, M7 Command Center (3939),
REM  Obsidian REST API (27123), Outbox writable.
REM  Ports: see 01_Command_Center\PORT_MAP.md
REM ============================================================
title Pineapple M7 - Connection Doctor
color 0B
python "%~dp004_Tech_Lab\m7_doctor.py"
if errorlevel 1 py "%~dp004_Tech_Lab\m7_doctor.py"
echo.
pause
