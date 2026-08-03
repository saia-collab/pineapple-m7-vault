@echo off
chcp 65001 >nul
title M7 ENTERPRISE - MORNING ENGINE SWEEP
cd /d "%~dp0"

REM ============================================================
REM  AM_STARTUP.bat — morning sweep: brief, then start the studio.
REM  Runs ONLY when you double-click it. Nothing is auto-scheduled.
REM
REM  Ports (see 01_Command_Center\PORT_MAP.md):
REM    3737  Agentic OS / Local Studio  <- this file starts it
REM    3000  RESERVED for SEO Office — never start the studio here
REM ============================================================

REM One line to update when you unzip a newer pack:
set "STUDIO=%~dp003_Knowledge_Mat\00_Atlas\templates\agent-os-pack-2026-07-30\source"

echo =============================================================
echo  [M7 OS] MORNING WORKSPACE SWEEP
echo  Launches the Claude Code agent to scan + brief, then the studio.
echo =============================================================
echo.

REM --- 1) Agent writes today's brief (PAUSED — publishes nothing) -----------
call claude "Scan 01_Command_Center/ and 03_Knowledge_Mat/ for files modified in the last 24h. Write an extreme-density bulleted executive brief for today into 03_Knowledge_Mat/active_context/ops_sync_latest.md. Cross-reference GSC striking-distance keywords for the top 3 daily targets (Frisco, Plano, Lewisville). Apply M7 brand law (CPPA, IKO Certified, zero green). Mark STATUS: PAUSED. Do not publish anything."

echo.
echo  [M7 OS] Brief written to 03_Knowledge_Mat\active_context\ops_sync_latest.md
echo  [M7 OS] Google Drive Desktop will sync it to the cloud.
echo.

REM --- 2) Start the Local Studio on its own port ---------------------------
if not exist "%STUDIO%\package.json" (
  echo  [M7 OS] ERROR: studio not found at:
  echo           %STUDIO%
  echo  [M7 OS] Unzipped a newer pack? Update the STUDIO line at the top of
  echo          this file to the new agent-os-pack-YYYY-MM-DD folder.
  echo.
  pause
  exit /b 1
)

REM Clear an orphaned instance still holding 3737 from a previous run.
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3737') do taskkill /f /pid %%a 2>nul

echo  [M7 OS] Starting Local Studio at http://localhost:3737 ...
start /b /d "%STUDIO%" cmd /c "set PORT=3737 && npm start"

echo  [M7 OS] Studio starting. Give it ~20s, then open http://localhost:3737
echo.
pause
