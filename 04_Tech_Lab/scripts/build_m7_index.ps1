# INTENT: Rescan the 4-Room Fala and rewrite the M7_INDEX snapshot inside OS_Dashboard.html.
# Run:  powershell -ExecutionPolicy Bypass -File .\build_m7_index.ps1
# Effect: replaces the `const M7_INDEX = {...};` block with fresh real file counts.

$ErrorActionPreference = 'Stop'
$Root = 'C:\Pineapple Contractors M7'
$Dashboard = Join-Path $Root '01_Command_Center\OS_Dashboard.html'

$rooms = '01_Command_Center','02_Media_Vault','03_Knowledge_Mat','04_Tech_Lab'

function Count-Files($path) {
    if (-not (Test-Path $path)) { return 0 }
    @(Get-ChildItem -LiteralPath $path -Recurse -File -Force -ErrorAction SilentlyContinue).Count
}

$roomObjs = foreach ($r in $rooms) {
    $roomPath = Join-Path $Root $r
    $clusters = @()
    # one cluster per immediate subfolder
    foreach ($d in Get-ChildItem -LiteralPath $roomPath -Directory -Force -ErrorAction SilentlyContinue) {
        $c = Count-Files $d.FullName
        if ($c -gt 0) { $clusters += [pscustomobject]@{ name = $d.Name; files = $c } }
    }
    # loose files at the room root become a "(room root)" cluster
    $rootLoose = @(Get-ChildItem -LiteralPath $roomPath -File -Force -ErrorAction SilentlyContinue).Count
    if ($rootLoose -gt 0) { $clusters += [pscustomobject]@{ name = '(room root)'; files = $rootLoose } }
    $clusters = $clusters | Sort-Object files -Descending
    [pscustomobject]@{
        id       = $r
        label    = ($r -replace '_',' ')
        files    = Count-Files $roomPath
        clusters = $clusters
    }
}

# est. tokens of curated text (.md/.txt/.json) in rooms 01 + 03, bytes/4
$curatedBytes = 0
foreach ($r in '01_Command_Center','03_Knowledge_Mat') {
    Get-ChildItem -LiteralPath (Join-Path $Root $r) -Recurse -File -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -in '.md','.txt','.json' } |
        ForEach-Object { $curatedBytes += $_.Length }
}
$curatedTokens = [int]($curatedBytes / 4)

# --- build the JS block ---
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('    const M7_INDEX = {')
[void]$sb.AppendLine("        generated: `"$(Get-Date -Format 'yyyy-MM-dd')`",")
[void]$sb.AppendLine('        root: "C:\\Pineapple Contractors M7",')
[void]$sb.AppendLine("        curatedTokensEst: $curatedTokens,")
[void]$sb.AppendLine('        rooms: [')
for ($i = 0; $i -lt $roomObjs.Count; $i++) {
    $room = $roomObjs[$i]
    [void]$sb.AppendLine("            { id: `"$($room.id)`", label: `"$($room.label)`", files: $($room.files), clusters: [")
    for ($j = 0; $j -lt $room.clusters.Count; $j++) {
        $cl = $room.clusters[$j]
        $name = $cl.name -replace '"','\"'
        $comma = if ($j -lt $room.clusters.Count - 1) { ',' } else { '' }
        [void]$sb.AppendLine("                { name: `"$name`", files: $($cl.files) }$comma")
    }
    $rcomma = if ($i -lt $roomObjs.Count - 1) { ',' } else { '' }
    [void]$sb.AppendLine("            ]}$rcomma")
}
[void]$sb.AppendLine('        ]')
[void]$sb.Append('    };')
$block = $sb.ToString()

# Read/write as UTF-8 (no BOM) explicitly so multibyte chars survive the round-trip.
$utf8 = New-Object System.Text.UTF8Encoding $false
$html = [System.IO.File]::ReadAllText($Dashboard, $utf8)
$pattern = '(?s)    const M7_INDEX = \{.*?\r?\n    \};'
if ($html -notmatch $pattern) { throw 'M7_INDEX block not found in OS_Dashboard.html' }
$evaluator = [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $block }
$html = [regex]::Replace($html, $pattern, $evaluator)
[System.IO.File]::WriteAllText($Dashboard, $html, $utf8)

Write-Host "M7_INDEX refreshed: $($roomObjs.Count) rooms, $((($roomObjs | Measure-Object files -Sum).Sum)) files, ~${curatedTokens} curated tokens."
