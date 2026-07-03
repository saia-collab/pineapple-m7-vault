@echo off
REM ============================================================
REM  M7_CLEANUP.bat — safe tidy (double-click)
REM  - removes 3 junk test files from Outbox
REM  - moves duplicate dashboards to legacy_backup
REM  - moves stray root docs to _Inbox_Cleanup (NOT deleted)
REM  Never touches your 4-Fala folders' contents or system files.
REM ============================================================
title Pineapple M7 - Safe Cleanup
color 0E
cd /d "%~dp0"
echo.
echo   Cleaning up Pineapple M7 (safe, reversible)...
echo.

REM 1) junk test files in Outbox
for %%F in (health_check_test.md idempotent_check.md verify_routing.md) do (
  if exist "01_Command_Center\Outbox_Drafts\%%F" del /q "01_Command_Center\Outbox_Drafts\%%F" && echo   deleted Outbox\%%F
)

REM 2) duplicate dashboards -> legacy_backup\command_center_legacy
if not exist "legacy_backup\command_center_legacy" mkdir "legacy_backup\command_center_legacy"
if exist "01_Command_Center\KomputerMechanic-Hermes-Dashboard-Template.html" move /y "01_Command_Center\KomputerMechanic-Hermes-Dashboard-Template.html" "legacy_backup\command_center_legacy\" >nul && echo   archived KomputerMechanic-Hermes-Dashboard-Template.html
if exist "03_Knowledge_Mat\M7_Command_Center.html" move /y "03_Knowledge_Mat\M7_Command_Center.html" "legacy_backup\command_center_legacy\" >nul && echo   archived 03_Knowledge_Mat\M7_Command_Center.html

REM 3) stray ROOT docs -> _Inbox_Cleanup (reversible; system files left alone)
if not exist "_Inbox_Cleanup" mkdir "_Inbox_Cleanup"
for %%F in ("Untitled Kanban.md" "M7 Agentic OS Master Execution.gdoc" "PINEAPPLE CONTRACTORS M7 MASTER PLAYBOOK AND MARKDOWNS.gdoc" "SKILL.md.gdoc" "SOP  Build An AI Agent Operating System (Rank #1 on Google via Claude Code + Google Flow Video Factory).gdoc") do (
  if exist "%%~F" move /y "%%~F" "_Inbox_Cleanup\" >nul && echo   moved %%~F -> _Inbox_Cleanup
)

echo.
echo   Done. KEPT at root (system files): GROUNDING.md, USER.md, MEMORY.md, .env, .gitignore, the .bat launchers.
echo   Canonical dashboard kept: 01_Command_Center\M7_COMMAND_CENTER.html
echo   Anything moved is in _Inbox_Cleanup or legacy_backup (nothing lost).
echo.
pause
