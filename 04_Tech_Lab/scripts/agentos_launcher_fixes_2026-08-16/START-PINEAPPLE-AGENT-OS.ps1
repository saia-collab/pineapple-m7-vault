[CmdletBinding()]
param([switch]$NoPause)

$ErrorActionPreference = "Stop"
$M7Root = "C:\Pineapple Contractors M7"
$TechRoot = Join-Path $M7Root "04_Tech_Lab"
$AppRoot = Join-Path $TechRoot "Pineapple_Agent_OS"
$Current = Join-Path $AppRoot "current"
$HermesHome = Join-Path $env:LOCALAPPDATA "hermes"
$LogDir = Join-Path $TechRoot "logs"
$RunLog = Join-Path $LogDir "pineapple-agent-os-live.log"

function Port-IsOpen([int]$Port) {
  return [bool](Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction SilentlyContinue)
}
function Stop-OldAgentOS3000 {
  # The current Studio runs on 3737. Anything still listening on :3000 is an OLD
  # agent-os build (the "second studio" Saia was seeing) — stop it so exactly one
  # Studio is ever up. Nothing else in this stack uses :3000.
  $ids = (Get-NetTCPConnection -State Listen -LocalPort 3000 -ErrorAction SilentlyContinue).OwningProcess | Select-Object -Unique
  foreach ($id in $ids) { if ($id) { Stop-Process -Id $id -Force -ErrorAction SilentlyContinue } }
}
function Find-Hermes {
  $found = Get-Command hermes.exe -ErrorAction SilentlyContinue
  if ($found) { return $found.Source }
  $known = Join-Path $env:LOCALAPPDATA "hermes\hermes-agent\venv\Scripts\hermes.exe"
  if (Test-Path $known) { return $known }
  return $null
}
function Start-HiddenCommand([string]$WorkingDirectory, [string]$Command) {
  Start-Process -FilePath $env:ComSpec -WorkingDirectory $WorkingDirectory -ArgumentList @('/d','/s','/c',"`"$Command`"") -WindowStyle Hidden | Out-Null
}
function Wait-Web([string]$Url, [int]$Seconds) {
  $until = (Get-Date).AddSeconds($Seconds)
  do {
    try {
      $r = Invoke-WebRequest -UseBasicParsing -Uri $Url -TimeoutSec 3
      if ($r.StatusCode -ge 200 -and $r.StatusCode -lt 500) { return $true }
    } catch {}
    Start-Sleep 2
  } while ((Get-Date) -lt $until)
  return $false
}

try {
  New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
  if (-not (Test-Path (Join-Path $Current "package.json"))) { throw "The current Agent OS is not installed. Run DOUBLE_CLICK_INSTALL_AND_START.bat once." }
  $npm = Get-Command npm.cmd -ErrorAction SilentlyContinue
  if (-not $npm) { throw "Node.js/npm is missing." }

  Write-Host "Starting Pineapple Local Studio..." -ForegroundColor Cyan
  $env:HERMES_HOME = $HermesHome
  $env:PORT = "3737"
  Stop-OldAgentOS3000

  $hermes = Find-Hermes
  if ($hermes -and -not (Port-IsOpen 9119)) {
    Start-Process -FilePath $hermes -ArgumentList @('dashboard','--no-open','--port','9119','--skip-build') -WindowStyle Hidden | Out-Null
  }

  # Free Claude Code proxy on :8082 — powers the "Free Claude Code" tab + its /admin key panel
  # (paste API keys in a UI, no terminal). This is why the standalone launcher is no longer needed.
  if (-not (Port-IsOpen 8082)) {
    # Free Claude Code proxy → routes the `claude` CLI to the cloud FREE tier (Groq).
    # Resolve the .exe shim explicitly: $fcc.Source can be the extension-less script,
    # which Start-Process cannot launch — that was why 8082 kept coming up dead.
    $fcc = Get-Command fcc-server -ErrorAction SilentlyContinue
    if ($fcc) {
      $fccExe = if (Test-Path "$($fcc.Source).exe") { "$($fcc.Source).exe" } else { $fcc.Source }
      $fccLog = Join-Path $LogDir "fcc-8082.log"
      # fcc-server reads $env:PORT. The launcher set PORT=3737 for the Studio, so fcc INHERITED 3737
      # and bound the Studio's port (leaving :8082 dead — the "Free Claude Code offline" bug).
      # Pin PORT=8082 for THIS child only, then restore 3737 for the Studio that starts below.
      $savedPort = $env:PORT
      $env:PORT = '8082'
      try { Start-Process -FilePath $fccExe -WindowStyle Hidden -RedirectStandardOutput $fccLog -RedirectStandardError "$fccLog.err" | Out-Null }
      finally { $env:PORT = $savedPort }
    }
  }

  # OmniRoute free-model router on :20128 — the Free Claude Code tab routes through this.
  # Launch via cmd so the omniroute.cmd shim RUNS. (Get-Command resolves omniroute.ps1 first, and
  # Start-Process on a .ps1 just opens it in Notepad — that was the "omniroute opens in Notepad" bug.)
  # Working dir = $AppRoot (NOT $Current): a process whose CWD sits inside current\ locks that folder,
  # which made the updater's swap fail with "file is being used by another process". Keep omniroute out of current\.
  if (-not (Port-IsOpen 20128)) {
    # Force PORT=20128 for omniroute. START sets $env:PORT=3737 for the Studio, and a child
    # process INHERITS it — omniroute would then bind 3737 and DISPLACE the Studio (the
    # "two studios" / OmniRoute-dashboard-on-3737 bug Saia hit). Pin it to its real port.
    if (Get-Command omniroute -ErrorAction SilentlyContinue) { Start-HiddenCommand $AppRoot "set PORT=20128&& set OMNIROUTE_PORT=20128&& omniroute" }
  }

  if (-not (Port-IsOpen 51763) -and (Test-Path (Join-Path $TechRoot "server_m7.py"))) {
    $python = Get-Command python.exe -ErrorAction SilentlyContinue
    if (-not $python) { $python = Get-Command py.exe -ErrorAction SilentlyContinue }
    if ($python) { Start-Process -FilePath $python.Source -WorkingDirectory $TechRoot -ArgumentList @((Join-Path $TechRoot "server_m7.py")) -WindowStyle Hidden | Out-Null }
  }

  if (-not (Port-IsOpen 3100) -and (Test-Path (Join-Path $M7Root "START_PAPERCLIP.bat"))) {
    Start-Process -FilePath (Join-Path $M7Root "START_PAPERCLIP.bat") -WindowStyle Minimized | Out-Null
  }

  if (-not (Port-IsOpen 3001)) {
    $openSeoCandidates = @(
      (Join-Path $env:USERPROFILE "open-seo"),
      (Join-Path $env:USERPROFILE "OpenSEO"),
      (Join-Path $TechRoot "open-seo")
    )
    $openSeo = $openSeoCandidates | Where-Object { Test-Path (Join-Path $_ "docker-compose.yml") } | Select-Object -First 1
    if ($openSeo -and (Get-Command docker.exe -ErrorAction SilentlyContinue)) {
      Start-HiddenCommand $openSeo "docker compose up -d"
    }
  }

  $studioAlready = Port-IsOpen 3737
  if (-not $studioAlready) {
    $escapedHome = $HermesHome.Replace('"','')
    $escapedLog = $RunLog.Replace('"','')
    # Use a stable virtual route instead of a provider-specific model ID. Provider catalogs,
    # free tiers, and auth requirements change; OMNIROUTE_MODEL can override this per machine.
    # Any OMNIROUTE_API_KEY already present in the parent environment is inherited by the app.
    $routeModel = if ($env:OMNIROUTE_MODEL) { $env:OMNIROUTE_MODEL } else { "auto/best-coding" }
    $escapedModel = $routeModel.Replace('"','')
    $command = "set HERMES_HOME=$escapedHome&& set PORT=3737&& set OMNIROUTE_MODEL=$escapedModel&& npm start 1>>`"$escapedLog`" 2>>&1"
    Start-HiddenCommand $Current $command
  }

  if (-not (Wait-Web "http://127.0.0.1:3737/hermes" 90)) { throw "Local Studio did not become ready. Send pineapple-agent-os-live.log to ChatGPT." }
  # Always open the Studio in the browser when the launcher runs — that's the whole point of
  # clicking it. (The old "two studios" was the OmniRoute:3737 port collision, now fixed, NOT this.)
  Start-Process "http://localhost:3737/hermes"
  Write-Host "READY - Hermes opened at http://localhost:3737/hermes" -ForegroundColor Yellow
  Write-Host "SEO is under http://localhost:3737/seo and remains PAUSED until you approve publishing." -ForegroundColor Cyan
  exit 0
} catch {
  Write-Host "Could not start Local Studio: $($_.Exception.Message)" -ForegroundColor Red
  Write-Host "Log: $RunLog" -ForegroundColor Yellow
  if (-not $NoPause) { Read-Host "Press Enter to close" | Out-Null }
  exit 1
}
