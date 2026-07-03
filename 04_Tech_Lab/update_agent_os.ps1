# ============================================================
#  Pineapple M7 — Safe Agent OS Update (one button)
#  Backs up, applies the newest pack, PRESERVES M7 customizations,
#  rebuilds, and restarts. Follows UPDATE-WITH-AI.md safely.
# ============================================================
$ErrorActionPreference = "Stop"
$APP  = "C:\Pineapple Contractors M7\03_Knowledge_Mat\00_Atlas\templates\agent-os-pack-2026-06-29\source"
$ROOT = "C:\Pineapple Contractors M7"
$BAKROOT = "C:\tmp\m7_agentos_backup"

# The M7 customizations that must survive every update
$CUSTOMS = @(
  "src\lib\seoPipeline.ts",
  "src\app\api\seo\research\route.ts",
  "src\app\api\seo\generate\route.ts",
  "src\components\SEOView.tsx",
  "src\components\TopBar.tsx",
  "src\app\paperclip\page.tsx",
  "src\app\globals.css",
  "public\build-guide.html"
)

Write-Host "🍍 Pineapple M7 — Safe Agent OS Update" -ForegroundColor Yellow

# 1. Find newest agent-os-pack*.zip (Downloads + vault root)
$zips = @()
$zips += Get-ChildItem "$HOME\Downloads\agent-os-pack*.zip" -ErrorAction SilentlyContinue
$zips += Get-ChildItem "$ROOT\agent-os-pack*.zip" -ErrorAction SilentlyContinue
$zip = $zips | Sort-Object Name -Descending | Select-Object -First 1
if (-not $zip) { Write-Host "❌ No agent-os-pack*.zip found in Downloads or vault root." -ForegroundColor Red; exit 1 }
Write-Host "📦 Using pack: $($zip.FullName)"

$ts = Get-Date -Format "yyyyMMdd_HHmmss"

# 2. Back up current app CODE (deps regenerate) + save customizations
$bak  = "$BAKROOT\source.bak-$ts"
$csav = "$BAKROOT\_M7_customizations-$ts"
New-Item -ItemType Directory -Path $bak,$csav -Force | Out-Null
robocopy $APP $bak /E /XD node_modules .next .turbo /NFL /NDL /NJH /NJS /NC /NS /R:1 /W:1 | Out-Null
foreach ($f in $CUSTOMS) { $s = Join-Path $APP $f; if (Test-Path $s) { $d = Join-Path $csav $f; New-Item -ItemType Directory -Path (Split-Path $d) -Force | Out-Null; Copy-Item $s $d -Force } }
Write-Host "🛡️  Backup: $bak"

# 3. Extract new pack, locate source
$tmp = "$BAKROOT\_newpack-$ts"
New-Item -ItemType Directory -Path $tmp -Force | Out-Null
Expand-Archive -Path $zip.FullName -DestinationPath $tmp -Force
$new = (Get-ChildItem $tmp -Recurse -Directory -Filter "source" | Where-Object { Test-Path (Join-Path $_.FullName "package.json") } | Select-Object -First 1).FullName
if (-not $new) { Write-Host "❌ Couldn't find source/ in the pack." -ForegroundColor Red; exit 1 }
Write-Host "📂 New source: $new  (VERSION $(Get-Content (Join-Path $new 'VERSION')))"

# 4. Stop dashboard, mirror new code (keep deps), restore customizations
$p = (Get-NetTCPConnection -LocalPort 3000 -State Listen -ErrorAction SilentlyContinue).OwningProcess | Select-Object -Unique
foreach ($id in $p) { try { Stop-Process -Id $id -Force } catch {} }
Start-Sleep 2
robocopy $new $APP /MIR /XD node_modules .next .turbo /NFL /NDL /NJH /NJS /NC /NS /R:1 /W:1 | Out-Null
foreach ($f in $CUSTOMS) { $s = Join-Path $csav $f; if (Test-Path $s) { $d = Join-Path $APP $f; New-Item -ItemType Directory -Path (Split-Path $d) -Force | Out-Null; Copy-Item $s $d -Force } }
Write-Host "✅ New code applied + $($CUSTOMS.Count) M7 customizations restored."

# 4b. ZERO-GREEN M7 sweep — kill any green the new pack reintroduced (hex, tailwind classes, rgba)
$greenHex = @('5ab896','3a8a6e','34d399','a3e635','10b981','22c55e','4ade80','16a34a','15803d','2d7d46','059669','84cc16','bef264')
foreach ($file in (Get-ChildItem "$APP\src" -Recurse -Include *.tsx,*.ts,*.css,*.jsx -ErrorAction SilentlyContinue)) {
  $c = Get-Content $file.FullName -Raw; $o = $c
  foreach ($h in $greenHex) { $c = $c -replace "(?i)#$h", "#00BFFF" }
  $c = $c -replace 'emerald-(\d)','cyan-$1' -replace '\bgreen-(\d)','sky-$1' -replace '\blime-(\d)','amber-$1'
  $c = $c -replace 'rgba\(52,\s*211,\s*153','rgba(0,191,255' -replace 'rgba\(90,\s*184,\s*150','rgba(0,191,255' -replace 'rgba\(16,\s*185,\s*129','rgba(0,191,255' -replace 'rgba\(34,\s*197,\s*94','rgba(0,191,255' -replace 'rgba\(163,\s*230,\s*53','rgba(251,192,45'
  if ($c -ne $o) { Set-Content $file.FullName $c -NoNewline }
}
Write-Host "🎨 Zero-green M7 sweep applied (Navy/Gold/Cyan enforced)."

# 5. Reinstall + rebuild
Set-Location $APP
Write-Host "📦 npm install..."; npm install 2>&1 | Out-Null
Write-Host "🔨 npm run build..."; npm run build 2>&1 | Out-Null

# 6. Start + verify
Start-Process -NoNewWindow powershell -ArgumentList "-Command","`$env:PORT=3000; npm start"
Start-Sleep 8
$code = try { (Invoke-WebRequest "http://127.0.0.1:3000/" -UseBasicParsing -TimeoutSec 5).StatusCode } catch { 0 }
if ($code -eq 200) { Write-Host "🟢 Dashboard UP on http://localhost:3000 (updated + M7-branded)." -ForegroundColor Green }
else { Write-Host "⚠️ Dashboard didn't confirm 200 yet — give it a moment, or roll back from $bak" -ForegroundColor Yellow }
Write-Host "↩️  Rollback backup: $bak"
