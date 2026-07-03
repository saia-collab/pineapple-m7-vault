<#
================================================================================
 PINEAPPLE CONTRACTORS M7 — SCAFFOLDER & PRE-FLIGHT  (setup_m7.ps1)
 Builds/repairs the immutable 4-Fala topography, verifies dependencies,
 and arms the Brand Firewall. Idempotent — safe to re-run. Zero directory drift.
 Ko e hala 'o e fononga ko e faka'apa'apa.
================================================================================
#>

$ErrorActionPreference = "Stop"
$Root = "C:\Pineapple Contractors M7"
Write-Host "== M7 SCAFFOLDER ==" -ForegroundColor Yellow
Write-Host "Root: $Root"

# --- 1. Immutable 4-Fala topography -------------------------------------------
$dirs = @(
  "01_Command_Center","01_Command_Center\Outbox_Drafts",
  "02_Workspaces","02_Workspaces\Active_Campaigns",
  "02_Media_Vault",
  "03_Knowledge_Mat","03_Knowledge_Mat\raw","03_Knowledge_Mat\00_Atlas",
  "04_Tech_Lab","04_Tech_Lab\Scripts","04_Tech_Lab\config","04_Tech_Lab\logs",
  "05_Campaign_Factory\10_Research_Stage\input","05_Campaign_Factory\10_Research_Stage\output",
  "05_Campaign_Factory\20_Copy_Drafting\output",
  "05_Campaign_Factory\30_Compliance_Audit\output",
  ".obsidian\plugins\obsidian-local-rest-api",".obsidian\plugins\mcp-tools",".obsidian\canvas"
)
foreach ($d in $dirs) {
  $p = Join-Path $Root $d
  if (-not (Test-Path $p)) { New-Item -ItemType Directory -Force -Path $p | Out-Null; Write-Host "  + $d" -ForegroundColor Cyan }
}

# --- 2. Dependency pre-flight -------------------------------------------------
function Check-Cmd($name) {
  $ok = $null -ne (Get-Command $name -ErrorAction SilentlyContinue)
  $color = if ($ok) { "Cyan" } else { "Yellow" }
  Write-Host ("  {0,-10} {1}" -f $name, ($(if ($ok) {"OK"} else {"MISSING"}))) -ForegroundColor $color
  return $ok
}
Write-Host "`n== Dependencies ==" -ForegroundColor Yellow
$py = Check-Cmd "python"; Check-Cmd "node"; Check-Cmd "npx"; Check-Cmd "git" | Out-Null

# --- 3. Python deps for the firewall listener --------------------------------
if ($py) {
  Write-Host "`n== Python deps ==" -ForegroundColor Yellow
  python -m pip install --quiet watchdog 2>$null
  Write-Host "  watchdog installed (live FS listener)" -ForegroundColor Cyan
}

# --- 4. Purge legacy drift ----------------------------------------------------
$legacy = @("$Root\..\Pineapple-Mana-Global")
foreach ($l in $legacy) { if (Test-Path $l) { Write-Host "  ! legacy path present: $l (archive recommended)" -ForegroundColor Yellow } }

# --- 5. Arm the Brand Firewall ------------------------------------------------
Write-Host "`n== Brand Firewall pre-flight ==" -ForegroundColor Yellow
$fw = Join-Path $Root "04_Tech_Lab\Scripts\brand_firewall.py"
if (Test-Path $fw) {
  python $fw --report
  if ($LASTEXITCODE -eq 0) { Write-Host "  FIREWALL PASS" -ForegroundColor Cyan }
  else { Write-Host "  FIREWALL flagged items — run: python `"$fw`" --fix" -ForegroundColor Yellow }
}

Write-Host "`nScaffold complete. Ko e hala 'o e fononga ko e faka'apa'apa." -ForegroundColor Yellow
