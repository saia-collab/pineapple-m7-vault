@echo off
REM M7 Paperclip Daemon — auto-start wrapper (used by the "M7 Paperclip Daemon" scheduled task)
cd /d "%USERPROFILE%"
npx paperclipai run
