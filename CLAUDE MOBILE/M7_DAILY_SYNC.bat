@echo off
REM ============================================================================
REM  PINEAPPLE CONTRACTORS M7 — DAILY AUTO-SYNC (hands-free)
REM  Runs the whole maintenance loop so the OS updates itself into the workflow:
REM    intake new drops -> firewall M7 output -> index + catalog -> telemetry
REM    -> mobile snapshot -> sync-status for the dashboard -> git snapshot.
REM  Outbox Shield stays on. Register with REGISTER_DAILY_SYNC.bat (Task Scheduler).
REM  Ko e hala 'o e fononga ko e faka'apa'apa.
REM ============================================================================
setlocal
set ROOT=C:\Pineapple Contractors M7
set S=%ROOT%\04_Tech_Lab\Scripts
set LOG=%ROOT%\04_Tech_Lab\logs\daily_sync_log.md
cd /d "%ROOT%"
for /f "tokens=*" %%t in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd_HH:mm"') do set NOW=%%t

echo. >> "%LOG%"
echo ## Daily Sync %NOW% >> "%LOG%"

echo [M7] 1/7 Ingest any new inbox drops...
python "%S%\m7_skill_intake.py" --root "%ROOT%" >> "%LOG%" 2>&1

echo [M7] 2/7 Brand firewall over M7-generated output (Command Center + Outbox + Factory)...
python "%S%\brand_firewall.py" --root "%ROOT%\01_Command_Center" --fix >> "%LOG%" 2>&1
python "%S%\brand_firewall.py" --root "%ROOT%\05_Campaign_Factory" --fix >> "%LOG%" 2>&1

echo [M7] 3/7 Rebuild Atlas index + catalog...
python "%S%\m7_aggregate.py" >> "%LOG%" 2>&1
python "%S%\m7_catalog.py" >> "%LOG%" 2>&1

echo [M7] 4/7 Refresh avatar telemetry + history...
python "%S%\m7_scoring.py" --demo > "%ROOT%\04_Tech_Lab\logs\last_scoring.json" 2>&1

echo [M7] 5/7 Write dashboard sync-status...
python -c "import json,datetime,os;r=r'%ROOT%';sk=len([d for d in os.listdir(os.path.join(r,'04_Tech_Lab','skills')) if os.path.isdir(os.path.join(r,'04_Tech_Lab','skills',d)) and not d.startswith(('.','_'))]) if os.path.isdir(os.path.join(r,'04_Tech_Lab','skills')) else 0;tp=len([d for d in os.listdir(os.path.join(r,'03_Knowledge_Mat','00_Atlas','templates')) if os.path.isdir(os.path.join(r,'03_Knowledge_Mat','00_Atlas','templates',d)) and not d.startswith(('.','_'))]) if os.path.isdir(os.path.join(r,'03_Knowledge_Mat','00_Atlas','templates')) else 0;open(os.path.join(r,'01_Command_Center','sync_status.json'),'w').write(json.dumps({'last_sync':datetime.datetime.now().isoformat(),'skills':sk,'templates':tp,'outbox_shield':'PAUSED'},indent=2))"

echo [M7] 6/7 Write mobile status snapshot (phone oversight)...
python "%S%\m7_mobile_snapshot.py" >> "%LOG%" 2>&1

echo [M7] 7/7 Git snapshot...
git add -A >nul 2>&1
git commit -m "M7 daily auto-sync %NOW%" >nul 2>&1

echo [M7] Daily sync complete %NOW%. Log: 04_Tech_Lab\logs\daily_sync_log.md
echo - done %NOW% >> "%LOG%"
