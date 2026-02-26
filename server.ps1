# Paper Generator Manager for Windows
# PowerShell script untuk mengelola Paper Generator (Flask + Vite)

param([string]$Command = "")

# Configuration
$AppDir    = Split-Path -Parent $MyInvocation.MyCommand.Path
$BackendDir = Join-Path $AppDir "backend"
$FrontendDir = Join-Path $AppDir "frontend"
$BackendPort  = 5000
$FrontendPort = 3000

function Write-Header {
    Write-Host ""
    Write-Host "============================================" -ForegroundColor Cyan
    Write-Host "      Paper Generator Manager" -ForegroundColor Cyan
    Write-Host "       Flask API + Vite Frontend" -ForegroundColor Cyan
    Write-Host "============================================" -ForegroundColor Cyan
    Write-Host ""
}

function Get-ProcessByPort {
    param([int]$Port)
    try {
        $conn = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($conn) {
            return Get-Process -Id $conn.OwningProcess -ErrorAction SilentlyContinue
        }
    } catch {}
    return $null
}

function Check-Status {
    Write-Host "Checking Server Status..." -ForegroundColor Yellow
    Write-Host ""

    # Check Frontend (Vite)
    $frontendProcess = Get-ProcessByPort $FrontendPort
    if ($frontendProcess) {
        Write-Host "   OK - Frontend (Vite):  RUNNING (PID: $($frontendProcess.Id))" -ForegroundColor Green
    } else {
        Write-Host "   NO - Frontend (Vite):  STOPPED" -ForegroundColor Red
    }

    # Check Backend (Flask)
    $backendProcess = Get-ProcessByPort $BackendPort
    if ($backendProcess) {
        Write-Host "   OK - Backend  (Flask): RUNNING (PID: $($backendProcess.Id))" -ForegroundColor Green
    } else {
        Write-Host "   NO - Backend  (Flask): STOPPED" -ForegroundColor Red
    }

    # Port connectivity
    Write-Host ""
    Write-Host "Port Status:" -ForegroundColor Yellow

    if (Test-NetConnection -ComputerName localhost -Port $FrontendPort -InformationLevel Quiet -WarningAction SilentlyContinue) {
        Write-Host "   OK - Port $FrontendPort (Frontend): LISTENING" -ForegroundColor Green
    } else {
        Write-Host "   NO - Port $FrontendPort (Frontend): NOT LISTENING" -ForegroundColor Red
    }

    if (Test-NetConnection -ComputerName localhost -Port $BackendPort -InformationLevel Quiet -WarningAction SilentlyContinue) {
        Write-Host "   OK - Port $BackendPort (Backend):  LISTENING" -ForegroundColor Green
    } else {
        Write-Host "   NO - Port $BackendPort (Backend):  NOT LISTENING" -ForegroundColor Red
    }

    # Dependencies
    Write-Host ""
    Write-Host "Dependencies:" -ForegroundColor Yellow

    if (Get-Command node -ErrorAction SilentlyContinue) {
        Write-Host "   OK - Node.js: $(node -v)" -ForegroundColor Green
    } else {
        Write-Host "   NO - Node.js: Not installed" -ForegroundColor Red
    }

    if (Get-Command npm -ErrorAction SilentlyContinue) {
        Write-Host "   OK - npm:     $(npm -v)" -ForegroundColor Green
    } else {
        Write-Host "   NO - npm:     Not installed" -ForegroundColor Red
    }

    if (Get-Command python -ErrorAction SilentlyContinue) {
        $pyVer = & python --version 2>&1
        Write-Host "   OK - Python:  $pyVer" -ForegroundColor Green
    } else {
        Write-Host "   NO - Python:  Not installed" -ForegroundColor Red
    }

    # .env check
    Write-Host ""
    Write-Host "Configuration:" -ForegroundColor Yellow
    $envFile = Join-Path $BackendDir ".env"
    if (Test-Path $envFile) {
        $hasKey = (Get-Content $envFile) -match "OPENAI_API_KEY\s*=\s*.+"
        if ($hasKey) {
            Write-Host "   OK - backend/.env: Found (OPENAI_API_KEY set)" -ForegroundColor Green
        } else {
            Write-Host "   WN - backend/.env: Found (OPENAI_API_KEY NOT set)" -ForegroundColor Yellow
        }
    } else {
        Write-Host "   NO - backend/.env: NOT FOUND (create it!)" -ForegroundColor Red
    }

    # API health
    Write-Host ""
    Write-Host "API Health:" -ForegroundColor Yellow
    try {
        $resp = Invoke-WebRequest -Uri "http://localhost:$BackendPort/health" -TimeoutSec 2 -UseBasicParsing -ErrorAction SilentlyContinue
        if ($resp.StatusCode -eq 200) {
            Write-Host "   OK - Flask API /health: OK" -ForegroundColor Green
        } else {
            Write-Host "   WN - Flask API /health: $($resp.StatusCode)" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "   NO - Flask API /health: Not responding" -ForegroundColor Red
    }

    # Access URLs
    Write-Host ""
    Write-Host "Access URLs:" -ForegroundColor Cyan
    Write-Host "   http://localhost:$FrontendPort    (Frontend)"
    Write-Host "   http://localhost:$BackendPort    (Backend API)"

    $localIP = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike "127.*" -and $_.IPAddress -notlike "169.*" } | Select-Object -First 1).IPAddress
    if ($localIP) {
        Write-Host "   http://${localIP}:$FrontendPort (local network)"
    }

    Write-Host ""
}

function Start-Services {
    Write-Host "Starting Services..." -ForegroundColor Yellow
    Write-Host ""

    $frontendStarted = $false
    $backendStarted  = $false

    # Start Frontend (Vite)
    if (!(Get-ProcessByPort $FrontendPort)) {
        Write-Host "   Starting Frontend (Vite)..." -ForegroundColor Gray
        $frontendCmd = "Set-Location '$FrontendDir'; npm run dev"
        Start-Process powershell -ArgumentList "-NoExit", "-Command", $frontendCmd
        $frontendStarted = $true
    } else {
        Write-Host "   SKIP - Frontend already running on port $FrontendPort" -ForegroundColor Yellow
    }

    # Start Backend (Flask)
    if (!(Get-ProcessByPort $BackendPort)) {
        Write-Host "   Starting Backend (Flask)..." -ForegroundColor Gray
        $backendCmd = "Set-Location '$BackendDir'; python app.py"
        Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendCmd
        $backendStarted = $true
    } else {
        Write-Host "   SKIP - Backend already running on port $BackendPort" -ForegroundColor Yellow
    }

    # Wait for services
    if ($frontendStarted -or $backendStarted) {
        Write-Host "   Waiting for services to start..." -ForegroundColor Gray
        $timeout = 0
        while ($timeout -lt 30) {
            $frontendOk = Get-ProcessByPort $FrontendPort
            $backendOk  = Get-ProcessByPort $BackendPort

            if ($frontendStarted -and $frontendOk -and -not ($frontendStarted -and -not $frontendOk)) {
                # already reported
            }
            if ($backendStarted -and $backendOk -and -not ($backendStarted -and -not $backendOk)) {
                # already reported
            }

            if ((-not $frontendStarted -or $frontendOk) -and (-not $backendStarted -or $backendOk)) {
                break
            }

            Start-Sleep -Seconds 1
            $timeout++
        }

        if (Get-ProcessByPort $FrontendPort) {
            Write-Host "   OK - Frontend started on port $FrontendPort" -ForegroundColor Green
        } elseif ($frontendStarted) {
            Write-Host "   WN - Frontend may still be starting..." -ForegroundColor Yellow
        }

        if (Get-ProcessByPort $BackendPort) {
            Write-Host "   OK - Backend started on port $BackendPort" -ForegroundColor Green
        } elseif ($backendStarted) {
            Write-Host "   WN - Backend may still be starting..." -ForegroundColor Yellow
        }
    }

    Write-Host ""
    Write-Host "Services started!" -ForegroundColor Green
    Write-Host "   Frontend: http://localhost:$FrontendPort" -ForegroundColor Cyan
    Write-Host "   Backend:  http://localhost:$BackendPort" -ForegroundColor Cyan
    Write-Host ""
}

function Stop-Services {
    Write-Host "Stopping Services..." -ForegroundColor Yellow
    Write-Host ""

    $frontendProcess = Get-ProcessByPort $FrontendPort
    $backendProcess  = Get-ProcessByPort $BackendPort

    if ($frontendProcess) {
        Stop-Process -Id $frontendProcess.Id -Force -ErrorAction SilentlyContinue
        Write-Host "   OK - Frontend (Vite) stopped" -ForegroundColor Green
    } else {
        Write-Host "   SKIP - Frontend not running" -ForegroundColor Yellow
    }

    if ($backendProcess) {
        Stop-Process -Id $backendProcess.Id -Force -ErrorAction SilentlyContinue
        Write-Host "   OK - Backend (Flask) stopped" -ForegroundColor Green
    } else {
        Write-Host "   SKIP - Backend not running" -ForegroundColor Yellow
    }

    Write-Host ""
    Write-Host "Services stopped!" -ForegroundColor Green
    Write-Host ""
}

function Restart-Services {
    Write-Host "Restarting Services..." -ForegroundColor Yellow
    Write-Host ""
    Stop-Services
    Start-Sleep -Seconds 2
    Start-Services
}

function Show-Logs {
    Write-Host "Process Information:" -ForegroundColor Yellow
    Write-Host ""

    $frontendProcess = Get-ProcessByPort $FrontendPort
    if ($frontendProcess) {
        Write-Host "Frontend / Vite (PID: $($frontendProcess.Id))" -ForegroundColor Green
        Write-Host "  Started: $($frontendProcess.StartTime)" -ForegroundColor Gray
        Write-Host "  Memory:  $([math]::Round($frontendProcess.WorkingSet64/1MB, 2)) MB" -ForegroundColor Gray
        Write-Host "  URL:     http://localhost:$FrontendPort" -ForegroundColor Gray
    } else {
        Write-Host "Frontend / Vite: NOT RUNNING" -ForegroundColor Red
    }

    Write-Host ""

    $backendProcess = Get-ProcessByPort $BackendPort
    if ($backendProcess) {
        Write-Host "Backend / Flask (PID: $($backendProcess.Id))" -ForegroundColor Green
        Write-Host "  Started: $($backendProcess.StartTime)" -ForegroundColor Gray
        Write-Host "  Memory:  $([math]::Round($backendProcess.WorkingSet64/1MB, 2)) MB" -ForegroundColor Gray
        Write-Host "  URL:     http://localhost:$BackendPort" -ForegroundColor Gray
    } else {
        Write-Host "Backend / Flask: NOT RUNNING" -ForegroundColor Red
    }

    Write-Host ""
}

function Install-Dependencies {
    Write-Host "Installing Dependencies..." -ForegroundColor Yellow
    Write-Host ""

    # Frontend
    Write-Host "   Installing frontend (npm)..." -ForegroundColor Gray
    Push-Location $FrontendDir
    npm install
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   OK - Frontend deps installed" -ForegroundColor Green
    } else {
        Write-Host "   ERROR - Frontend deps failed" -ForegroundColor Red
    }
    Pop-Location

    # Backend
    Write-Host "   Installing backend (pip)..." -ForegroundColor Gray
    Push-Location $BackendDir
    python -m pip install -r requirements.txt
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   OK - Backend deps installed" -ForegroundColor Green
    } else {
        Write-Host "   ERROR - Backend deps failed" -ForegroundColor Red
    }
    Pop-Location

    Write-Host ""
    Write-Host "Dependencies installed!" -ForegroundColor Green
    Write-Host ""
}

function Rebuild-App {
    Write-Host "Rebuilding Frontend..." -ForegroundColor Yellow
    Write-Host ""

    Stop-Services
    Push-Location $FrontendDir

    Write-Host "   Building Vite..." -ForegroundColor Gray
    npm run build

    if ($LASTEXITCODE -eq 0) {
        Write-Host "   OK - Build successful" -ForegroundColor Green
        Pop-Location
        Start-Services
    } else {
        Write-Host "   ERROR - Build failed" -ForegroundColor Red
        Pop-Location
    }
    Write-Host ""
}

function Setup-Firewall {
    Write-Host "Setting Up Firewall..." -ForegroundColor Yellow
    Write-Host ""

    try {
        Remove-NetFirewallRule -DisplayName "PaperGen Frontend*" -ErrorAction SilentlyContinue
        Remove-NetFirewallRule -DisplayName "PaperGen Backend*" -ErrorAction SilentlyContinue

        New-NetFirewallRule -DisplayName "PaperGen Frontend (Vite)" -Direction Inbound -Protocol TCP -LocalPort $FrontendPort -Action Allow -Profile Any | Out-Null
        Write-Host "   OK - Port $FrontendPort opened (Frontend)" -ForegroundColor Green

        New-NetFirewallRule -DisplayName "PaperGen Backend (Flask)" -Direction Inbound -Protocol TCP -LocalPort $BackendPort -Action Allow -Profile Any | Out-Null
        Write-Host "   OK - Port $BackendPort opened (Backend)" -ForegroundColor Green

        Write-Host ""
        Write-Host "Firewall configured!" -ForegroundColor Green
    } catch {
        Write-Host "   ERROR - Run as Administrator!" -ForegroundColor Red
    }
    Write-Host ""
}

function Show-Help {
    Write-Host "Usage: .\paper-manager.ps1 <command>"
    Write-Host ""
    Write-Host "Commands:"
    Write-Host "  start    - Start frontend + backend"
    Write-Host "  stop     - Stop frontend + backend"
    Write-Host "  restart  - Restart all services"
    Write-Host "  status   - Check service status"
    Write-Host "  logs     - Show process info"
    Write-Host "  install  - Install npm + pip dependencies"
    Write-Host "  rebuild  - Rebuild frontend (vite build)"
    Write-Host "  firewall - Open ports in firewall (admin)"
    Write-Host "  help     - Show this help"
    Write-Host ""
    Write-Host "Ports:"
    Write-Host "  $FrontendPort - Frontend (Vite / Vue)"
    Write-Host "  $BackendPort - Backend  (Flask API)"
    Write-Host ""
}

function Show-Menu {
    Write-Host "Select an option:" -ForegroundColor Cyan
    Write-Host "  1 - Start services"
    Write-Host "  2 - Stop services"
    Write-Host "  3 - Restart services"
    Write-Host "  4 - Check status"
    Write-Host "  5 - Show logs"
    Write-Host "  6 - Install dependencies"
    Write-Host "  7 - Rebuild frontend"
    Write-Host "  8 - Setup firewall"
    Write-Host "  9 - Exit"
    Write-Host ""

    $choice = Read-Host "Enter choice (1-9)"

    switch ($choice) {
        "1" { Start-Services }
        "2" { Stop-Services }
        "3" { Restart-Services }
        "4" { Check-Status }
        "5" { Show-Logs }
        "6" { Install-Dependencies }
        "7" { Rebuild-App }
        "8" { Setup-Firewall }
        "9" { exit 0 }
        default { Write-Host "Invalid choice" -ForegroundColor Red }
    }
}

# ─── Main ─────────────────────────────────────────────────────────────────────
Write-Header

switch ($Command) {
    "start"    { Start-Services }
    "stop"     { Stop-Services }
    "restart"  { Restart-Services }
    "status"   { Check-Status }
    "logs"     { Show-Logs }
    "install"  { Install-Dependencies }
    "rebuild"  { Rebuild-App }
    "firewall" { Setup-Firewall }
    { $_ -in @("help", "-h", "--help") } { Show-Help }
    default {
        if ([string]::IsNullOrEmpty($Command)) {
            Show-Menu
        } else {
            Write-Host "Unknown command: $Command" -ForegroundColor Red
            Write-Host ""
            Show-Help
        }
    }
}
