@echo off
title PM7 -- PAID MODE (Claude Opus subscription)
color 09
echo ============================================================
echo   PINEAPPLE M7 -- PAID MODE
echo   Claude Code runs on your real Claude Opus subscription
echo   (best quality). No OmniRoute, no free routing.
echo ============================================================
echo.

REM Clear any free-routing env vars so Claude Code uses your logged-in subscription.
set "ANTHROPIC_BASE_URL="
set "ANTHROPIC_API_KEY="
set "OPENAI_BASE_URL="
set "OPENAI_API_KEY="
set "PM7_CANONICAL_ROOT=C:\Pineapple Contractors M7"

echo [info] Free-routing env cleared. Using Claude subscription login.
echo        (If it ever asks you to log in, run:  claude  then /login )
echo.
echo Launching Claude Code (PAID) in %PM7_CANONICAL_ROOT% ...
cd /d "%PM7_CANONICAL_ROOT%"
claude
pause
