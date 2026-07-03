@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo 🍍 Initializing Unified Pineapple Contractors M7 Agent Engine Matrix...

REM --- Hot-relaunch protection: port-based purge of orphaned/locked instances before re-binding ---
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3737') do taskkill /f /pid %%a 2>nul
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3000') do taskkill /f /pid %%a 2>nul
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3100') do taskkill /f /pid %%a 2>nul
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8082') do taskkill /f /pid %%a 2>nul

start /b cmd /c "set PORT=3737 && npm start"
start /b /d "C:\Pineapple Contractors M7\03_Knowledge_Mat\00_Atlas\templates\agent-os-pack-2026-06-29\source" cmd /c "set PORT=3000 && npm start"
start /b cmd /c "npx fcc-server --port 8082"
echo 📎 Launching Paperclip AI Company Daemon Engine...
start /b cmd /c "npx paperclipai run"
echo 🟢 Core Suite (3737), Legacy Dashboard (3000), FCC Proxy (8082), and Paperclip (3100) are operating persistently.
