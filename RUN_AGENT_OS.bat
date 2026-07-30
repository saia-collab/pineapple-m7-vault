@echo off
REM ============================================================
REM  RUN_AGENT_OS.bat — start the Pineapple M7 Agent OS server
REM  Serves the Command Center at http://localhost:3939
REM  Zero installs — runs on Node's built-ins.
REM ============================================================
title Pineapple M7 - Agent OS
color 0E
cd /d "%~dp0"
echo.
echo   Starting Pineapple M7 Agent OS on http://localhost:3939 ...
echo   (Leave this window open. Ctrl+C to stop.)
echo.
start "" "http://localhost:3939"
node server.js
if errorlevel 1 (
  echo.
  echo   Node not found? Install Node.js from https://nodejs.org  then double-click this again.
)
pause
