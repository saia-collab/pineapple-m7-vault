@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo 🍍 Initializing Unified Pineapple Contractors M7 Agent Engine Matrix...

REM --- Port map ------------------------------------------------------------
REM   3000  reserved for SEO Office (Agentic OS hardcodes localhost:3000/office)
REM   3001  OpenSEO (Docker)          3100  Paperclip
REM   3737  Agentic OS  (its start script hardcodes PORT=3737)
REM   3939  M7 Command Center (server.js)
REM   8082  FCC proxy                 9119  Hermes dashboard
REM   Do NOT put the Agentic OS on 3000 — it squats SEO Office's port and the
REM   SEO Office tab then iframes the Agentic OS into itself.
REM -------------------------------------------------------------------------

REM --- Hot-relaunch protection: port-based purge of orphaned/locked instances before re-binding ---
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3939') do taskkill /f /pid %%a 2>nul
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3737') do taskkill /f /pid %%a 2>nul
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3100') do taskkill /f /pid %%a 2>nul
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8082') do taskkill /f /pid %%a 2>nul

start /b cmd /c "set PORT=3939 && npm start"
start /b /d "C:\Pineapple Contractors M7\03_Knowledge_Mat\00_Atlas\templates\agent-os-pack-2026-07-31\source" cmd /c "set PORT=3737 && npm start"
start /b cmd /c "npx fcc-server --port 8082"
echo 📎 Launching Paperclip AI Company Daemon Engine...
start /b cmd /c "npx paperclipai run"
echo 🔷 Command Center (3939), Agentic OS (3737), FCC Proxy (8082), and Paperclip (3100) are operating persistently.
