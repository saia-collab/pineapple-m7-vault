# Pineapple M7 — Agent OS brand paint. Re-applies M7 brand law to any build source dir.
# Pineapple Blue #003299 / Pineapple Yellow #ffdd17. ZERO GREEN. De-Julian. (Naa Sione brand, 2026-08-14)
# Usage: powershell -File pineapple_os_brandpaint.ps1 -SrcRoot "<path>\src"
param([Parameter(Mandatory=$true)][string]$SrcRoot)

if (-not (Test-Path $SrcRoot)) { Write-Host "brandpaint: src not found: $SrcRoot"; exit 0 }

# 1) Theme palette in globals.css (aubergine -> deep navy bg, tan-gold -> Pineapple yellow, green/cyan -> Pineapple blue)
$css = Join-Path $SrcRoot "app\globals.css"
if (Test-Path $css) {
  $t = [System.IO.File]::ReadAllText($css)
  $t = $t -replace '#15101a','#0d1826' -replace '#1c1622','#12233a' -replace '#251d2c','#172c47' -replace '#2e2436','#1e3a5c'
  $t = $t -replace '#d4a574','#ffdd17' -replace '#e6c69a','#ffe86b' -replace '#a87f54','#d4b400'
  $t = $t -replace '#5ab896','#003299' -replace '#3a8a6e','#00246e'
  $t = $t -replace '212,\s*165,\s*116','255, 221, 23' -replace '230,\s*198,\s*154','255, 232, 107'
  # retired Pineapple palette -> Naa Sione brand (old->new so a repaint can't regress)
  $t = $t -replace '#1A365D','#003299' -replace '#1a365d','#003299' -replace '#FBC02D','#ffdd17' -replace '#fbc02d','#ffdd17' -replace '#00BFFF','#003299' -replace '#00bfff','#003299'
  [System.IO.File]::WriteAllText($css, $t)
}

# 2) Full hex sweep across .ts/.tsx AND .css: green->cyan, aubergine->navy, tan->gold.
#    Catches Tailwind arbitrary classes (text-[#15101a]) and hardcoded tints (#5ab8960f).
$greens = @('#5ab896','#3a8a6e','#22c55e','#16a34a','#15803d','#4ade80','#10b981','#059669','#34d399','#2D7D46','#2d7d46','#4CAF50','#4caf50','#06201b')
foreach ($f in Get-ChildItem $SrcRoot -Recurse -Include *.ts,*.tsx,*.css -File) {
  $t = [System.IO.File]::ReadAllText($f.FullName); $orig = $t
  foreach ($g in $greens) { $t = $t -replace [regex]::Escape($g), '#003299' }
  # aubergine backgrounds -> deep navy bg (dark chrome, brand-compliant)
  $t = $t -replace '#15101a','#0d1826' -replace '#1c1622','#12233a' -replace '#251d2c','#172c47' -replace '#2e2436','#1e3a5c'
  # tan-gold -> Pineapple yellow
  $t = $t -replace '#d4a574','#ffdd17' -replace '#e6c69a','#ffe86b' -replace '#a87f54','#d4b400'
  # retired Pineapple palette -> Naa Sione brand (old->new so a repaint can't regress)
  $t = $t -replace '#1A365D','#003299' -replace '#1a365d','#003299' -replace '#FBC02D','#ffdd17' -replace '#fbc02d','#ffdd17' -replace '#00BFFF','#003299' -replace '#00bfff','#003299'
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
# 4) De-Julian sweep across the whole source — identity strings only.
#    NOT GoldieBench / goldiebench.com: that's a model benchmark label, not identity — leave it.
#    Literal .Replace (not regex) so dots/quotes need no escaping; ordered so full domains
#    resolve before the bare "aimoneylab" id.
$julianMap = [ordered]@{
  'aimoneylabjuliangoldie.com'   = 'pineappleroofingllc.com'
  'aisuccesslabjuliangoldie.com' = 'pineappleroofingllc.com'
  'juliangoldieaiautomation.com' = 'pineappleroofingllc.com'
  'aiprofitboardroom.com'        = 'pineappleroofingllc.com'
  'goldie.agency'                = 'pineappleroofingllc.com'
  '/Users/juliangoldie'          = '/Users/estim'
  'Julian Goldie'                = 'Pineapple Roofing'
  '"aimoneylab"'                 = '"pineapple"'
  '"julian"'                     = '"main"'
}
foreach ($f in Get-ChildItem $SrcRoot -Recurse -Include *.ts,*.tsx,*.css,*.md -File) {
  $t = [System.IO.File]::ReadAllText($f.FullName); $orig = $t
  foreach ($k in $julianMap.Keys) { $t = $t.Replace($k, [string]$julianMap[$k]) }
  if ($t -ne $orig) { [System.IO.File]::WriteAllText($f.FullName, $t) }
}
Write-Host "brandpaint: applied Pineapple palette + de-Julianed $SrcRoot"
