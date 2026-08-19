@echo off
title PM7 Local Studio Master Launcher
color 0A
echo ============================================================
echo   PINEAPPLE CONTRACTORS M7 - LOCAL AI STUDIO LAUNCHER
echo ============================================================
echo.

set "ANTHROPIC_BASE_URL=http://127.0.0.1:20128"
set "ANTHROPIC_API_KEY=sk-pm7-free-local-token"
set "OPENAI_BASE_URL=http://127.0.0.1:20128/v1"
set "OPENAI_API_KEY=sk-pm7-free-local-token"
set "PM7_CANONICAL_ROOT=C:\Pineapple Contractors M7"

echo [1/2] Verifying OmniRoute Gateway on http://127.0.0.1:20128...
powershell -NoProfile -Command "try { $r = Invoke-RestMethod -Uri 'http://127.0.0.1:20128/v1/models' -TimeoutSec 3; Write-Host '[PASS] OmniRoute Gateway ACTIVE on Port 20128!' -ForegroundColor Green } catch { Write-Host '[WARNING] OmniRoute not responding. Make sure omniroute is running in another terminal.' -ForegroundColor Yellow }"

echo.
echo [2/2] Launching Claude Code in %PM7_CANONICAL_ROOT%...
cd /d "%PM7_CANONICAL_ROOT%"
claude
pause
