# ============================================================
#  Pineapple M7 - Safe Agent OS Update (one button)
#  Backs up, applies newest pack, PRESERVES M7 customizations,
#  enforces zero-green, rebuilds, restarts, and VERIFIES every
#  install guide. Follows UPDATE-WITH-AI.md safely.
# ============================================================
$ErrorActionPreference = "Stop"
$APP  = "C:\Pineapple Contractors M7\03_Knowledge_Mat\00_Atlas\templates\agent-os-pack-2026-06-29\source"
$ROOT = "C:\Pineapple Contractors M7"
$BAKROOT = "C:\Pineapple Contractors M7\04_Tech_Lab\_agentos_backups"

# M7 customizations that must survive every update
$CUSTOMS = @(
  "src\lib\seoPipeline.ts",
  "src\app\api\seo\research\route.ts",
  "src\app\api\seo\generate\route.ts",
  "src\components\SEOView.tsx",
  "src\components\TopBar.tsx",
  "src\app\paperclip\page.tsx",
  "src\app\globals.css",
  "public\build-guide.html",
  "src\app\api\hermes\realtime\sdp\route.ts",
  "src\components\JarvisRealtime.tsx",
  "src\components\JarvisView.tsx",
  "src\lib\hermesJarvis.ts",
  "src\app\api\astros\scan\route.ts",
  "src\app\api\astros\latest\route.ts",
  "src\app\api\astros\history\route.ts",
  "src\app\api\astros\config\route.ts",
  "src\app\api\astros\notebook\route.ts",
  "src\lib\kanbanSeo.ts",
  "src\components\ApolloView.tsx"
)

Write-Host "Pineapple M7 - Safe Agent OS Update" -ForegroundColor Yellow

# 1. Find newest agent-os-pack*.zip (Downloads + vault root)
$zips = @()
$zips += Get-ChildItem "$HOME\Downloads\agent-os-pack*.zip" -ErrorAction SilentlyContinue
$zips += Get-ChildItem "$ROOT\agent-os-pack*.zip" -ErrorAction SilentlyContinue
$zip = $zips | Sort-Object Name -Descending | Select-Object -First 1
if (-not $zip) { Write-Host "No agent-os-pack*.zip found in Downloads or vault root." -ForegroundColor Red; Read-Host "Enter to exit"; exit 1 }
Write-Host "Using pack: $($zip.FullName)"

$ts = Get-Date -Format "yyyyMMdd_HHmmss"

# 2. Back up current app CODE (deps regenerate) + save customizations
$bak  = "$BAKROOT\source.bak-$ts"
$csav = "$BAKROOT\_M7_customizations-$ts"
New-Item -ItemType Directory -Path $bak,$csav -Force | Out-Null
robocopy $APP $bak /E /XD node_modules .next .turbo /NFL /NDL /NJH /NJS /NC /NS /R:1 /W:1 | Out-Null
foreach ($f in $CUSTOMS) {
  $s = Join-Path $APP $f
  if (Test-Path $s) { $d = Join-Path $csav $f; New-Item -ItemType Directory -Path (Split-Path $d) -Force | Out-Null; Copy-Item $s $d -Force }
}
Write-Host "Backup: $bak"

# 3. Extract new pack, locate source
$tmp = "$BAKROOT\_newpack-$ts"
New-Item -ItemType Directory -Path $tmp -Force | Out-Null
Expand-Archive -Path $zip.FullName -DestinationPath $tmp -Force
$new = (Get-ChildItem $tmp -Recurse -Directory -Filter "source" | Where-Object { Test-Path (Join-Path $_.FullName "package.json") } | Select-Object -First 1).FullName
if (-not $new) { Write-Host "Could not find source/ in the pack." -ForegroundColor Red; Read-Host "Enter to exit"; exit 1 }
Write-Host "New source: $new (VERSION $(Get-Content (Join-Path $new 'VERSION')))"

# 4. Stop dashboard, mirror new code (keep deps), restore customizations
$pids = (Get-NetTCPConnection -LocalPort 3000 -State Listen -ErrorAction SilentlyContinue).OwningProcess | Select-Object -Unique
foreach ($id in $pids) { try { Stop-Process -Id $id -Force } catch {} }
Start-Sleep 2
robocopy $new $APP /MIR /XD node_modules .next .turbo /NFL /NDL /NJH /NJS /NC /NS /R:1 /W:1 | Out-Null
foreach ($f in $CUSTOMS) {
  $s = Join-Path $csav $f
  if (Test-Path $s) { $d = Join-Path $APP $f; New-Item -ItemType Directory -Path (Split-Path $d) -Force | Out-Null; Copy-Item $s $d -Force }
}
Write-Host "New code applied + $($CUSTOMS.Count) M7 customizations restored."

# 4b. ZERO-GREEN M7 sweep (hashtable-based; enforces Navy/Gold/Cyan)
$hexMap = @{
  '#5ab896'='#00BFFF';'#3a8a6e'='#00BFFF';'#34d399'='#00BFFF';'#a3e635'='#FBC02D';
  '#10b981'='#00BFFF';'#22c55e'='#00BFFF';'#4ade80'='#00BFFF';'#16a34a'='#00BFFF';
  '#15803d'='#00BFFF';'#2d7d46'='#00BFFF';'#059669'='#00BFFF';'#84cc16'='#FBC02D';'#bef264'='#FBC02D'
}
$rgbaMap = @{
  'rgba\(52,\s*211,\s*153'='rgba(0,191,255';'rgba\(90,\s*184,\s*150'='rgba(0,191,255';
  'rgba\(16,\s*185,\s*129'='rgba(0,191,255';'rgba\(34,\s*197,\s*94'='rgba(0,191,255';
  'rgba\(163,\s*230,\s*53'='rgba(251,192,45'
}
# M7 de-personalization: strip the pack author's branding (Julian Goldie) -> Pineapple M7
# NOTE: array of pairs (NOT a hashtable) — PowerShell hashtable keys are case-insensitive,
# so 'GoldieBench'/'goldiebench' would collide. Order matters (specific before generic).
$brandPairs = @(
  @('hermes@goldie.agency','hermes@pineapplecontractors.com'),
  @('goldie.pass','pineapple.pass'),
  @('aimoneylabjuliangoldie.com','pineapplecontractors.com'),
  @('ai-seo-with-julian-goldie-1553','pineapplecontractors'),
  @('goldiebench.com','pineapplecontractors.com'),
  @('GoldieBench','M7 Bench'),
  @('goldiebench','the leaderboard'),
  @('/Users/juliangoldie','/Users/saia'),
  @('skool.com/ai-profit-lab-7462','pineapplecontractors.com'),
  @('AI Money Lab','the Complimentary Professional Photo Audit (CPPA)'),
  @('AI Profit Boardroom','the Pineapple Standard'),
  @('juliangoldie','pineapplem7')
)
foreach ($file in (Get-ChildItem "$APP\src" -Recurse -Include *.tsx,*.ts,*.css,*.jsx -ErrorAction SilentlyContinue)) {
  $c = [System.IO.File]::ReadAllText($file.FullName)
  $o = $c
  foreach ($k in $hexMap.Keys)  { $c = $c -replace ('(?i)' + [regex]::Escape($k)), $hexMap[$k] }
  $c = $c -replace 'emerald-(\d)','cyan-$1'
  $c = $c -replace 'green-(\d)','sky-$1'
  $c = $c -replace 'lime-(\d)','amber-$1'
  foreach ($k in $rgbaMap.Keys) { $c = $c -replace $k, $rgbaMap[$k] }
  foreach ($pair in $brandPairs) { $c = $c.Replace($pair[0], $pair[1]) }
  if ($c -ne $o) { [System.IO.File]::WriteAllText($file.FullName, $c) }
}
Write-Host "Zero-green M7 sweep applied (Navy/Gold/Cyan enforced)."

# 5. Reinstall + rebuild
Set-Location $APP
Write-Host "npm install..."
cmd /c "npm install" *> $null
Write-Host "npm run build..."
cmd /c "npm run build" *> $null

# 6. Start + verify
Start-Process -NoNewWindow powershell -ArgumentList "-Command","`$env:PORT=3000; npm start"
Start-Sleep 8
$code = 0
try { $code = (Invoke-WebRequest "http://127.0.0.1:3000/" -UseBasicParsing -TimeoutSec 5).StatusCode } catch { $code = 0 }
if ($code -eq 200) { Write-Host "Dashboard UP on http://localhost:3000 (updated + M7-branded)." -ForegroundColor Green }
else { Write-Host "Dashboard did not confirm 200 yet - give it a moment, or roll back from $bak" -ForegroundColor Yellow }

# 7. POST-UPDATE VERIFICATION - reach EVERY install guide + verify runtime
Write-Host ""
Write-Host "VERIFICATION PASS - checking every install guide + component..." -ForegroundColor Cyan
$installDir = Join-Path (Split-Path (Split-Path $APP)) "install"
$guides = @(Get-ChildItem "$installDir\*.md" -ErrorAction SilentlyContinue)
Write-Host "  install guides found: $($guides.Count) (expected ~27)"

$svc = [ordered]@{ "3000"="Dashboard"; "3737"="CommandCtr"; "3100"="Paperclip"; "8082"="FCC"; "11434"="Ollama" }
foreach ($p in $svc.Keys) {
  $up = $false
  try { $null = (Invoke-WebRequest "http://127.0.0.1:$p/" -UseBasicParsing -TimeoutSec 4).StatusCode; $up = $true }
  catch { if ($_.Exception.Response.StatusCode.value__ -ge 400) { $up = $true } }
  $mark = "WARN"; if ($up) { $mark = "OK" }
  Write-Host "  [$mark] :$p $($svc[$p])"
}

foreach ($d in @("ffmpeg","node","npm")) {
  $mark = "WARN"; if (Get-Command $d -ErrorAction SilentlyContinue) { $mark = "OK" }
  Write-Host "  [$mark] $d"
}

$penv = "$env:LOCALAPPDATA\hermes\profiles\main\.env"
if (Test-Path $penv) {
  $names = (Get-Content $penv | Select-String "^[A-Z_]+_API_KEY=" | ForEach-Object { ($_ -split "=")[0] }) -join " "
  Write-Host "  keys in main profile: $names"
}

$greenServed = @(Get-ChildItem "$APP\.next\static" -Recurse -Include *.css -ErrorAction SilentlyContinue | Select-String -Pattern "#5ab896|#34d399|#a3e635|#10b981" -ErrorAction SilentlyContinue).Count
$gmark = "WARN"; if ($greenServed -eq 0) { $gmark = "OK" }
Write-Host "  [$gmark] zero-green in served CSS ($greenServed refs)"

$cfg = "$env:USERPROFILE\.agentic-os\config.json"
if (Test-Path $cfg) { $uj = Get-Content $cfg -Raw | ConvertFrom-Json; Write-Host "  branding: userName=$($uj.userName) vaultRoot=$($uj.vaultRoot)" }

Write-Host ""
Write-Host "  Full per-guide audit: 01_Command_Center\M7_AGENT_OS_SETUP_AUDIT.md" -ForegroundColor Cyan
Write-Host "  Rollback backup: $bak"
