[CmdletBinding()]
param(
  [string]$VaultRoot = "C:\Pineapple Contractors M7",
  [switch]$RestartObsidian
)

$ErrorActionPreference = "Stop"
$Results = @()
$Stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"

function Add-Result([string]$Area, [string]$Status, [string]$Detail) {
  $script:Results += [pscustomobject]@{ Area = $Area; Status = $Status; Detail = $Detail }
  $color = switch ($Status) { "PASS" { "Green" } "FAIL" { "Red" } default { "Yellow" } }
  Write-Host ("[{0}] {1} - {2}" -f $Status, $Area, $Detail) -ForegroundColor $color
}

function Test-LocalPort([int]$Port) {
  $client = New-Object System.Net.Sockets.TcpClient
  try {
    $pending = $client.BeginConnect("127.0.0.1", $Port, $null, $null)
    if (-not $pending.AsyncWaitHandle.WaitOne(1000, $false)) { return $false }
    $client.EndConnect($pending)
    return $true
  } catch {
    return $false
  } finally {
    $client.Close()
  }
}

function Write-Receipt([string]$Outbox) {
  New-Item -ItemType Directory -Force -Path $Outbox | Out-Null
  $receipt = Join-Path $Outbox ("PM7_OBSIDIAN_MEMORY_RECOVERY_{0}.md" -f $Stamp)
  $lines = @(
    "---",
    "title: PM7 Obsidian Memory Recovery $Stamp",
    "status: PAUSED",
    "generated_by: PM7_OBSIDIAN_MEMORY_RECOVERY.ps1",
    "---",
    "",
    "# PM7 Obsidian memory recovery receipt",
    "",
    "- Computer: $env:COMPUTERNAME",
    "- Project root: ``$VaultRoot``",
    "- Focused AI memory: ``$(Join-Path $VaultRoot '03_Knowledge_Mat')``",
    "- Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
    "- Secrets recorded: no",
    "",
    "| Check | Result | Evidence |",
    "|---|---|---|"
  )
  foreach ($row in $Results) {
    $detail = ([string]$row.Detail).Replace("|", "\|").Replace("`r", " ").Replace("`n", " ")
    $lines += "| $($row.Area) | $($row.Status) | $detail |"
  }
  $lines += @(
    "",
    "> This receipt deliberately contains no Local REST API key or configuration values. Key rotation remains an owner-only action in Obsidian settings. Outbound publishing and spend remain PAUSED."
  )
  Set-Content -Path $receipt -Value $lines -Encoding UTF8
  Write-Host ("Receipt: {0}" -f $receipt) -ForegroundColor Cyan
}

Write-Host ""
Write-Host "PINEAPPLE M7 - OBSIDIAN MEMORY RECOVERY" -ForegroundColor Cyan

if (-not (Test-Path -LiteralPath $VaultRoot -PathType Container)) {
  Write-Error "Vault root does not exist: $VaultRoot"
  exit 1
}

$VaultRoot = (Resolve-Path -LiteralPath $VaultRoot).Path
$ObsidianRoot = Join-Path $VaultRoot ".obsidian"
$MemoryRoot = Join-Path $VaultRoot "03_Knowledge_Mat"
$Outbox = Join-Path $VaultRoot "01_Command_Center\Outbox_Drafts"

if (-not (Test-Path -LiteralPath $ObsidianRoot -PathType Container)) {
  Add-Result "Obsidian configuration" "FAIL" "The project-root .obsidian folder is missing; no workspace file was changed."
  Write-Receipt $Outbox
  exit 1
}
Add-Result "Obsidian configuration" "PASS" "Project-root .obsidian folder exists."

$processes = @(Get-Process -Name "Obsidian" -ErrorAction SilentlyContinue)
if ($processes.Count -eq 0) {
  Add-Result "Stop Obsidian" "PASS" "Obsidian was not running."
} else {
  foreach ($process in $processes) {
    try { [void]$process.CloseMainWindow() } catch {}
  }
  Start-Sleep -Seconds 4
  $remaining = @(Get-Process -Name "Obsidian" -ErrorAction SilentlyContinue)
  if ($remaining.Count -gt 0) {
    $remaining | Stop-Process -Force -ErrorAction Stop
    Start-Sleep -Seconds 2
  }
  if (Get-Process -Name "Obsidian" -ErrorAction SilentlyContinue) {
    Add-Result "Stop Obsidian" "FAIL" "One or more Obsidian processes could not be terminated."
  } else {
    Add-Result "Stop Obsidian" "PASS" "All Obsidian processes were terminated before the workspace reset."
  }
}

$workspace = Join-Path $ObsidianRoot "workspace.json"
$workspaceBackup = Join-Path $ObsidianRoot "workspace.json.bak"
try {
  if (Test-Path -LiteralPath $workspace) {
    if (Test-Path -LiteralPath $workspaceBackup) {
      $previous = Join-Path $ObsidianRoot ("workspace.json.bak.previous-{0}" -f $Stamp)
      Move-Item -LiteralPath $workspaceBackup -Destination $previous
    }
    Move-Item -LiteralPath $workspace -Destination $workspaceBackup
    Add-Result "Workspace reset" "PASS" "workspace.json was renamed to workspace.json.bak; no notes were moved or deleted."
  } elseif (Test-Path -LiteralPath $workspaceBackup) {
    Add-Result "Workspace reset" "PASS" "workspace.json was already absent and workspace.json.bak exists."
  } else {
    Add-Result "Workspace reset" "NOT NEEDED" "No workspace.json was present. Obsidian will create a clean workspace when opened."
  }
} catch {
  Add-Result "Workspace reset" "FAIL" $_.Exception.Message
}

$pluginFolder = Join-Path $ObsidianRoot "plugins\obsidian-local-rest-api"
$pluginManifest = Join-Path $pluginFolder "manifest.json"
$pluginData = Join-Path $pluginFolder "data.json"
$localRestExpected = $false
if (Test-Path -LiteralPath $pluginFolder -PathType Container) {
  $detail = "Plugin folder exists."
  $pluginFilesComplete = $true
  if (Test-Path -LiteralPath $pluginManifest) {
    try {
      $manifest = Get-Content -LiteralPath $pluginManifest -Raw | ConvertFrom-Json
      $detail += " Manifest id=$($manifest.id), version=$($manifest.version)."
    } catch {
      $detail += " Manifest exists but could not be parsed."
      $pluginFilesComplete = $false
    }
  } else {
    $detail += " Manifest is missing."
    $pluginFilesComplete = $false
  }
  if (Test-Path -LiteralPath $pluginData) {
    $detail += " Configuration file exists; its values were intentionally not read."
  } else {
    $detail += " Configuration file is missing."
    $pluginFilesComplete = $false
  }
  Add-Result "Local REST API plugin" ($(if ($pluginFilesComplete) { "PASS" } else { "FAIL" })) $detail
} else {
  Add-Result "Local REST API plugin" "FAIL" "Expected folder .obsidian\plugins\obsidian-local-rest-api is missing. Install and enable the official plugin before configuring clients."
}

$communityPlugins = Join-Path $ObsidianRoot "community-plugins.json"
if (Test-Path -LiteralPath $communityPlugins) {
  try {
    $enabled = @(Get-Content -LiteralPath $communityPlugins -Raw | ConvertFrom-Json)
    if ($enabled -contains "obsidian-local-rest-api") {
      $localRestExpected = $true
      Add-Result "Local REST enabled" "PASS" "The plugin id is present in community-plugins.json."
    } else {
      Add-Result "Local REST enabled" "FAIL" "The plugin folder exists but the plugin id is not enabled in community-plugins.json."
    }
  } catch {
    Add-Result "Local REST enabled" "NOT TESTED" "community-plugins.json could not be parsed."
  }
} else {
  Add-Result "Local REST enabled" "NOT TESTED" "community-plugins.json is missing."
}

if (Test-Path -LiteralPath $MemoryRoot -PathType Container) {
  Add-Result "Focused memory root" "PASS" "03_Knowledge_Mat exists and will remain the shared AI memory scope."
  $agentConfigDir = Join-Path $env:USERPROFILE ".agentic-os"
  $agentConfig = Join-Path $agentConfigDir "config.json"
  try {
    New-Item -ItemType Directory -Force -Path $agentConfigDir | Out-Null
    if (Test-Path -LiteralPath $agentConfig) {
      $config = Get-Content -LiteralPath $agentConfig -Raw | ConvertFrom-Json
      Copy-Item -LiteralPath $agentConfig -Destination ("{0}.bak.{1}" -f $agentConfig, $Stamp)
    } else {
      $config = [pscustomobject]@{}
    }
    if ($config.PSObject.Properties.Name -contains "vaultRoot") {
      $config.vaultRoot = $MemoryRoot
    } else {
      $config | Add-Member -NotePropertyName "vaultRoot" -NotePropertyValue $MemoryRoot
    }
    $temporary = "{0}.tmp.{1}" -f $agentConfig, $Stamp
    $config | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $temporary -Encoding UTF8
    Move-Item -LiteralPath $temporary -Destination $agentConfig -Force
    Add-Result "Local Studio memory scope" "PASS" "Agentic OS vaultRoot now targets 03_Knowledge_Mat; other configuration properties were preserved."
  } catch {
    Add-Result "Local Studio memory scope" "FAIL" ("Agentic OS config was not changed: {0}" -f $_.Exception.Message)
  }
} else {
  Add-Result "Focused memory root" "FAIL" "03_Knowledge_Mat is missing; Local Studio config was not changed."
}

if ($RestartObsidian) {
  $candidates = @(
    (Join-Path $env:LOCALAPPDATA "Obsidian\Obsidian.exe"),
    (Join-Path $env:LOCALAPPDATA "Programs\Obsidian\Obsidian.exe")
  )
  $obsidianCommand = Get-Command "Obsidian.exe" -ErrorAction SilentlyContinue
  if ($obsidianCommand) { $candidates += $obsidianCommand.Source }
  $executable = $candidates | Where-Object { $_ -and (Test-Path -LiteralPath $_ -PathType Leaf) } | Select-Object -First 1
  if ($executable) {
    try {
      Start-Process -FilePath $executable -ArgumentList ('"{0}"' -f $VaultRoot) | Out-Null
      Start-Sleep -Seconds 8
      if (Get-Process -Name "Obsidian" -ErrorAction SilentlyContinue) {
        Add-Result "Restart Obsidian" "PASS" "Obsidian restarted with a clean workspace state."
      } else {
        Add-Result "Restart Obsidian" "FAIL" "The executable launched but no Obsidian process was detected."
      }
    } catch {
      Add-Result "Restart Obsidian" "FAIL" $_.Exception.Message
    }
  } else {
    Add-Result "Restart Obsidian" "FAIL" "Obsidian.exe was not found in the standard Windows install locations or PATH."
  }
} else {
  Add-Result "Restart Obsidian" "NOT TESTED" "Restart was not requested."
}

$portReady = $false
for ($attempt = 1; $attempt -le 15; $attempt++) {
  if (Test-LocalPort 27124) {
    $portReady = $true
    break
  }
  Start-Sleep -Seconds 2
}

if ($portReady) {
  $curl = Get-Command "curl.exe" -ErrorAction SilentlyContinue
  if ($curl) {
    $httpCode = (& $curl.Source -k -s -o NUL -w "%{http_code}" --max-time 5 "https://127.0.0.1:27124/" 2>$null)
    if ($httpCode -eq "200") {
      Add-Result "Local REST HTTPS" "PASS" "Loopback HTTPS root returned HTTP 200 on port 27124."
    } else {
      Add-Result "Local REST HTTPS" "NOT TESTED" ("Port 27124 is listening; unauthenticated health probe returned HTTP {0}." -f $httpCode)
    }
  } else {
    Add-Result "Local REST HTTPS" "PASS" "Loopback port 27124 is listening; curl.exe was unavailable for the HTTP probe."
  }
} else {
  $status = if ($localRestExpected) { "FAIL" } else { "NOT TESTED" }
  Add-Result "Local REST HTTPS" $status "Port 27124 is not listening. Enable the official Local REST API plugin, then rerun this recovery."
}

Add-Result "Credential rotation" "OWNER ACTION" "In Obsidian, use Local REST API settings > Reset all cryptography. Never paste the replacement value into Git, Markdown, a launcher, or a receipt."
Write-Receipt $Outbox

$failures = @($Results | Where-Object { $_.Status -eq "FAIL" }).Count
if ($failures -gt 0) { exit 1 }
exit 0
