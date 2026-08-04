@echo off
title M7 ENTERPRISE - END-OF-DAY HARVEST
echo =============================================================
echo  [M7 OS] END-OF-DAY DATA HARVEST
echo  NOTE: launches the Claude Code agent to collect + scrub today's work.
echo  Runs ONLY when you double-click this file. Nothing auto-schedules.
echo =============================================================

:: 1. Agent harvests today's changes, scrubs brand law, writes the latest sync file
call claude "End-of-day harvest: collect text snippets, new review replies, and tracking updates modified today. Compile into a single file 03_Knowledge_Mat/active_context/ops_sync_latest.md (this folder is Google Drive-synced). Run the brand firewall: fix 'free inspection'->CPPA and '$0 down'->Full Restoration Coverage, flag any banned terms. Mark STATUS: PAUSED. Do not publish."

echo [M7 OS] Harvest complete. ops_sync_latest.md updated and syncing to Drive.
echo [M7 OS] Safe to close. Ko e hala 'o e fononga ko e faka'apa'apa.
pause
