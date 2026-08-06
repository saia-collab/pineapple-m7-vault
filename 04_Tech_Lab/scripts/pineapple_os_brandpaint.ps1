# Pineapple M7 — Agent OS brand paint. Re-applies M7 brand law to any build source dir.
# Navy #1A365D / Pineapple Gold #FBC02D / Status Cyan #00BFFF. ZERO GREEN. De-Julian.
# Usage: powershell -File pineapple_os_brandpaint.ps1 -SrcRoot "<path>\src"
param([Parameter(Mandatory=$true)][string]$SrcRoot)

if (-not (Test-Path $SrcRoot)) { Write-Host "brandpaint: src not found: $SrcRoot"; exit 0 }

# 1) Theme palette in globals.css (aubergine -> navy, tan-gold -> Pineapple gold, green -> cyan)
$css = Join-Path $SrcRoot "app\globals.css"
if (Test-Path $css) {
  $t = [System.IO.File]::ReadAllText($css)
  $t = $t -replace '#15101a','#0d1826' -replace '#1c1622','#12233a' -replace '#251d2c','#172c47' -replace '#2e2436','#1e3a5c'
  $t = $t -replace '#d4a574','#FBC02D' -replace '#e6c69a','#FFD34D' -replace '#a87f54','#C99A1F'
  $t = $t -replace '#5ab896','#00BFFF' -replace '#3a8a6e','#0090c0'
  $t = $t -replace '212,\s*165,\s*116','251, 192, 45' -replace '230,\s*198,\s*154','255, 211, 77'
  [System.IO.File]::WriteAllText($css, $t)
}

# 2) Full hex sweep across .ts/.tsx AND .css: green->cyan, aubergine->navy, tan->gold.
#    Catches Tailwind arbitrary classes (text-[#15101a]) and hardcoded tints (#5ab8960f).
$greens = @('#5ab896','#3a8a6e','#22c55e','#16a34a','#15803d','#4ade80','#10b981','#059669','#34d399','#2D7D46','#2d7d46','#4CAF50','#4caf50','#06201b')
foreach ($f in Get-ChildItem $SrcRoot -Recurse -Include *.ts,*.tsx,*.css -File) {
  $t = [System.IO.File]::ReadAllText($f.FullName); $orig = $t
  foreach ($g in $greens) { $t = $t -replace [regex]::Escape($g), '#00BFFF' }
  # aubergine backgrounds -> navy
  $t = $t -replace '#15101a','#0d1826' -replace '#1c1622','#12233a' -replace '#251d2c','#172c47' -replace '#2e2436','#1e3a5c'
  # tan-gold -> Pineapple gold
  $t = $t -replace '#d4a574','#FBC02D' -replace '#e6c69a','#FFD34D' -replace '#a87f54','#C99A1F'
  if ($t -ne $orig) { [System.IO.File]::WriteAllText($f.FullName, $t) }
}

# 3) De-Julian: Agent Kanban must publish to the Pineapple site, not his
$ak = Join-Path $SrcRoot "components\AgentKanban.tsx"
if (Test-Path $ak) {
  $t = [System.IO.File]::ReadAllText($ak)
  $t = $t -replace 'id:\s*"aimoneylab",\s*name:\s*"aimoneylabjuliangoldie\.com",\s*url:\s*"https://aimoneylabjuliangoldie\.com"', 'id: "pineapple", name: "pineappleroofingllc.com", url: "https://pineappleroofingllc.com"'
  $t = $t -replace 'aimoneylabjuliangoldie\.com','pineappleroofingllc.com'
  [System.IO.File]::WriteAllText($ak, $t)
}
Write-Host "brandpaint: applied Pineapple palette + de-Julianed $SrcRoot"
