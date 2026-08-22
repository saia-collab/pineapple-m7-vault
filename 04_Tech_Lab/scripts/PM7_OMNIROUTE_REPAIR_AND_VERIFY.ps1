[CmdletBinding()]
param(
  [switch]$StartServices,
  [switch]$RunModelTests
)

$ErrorActionPreference = "Stop"
$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$M7Root = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
$Outbox = Join-Path $M7Root "01_Command_Center\Outbox_Drafts"
$Results = @()

function Add-Result([string]$Area, [string]$Status, [string]$Detail) {
  $script:Results += [pscustomobject]@{ Area = $Area; Status = $Status; Detail = $Detail }
  $color = switch ($Status) { "PASS" { "Green" } "FAIL" { "Red" } default { "Yellow" } }
  Write-Host ("[{0}] {1} - {2}" -f $Status, $Area, $Detail) -ForegroundColor $color
}

function Test-Port([int]$Port) {
  $client = New-Object System.Net.Sockets.TcpClient
  try {
    $async = $client.BeginConnect("127.0.0.1", $Port, $null, $null)
    if (-not $async.AsyncWaitHandle.WaitOne(1000, $false)) { return $false }
    $client.EndConnect($async)
    return $true
  } catch { return $false } finally { $client.Close() }
}

function Invoke-Probe([string]$Url, [hashtable]$Headers = @{}, [int]$Timeout = 5) {
  try {
    $response = Invoke-WebRequest -UseBasicParsing -Uri $Url -Headers $Headers -TimeoutSec $Timeout
    return [pscustomobject]@{ Status = [int]$response.StatusCode; Body = [string]$response.Content; Error = "" }
  } catch {
    $status = $null
    if ($_.Exception.Response) {
      try { $status = [int]$_.Exception.Response.StatusCode } catch {}
    }
    return [pscustomobject]@{ Status = $status; Body = ""; Error = $_.Exception.Message }
  }
}

function Start-PM7Stack {
  $launchers = @(
    (Join-Path $M7Root "04_Tech_Lab\Pineapple_Agent_OS\START-PINEAPPLE-AGENT-OS.ps1"),
    (Join-Path $M7Root "04_Tech_Lab\scripts\agentos_launcher_fixes_2026-08-16\START-PINEAPPLE-AGENT-OS.ps1")
  )
  $launcher = $launchers | Where-Object { Test-Path $_ } | Select-Object -First 1
  if (-not $launcher) {
    Add-Result "Service startup" "FAIL" "Local Studio launcher is missing."
    return
  }
  Write-Host "Starting the PM7 stack with the current launcher..." -ForegroundColor Cyan
  $process = Start-Process -FilePath "powershell.exe" -ArgumentList @(
    "-NoLogo", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ('"{0}"' -f $launcher), "-NoPause"
  ) -Wait -PassThru
  if ($process.ExitCode -eq 0) {
    Add-Result "Service startup" "PASS" "Launcher completed."
  } else {
    Add-Result "Service startup" "FAIL" ("Launcher exited {0}." -f $process.ExitCode)
  }
}

function Test-Service([string]$Name, [int]$Port, [string]$Url, [bool]$Required) {
  if (-not (Test-Port $Port)) {
    Add-Result $Name ($(if ($Required) { "FAIL" } else { "OPTIONAL" })) ("Port {0} is not listening." -f $Port)
    return
  }
  $probe = Invoke-Probe $Url
  if ($probe.Status -and $probe.Status -ge 200 -and $probe.Status -lt 500) {
    $detail = "HTTP {0} on port {1}" -f $probe.Status, $Port
    if ($probe.Status -in 401,403) { $detail += " (running; authentication required)" }
    Add-Result $Name "PASS" $detail
  } else {
    Add-Result $Name ($(if ($Required) { "FAIL" } else { "OPTIONAL" })) ("Port open; HTTP probe failed: {0}" -f $probe.Error)
  }
}

function Test-OmniRouteModel([string]$Model, [hashtable]$Headers) {
  $payload = @{
    model = $Model
    messages = @(@{ role = "user"; content = "Reply exactly PM7_ROUTE_OK" })
    max_tokens = 12
    temperature = 0
  } | ConvertTo-Json -Depth 6
  try {
    $response = Invoke-RestMethod -Uri "http://127.0.0.1:20128/v1/chat/completions" -Method Post -Headers $Headers -ContentType "application/json" -Body $payload -TimeoutSec 35
    $content = [string]$response.choices[0].message.content
    if ($content -match "PM7_ROUTE_OK") {
      Add-Result ("Model {0}" -f $Model) "PASS" "Live generation returned the expected marker."
    } else {
      Add-Result ("Model {0}" -f $Model) "FAIL" "A response arrived but did not contain the expected marker."
    }
  } catch {
    $status = $null
    if ($_.Exception.Response) { try { $status = [int]$_.Exception.Response.StatusCode } catch {} }
    if ($status -in 401,403) {
      Add-Result ("Model {0}" -f $Model) "NOT TESTED" "Gateway requires a token. Configure an OmniRoute endpoint or set OMNIROUTE_API_KEY for this session."
    } else {
      Add-Result ("Model {0}" -f $Model) "FAIL" $_.Exception.Message
    }
  }
}

Write-Host "" 
Write-Host "PINEAPPLE M7 - OMNIROUTE REPAIR AND VERIFICATION" -ForegroundColor Cyan
Write-Host ("Vault: {0}" -f $M7Root)

try {
  $computer = Get-CimInstance Win32_ComputerSystem
  $os = Get-CimInstance Win32_OperatingSystem
  $ram = [math]::Round($computer.TotalPhysicalMemory / 1GB, 1)
  $freeRam = [math]::Round($os.FreePhysicalMemory / 1MB, 1)
  Add-Result "Machine" "PASS" ("{0}; {1} GB RAM; {2} GB currently free" -f $os.Caption, $ram, $freeRam)
} catch {
  Add-Result "Machine" "NOT TESTED" "Windows hardware details were unavailable."
}

$requiredCommands = @("node", "npm", "omniroute")
foreach ($name in $requiredCommands) {
  $command = Get-Command $name -ErrorAction SilentlyContinue
  Add-Result ("Command {0}" -f $name) ($(if ($command) { "PASS" } else { "FAIL" })) ($(if ($command) { $command.Source } else { "not found on PATH" }))
}
$optionalCommands = @("claude", "codex", "cursor", "opencode", "gemini", "ollama")
foreach ($name in $optionalCommands) {
  $command = Get-Command $name -ErrorAction SilentlyContinue
  Add-Result ("Client {0}" -f $name) ($(if ($command) { "PASS" } else { "OPTIONAL" })) ($(if ($command) { $command.Source } else { "not installed or not on PATH" }))
}

$omni = Get-Command omniroute -ErrorAction SilentlyContinue
if ($omni) {
  try {
    $version = (& omniroute --version 2>&1 | Select-Object -First 1)
    Add-Result "OmniRoute version" "PASS" ([string]$version)
  } catch { Add-Result "OmniRoute version" "FAIL" $_.Exception.Message }
}

if ($StartServices) { Start-PM7Stack }

Test-Service "Local Studio" 3737 "http://127.0.0.1:3737/hermes" $true
Test-Service "Hermes" 9119 "http://127.0.0.1:9119" $true
Test-Service "Free Claude proxy" 8082 "http://127.0.0.1:8082" $false
Test-Service "OmniRoute" 20128 "http://127.0.0.1:20128/v1/models" $true
Test-Service "M7 backend" 51763 "http://127.0.0.1:51763/api/health" $false
Test-Service "Notebook/Obsidian bridge" 8643 "http://127.0.0.1:8643" $false
Test-Service "Ollama" 11434 "http://127.0.0.1:11434/api/tags" $false

if (Test-Port 11434) {
  $ollama = Invoke-Probe "http://127.0.0.1:11434/api/tags"
  if ($ollama.Status -eq 200) {
    try {
      $models = @((ConvertFrom-Json $ollama.Body).models)
      if ($models.Count -eq 0) {
        Add-Result "Ollama models" "OPTIONAL" "Ollama is running with no installed local models."
      } else {
        $names = ($models | ForEach-Object { $_.name }) -join ", "
        Add-Result "Ollama models" "PASS" $names
      }
    } catch { Add-Result "Ollama models" "OPTIONAL" "Could not parse /api/tags." }
  }
}

if ($RunModelTests -and (Test-Port 20128)) {
  $headers = @{}
  if ($env:OMNIROUTE_API_KEY) { $headers["Authorization"] = "Bearer $($env:OMNIROUTE_API_KEY)" }
  foreach ($model in @("auto/best-chat", "auto/best-coding", "auto/best-reasoning")) {
    Test-OmniRouteModel $model $headers
  }
} elseif (-not $RunModelTests) {
  Add-Result "Live model generation" "NOT TESTED" "Run with -RunModelTests to send three 12-token test requests."
}

New-Item -ItemType Directory -Force -Path $Outbox | Out-Null
$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$receipt = Join-Path $Outbox ("PM7_LOCAL_VERIFY_{0}.md" -f $stamp)
$lines = @(
  "---",
  "title: PM7 Local Verification $stamp",
  "status: PAUSED",
  "generated_by: PM7_OMNIROUTE_REPAIR_AND_VERIFY.ps1",
  "---",
  "",
  "# PM7 local verification receipt",
  "",
  "- Computer: $env:COMPUTERNAME",
  "- Vault: ``$M7Root``",
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
  "> This receipt proves only the checks recorded above on this computer at this time. Provider availability and free tiers can change. Publishing and ad spend remain blocked by the Outbox Shield."
)
Set-Content -Path $receipt -Value $lines -Encoding UTF8
Write-Host ("Receipt: {0}" -f $receipt) -ForegroundColor Cyan

$coreFailures = @($Results | Where-Object { $_.Status -eq "FAIL" }).Count
if ($coreFailures -gt 0) { exit 1 }
exit 0
