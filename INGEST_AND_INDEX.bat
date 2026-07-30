@echo off
chcp 65001 >nul
REM ============================================================
REM  INGEST_AND_INDEX.bat — file new skills, then rebuild the catalog.
REM
REM  Many SOPs say "double-click INGEST_AND_INDEX.bat". That launcher had
REM  been retired to Launcher_Archive\ while the docs kept naming it, so the
REM  instruction dead-ended. Restored here as a thin wrapper over the two
REM  scripts that do the work:
REM     04_Tech_Lab\scripts\m7_skill_intake.py   (file zips/folders/loose)
REM     04_Tech_Lab\scripts\m7_catalog.py        (rebuild CATALOG.md)
REM
REM  Safe to re-run. Move-only — nothing is deleted.
REM ============================================================
title Pineapple M7 - Ingest and Index
color 0E
cd /d "%~dp0"

echo.
echo   🍍 M7 INGEST + INDEX
echo   Inbox: 04_Tech_Lab\skills_inbox
echo.

REM Resolve a working Python (py launcher first on Windows, then python).
set "PY="
where py >nul 2>&1 && set "PY=py"
if not defined PY (where python >nul 2>&1 && set "PY=python")
if not defined PY (
  echo   ERROR: Python not found on PATH.
  echo   Install from https://python.org then re-run this file.
  echo.
  pause
  exit /b 1
)

echo   [1/2] Filing new skills and templates...
%PY% "04_Tech_Lab\scripts\m7_skill_intake.py"
if errorlevel 1 (
  echo   ERROR: intake failed — see the message above. Catalog not rebuilt.
  echo.
  pause
  exit /b 1
)

echo.
echo   [2/2] Rebuilding the catalog...
%PY% "04_Tech_Lab\scripts\m7_catalog.py"
if errorlevel 1 (
  echo   ERROR: catalog rebuild failed — see the message above.
  echo.
  pause
  exit /b 1
)

echo.
echo   Done. Catalog: 03_Knowledge_Mat\00_Atlas\CATALOG.md
echo   Intake log:    04_Tech_Lab\logs\skill_intake_log.json
echo.
pause
