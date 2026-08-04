@echo off
REM ============================================================================
REM  Register M7 Mobile Snapshot to run every 30 minutes.
REM  Writes 01_Command_Center\MOBILE_STATUS.md (+ .json) so phone oversight
REM  stays live via the Drive-synced vault. Double-click ONCE.
REM  Ko e hala 'o e fononga ko e faka'apa'apa.
REM ============================================================================
set ROOT=C:\Pineapple Contractors M7
schtasks /Create /TN "M7 Mobile Snapshot" /TR "python \"%ROOT%\04_Tech_Lab\Scripts\m7_mobile_snapshot.py\"" /SC MINUTE /MO 30 /F
echo.
echo [M7] Registered "M7 Mobile Snapshot" to run every 30 minutes.
echo [M7] Run now to test:   schtasks /Run /TN "M7 Mobile Snapshot"
echo [M7] Remove later:      schtasks /Delete /TN "M7 Mobile Snapshot" /F
pause
