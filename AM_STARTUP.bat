@echo off
title M7 ENTERPRISE - MORNING ENGINE SWEEP
echo =============================================================
echo  [M7 OS] MORNING WORKSPACE SWEEP
echo  NOTE: this launches the Claude Code agent to scan + brief.
echo  It runs ONLY when you double-click this file. Nothing is auto-scheduled.
echo =============================================================

:: 1. Agent scans for overnight changes and writes today's brief (PAUSED, no publishing)
call claude "Scan 01_Command_Center/ and 03_Knowledge_Mat/ for files modified in the last 24h. Write an extreme-density bulleted executive brief for today into 03_Knowledge_Mat/active_context/ops_sync_latest.md. Cross-reference GSC striking-distance keywords for the top 3 daily targets (Frisco, Plano, Lewisville). Apply M7 brand law (CPPA, IKO Certified, zero green). Mark STATUS: PAUSED. Do not publish anything."

echo [M7 OS] Brief written to 03_Knowledge_Mat/active_context/ops_sync_latest.md
echo [M7 OS] Google Drive Desktop will sync it to the cloud.
echo [M7 OS] Starting Local Studio at http://localhost:3000 ...
cd source
npm run dev
