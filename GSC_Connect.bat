@echo off
chcp 65001 >nul
title Pineapple M7 - Connect / Reconnect Google Search Console
echo ============================================================
echo   GOOGLE SEARCH CONSOLE - CONNECT / RECONNECT
echo   Opens OpenSEO. Click "Search Performance" then
echo   "Connect Google Search Console" and sign in.
echo ============================================================
echo.

REM --- Is OpenSEO up on :3001? ---
netstat -aon | findstr ":3001" | findstr "LISTENING" >nul
if %errorlevel%==0 (
  echo [OK] OpenSEO is running on :3001. Opening...
) else (
  echo [!] OpenSEO not detected on :3001.
  echo     Start it first: double-click LAUNCH_ALL.bat in the vault root,
  echo     or open the OpenSEO tab in the dashboard, then run this again.
  echo.
  echo     Opening the dashboard so you can start it...
  start "" "http://localhost:3737"
  timeout /t 3 /nobreak >nul
)

start "" "http://localhost:3001"
echo.
echo Signed in already? You are done - it is collecting data.
echo Need to reconnect? Search Performance ^> Connect Google Search Console.
echo.
timeout /t 4 /nobreak >nul

