@echo off
title M7 - Connect Your AI Tabs
color 0B
echo.
echo   ================================================
echo      M7  -  CONNECT YOUR AI TABS  (double-click me)
echo   ================================================
echo.
echo   STEP 1 - I am opening your 2 KEY FILES in Notepad.
echo            Paste each key on its line, then press Ctrl+S to save.
echo.
start "" notepad "%LOCALAPPDATA%\hermes\.env"
start "" notepad "%USERPROFILE%\.fcc\.env"
echo      [File 1] Hermes keys   - add line:  OPENROUTER_API_KEY=sk-or-YOURKEY
echo                              - (optional) HEYGEN_API_KEY=...  ELEVENLABS_API_KEY=...
echo      [File 2] DeepSeek keys  - add line:  DEEPSEEK_API_KEY=sk-YOURKEY
echo.
echo   STEP 2 - I am opening OpenRouter so you can grab that key.
start "" https://openrouter.ai/keys
echo.
echo   ================================================
echo   STEP 3 - The browser LOGINS. Open a NEW PowerShell and
echo            paste ONE line at a time. A browser opens - click Approve.
echo   ================================================
echo.
echo        kimi login
echo        hermes auth add xai-oauth              ^(Grok / Astros - needs X Premium+^)
echo        hermes auth add minimax-oauth          ^(MiniMax / Hermes Studio^)
echo        hermes -p muse mcp login higgsfield    ^(Higgsfield^)
echo.
echo   ================================================
echo   STEP 4 - After adding keys, RESTART the Studio
echo            ^(double-click "START PINEAPPLE STUDIO"^).
echo   ================================================
echo.
echo   Full details: 01_Command_Center\M7_CONNECT_EVERYTHING_CHEATSHEET.md
echo.
pause
