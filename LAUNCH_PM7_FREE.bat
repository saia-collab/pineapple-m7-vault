@echo off
title PM7 -- FREE MODE (OmniRoute :20128)
color 0E
echo ============================================================
echo   PINEAPPLE M7 -- FREE MODE
echo   Claude Code routes through OmniRoute (free models, $0)
echo   NOT your paid Opus subscription.
echo ============================================================
echo.

set "ANTHROPIC_BASE_URL=http://127.0.0.1:20128"
set "ANTHROPIC_API_KEY=sk-pm7-free-local-token"
set "OPENAI_BASE_URL=http://127.0.0.1:20128/v1"
set "OPENAI_API_KEY=sk-pm7-free-local-token"
set "PM7_CANONICAL_ROOT=C:\Pineapple Contractors M7"

echo [1/2] Checking OmniRoute gateway on http://127.0.0.1:20128 ...
powershell -NoProfile -Command "try { Invoke-RestMethod -Uri 'http://127.0.0.1:20128/v1/models' -TimeoutSec 4 ^| Out-Null; Write-Host '[PASS] OmniRoute ACTIVE -- free routing ready.' -ForegroundColor Green } catch { Write-Host '[STOP] OmniRoute not responding. Start the Studio / OmniRoute first, then rerun this.' -ForegroundColor Red }"

echo.
echo [2/2] Launching Claude Code (FREE) in %PM7_CANONICAL_ROOT% ...
cd /d "%PM7_CANONICAL_ROOT%"
claude
pause
