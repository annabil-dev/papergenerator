#!/bin/bash
#
# Paper Generator Manager
# Script untuk mengelola Paper Generator (Flask API + Vite Frontend)
#

# ─── Colors ───────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
GRAY='\033[0;37m'
NC='\033[0m' # No Color

# ─── Paths & Ports ────────────────────────────────────────────────────────────
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$APP_DIR/backend"
FRONTEND_DIR="$APP_DIR/frontend"
BACKEND_PORT=5000
FRONTEND_PORT=3000
BACKEND_LOG="/tmp/paper-backend.log"
FRONTEND_LOG="/tmp/paper-frontend.log"

# ─── Header ───────────────────────────────────────────────────────────────────
print_header() {
    echo ""
    echo -e "${CYAN}╔════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║      Paper Generator Manager           ║${NC}"
    echo -e "${CYAN}║       Flask API + Vite Frontend        ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════╝${NC}"
    echo ""
}

# ─── Helpers ──────────────────────────────────────────────────────────────────
port_pid() {
    lsof -ti tcp:"$1" 2>/dev/null | head -1
}

port_listening() {
    if command -v ss &>/dev/null; then
        ss -tlnp 2>/dev/null | grep -q ":$1 "
    elif command -v netstat &>/dev/null; then
        netstat -tlnp 2>/dev/null | grep -q ":$1 "
    else
        lsof -i tcp:"$1" &>/dev/null
    fi
}

# ─── Status ───────────────────────────────────────────────────────────────────
check_status() {
    echo -e "${YELLOW}Checking Server Status...${NC}"
    echo ""

    # Frontend
    FRONTEND_PID=$(port_pid $FRONTEND_PORT)
    if [ -n "$FRONTEND_PID" ]; then
        echo -e "   ${GREEN}OK${NC} - Frontend (Vite):  ${GREEN}RUNNING${NC} (PID: $FRONTEND_PID)"
    else
        echo -e "   ${RED}NO${NC} - Frontend (Vite):  ${RED}STOPPED${NC}"
    fi

    # Backend
    BACKEND_PID=$(port_pid $BACKEND_PORT)
    if [ -n "$BACKEND_PID" ]; then
        echo -e "   ${GREEN}OK${NC} - Backend  (Flask): ${GREEN}RUNNING${NC} (PID: $BACKEND_PID)"
    else
        echo -e "   ${RED}NO${NC} - Backend  (Flask): ${RED}STOPPED${NC}"
    fi

    # Ports
    echo ""
    echo -e "${YELLOW}Port Status:${NC}"
    if port_listening $FRONTEND_PORT; then
        echo -e "   ${GREEN}OK${NC} - Port $FRONTEND_PORT (Frontend): LISTENING"
    else
        echo -e "   ${RED}NO${NC} - Port $FRONTEND_PORT (Frontend): NOT LISTENING"
    fi
    if port_listening $BACKEND_PORT; then
        echo -e "   ${GREEN}OK${NC} - Port $BACKEND_PORT (Backend):  LISTENING"
    else
        echo -e "   ${RED}NO${NC} - Port $BACKEND_PORT (Backend):  NOT LISTENING"
    fi

    # Dependencies
    echo ""
    echo -e "${YELLOW}Dependencies:${NC}"
    if command -v node &>/dev/null; then
        echo -e "   ${GREEN}OK${NC} - Node.js: $(node -v)"
    else
        echo -e "   ${RED}NO${NC} - Node.js: Not installed"
    fi
    if command -v npm &>/dev/null; then
        echo -e "   ${GREEN}OK${NC} - npm:     $(npm -v)"
    else
        echo -e "   ${RED}NO${NC} - npm:     Not installed"
    fi
    PYTHON_CMD=""
    if command -v python3 &>/dev/null; then
        PYTHON_CMD="python3"
        echo -e "   ${GREEN}OK${NC} - Python:  $(python3 --version)"
    elif command -v python &>/dev/null; then
        PYTHON_CMD="python"
        echo -e "   ${GREEN}OK${NC} - Python:  $(python --version)"
    else
        echo -e "   ${RED}NO${NC} - Python:  Not installed"
    fi

    # .env check
    echo ""
    echo -e "${YELLOW}Configuration:${NC}"
    if [ -f "$BACKEND_DIR/.env" ]; then
        if grep -qE '^OPENAI_API_KEY\s*=\s*.+' "$BACKEND_DIR/.env" 2>/dev/null; then
            echo -e "   ${GREEN}OK${NC} - backend/.env: Found (OPENAI_API_KEY set)"
        else
            echo -e "   ${YELLOW}WN${NC} - backend/.env: Found (OPENAI_API_KEY NOT set)"
        fi
    else
        echo -e "   ${RED}NO${NC} - backend/.env: NOT FOUND (create it!)"
    fi

    # API health
    echo ""
    echo -e "${YELLOW}API Health:${NC}"
    if command -v curl &>/dev/null; then
        HEALTH=$(timeout 2 curl -s -o /dev/null -w "%{http_code}" http://localhost:$BACKEND_PORT/health 2>/dev/null)
        if [ "$HEALTH" = "200" ]; then
            echo -e "   ${GREEN}OK${NC} - Flask API /health: OK"
        else
            echo -e "   ${RED}NO${NC} - Flask API /health: Not responding ($HEALTH)"
        fi
    fi

    # Access URLs
    echo ""
    echo -e "${CYAN}Access URLs:${NC}"
    echo -e "   http://localhost:$FRONTEND_PORT    (Frontend)"
    echo -e "   http://localhost:$BACKEND_PORT    (Backend API)"
    LOCAL_IP=$(hostname -I 2>/dev/null | awk '{print $1}')
    if [ -n "$LOCAL_IP" ]; then
        echo -e "   http://$LOCAL_IP:$FRONTEND_PORT (local network)"
    fi
    echo ""
}

# ─── Start ────────────────────────────────────────────────────────────────────
start_services() {
    echo -e "${YELLOW}Starting Services...${NC}"
    echo ""

    PYTHON_CMD="python3"
    command -v python3 &>/dev/null || PYTHON_CMD="python"

    # Start Backend (Flask)
    BACKEND_PID=$(port_pid $BACKEND_PORT)
    if [ -z "$BACKEND_PID" ]; then
        echo -e "   ${GRAY}Starting Backend (Flask)...${NC}"
        cd "$BACKEND_DIR"
        nohup $PYTHON_CMD app.py > "$BACKEND_LOG" 2>&1 &
        BACKEND_PID=$!
        echo -e "   ${GREEN}OK${NC} - Backend started (PID: $BACKEND_PID)"
    else
        echo -e "   ${YELLOW}SKIP${NC} - Backend already running on port $BACKEND_PORT"
    fi

    # Start Frontend (Vite)
    FRONTEND_PID=$(port_pid $FRONTEND_PORT)
    if [ -z "$FRONTEND_PID" ]; then
        echo -e "   ${GRAY}Starting Frontend (Vite)...${NC}"
        cd "$FRONTEND_DIR"
        nohup npm run dev > "$FRONTEND_LOG" 2>&1 &
        FRONTEND_PID=$!
        echo -e "   ${GREEN}OK${NC} - Frontend started (PID: $FRONTEND_PID)"
    else
        echo -e "   ${YELLOW}SKIP${NC} - Frontend already running on port $FRONTEND_PORT"
    fi

    # Wait for ports to open
    echo -e "   ${GRAY}Waiting for services to start...${NC}"
    TIMEOUT=30
    for i in $(seq 1 $TIMEOUT); do
        FPORT=$(port_pid $FRONTEND_PORT)
        BPORT=$(port_pid $BACKEND_PORT)
        if [ -n "$FPORT" ] && [ -n "$BPORT" ]; then
            break
        fi
        sleep 1
    done

    echo ""
    echo -e "${GREEN}Services started!${NC}"
    echo -e "   Frontend: http://localhost:$FRONTEND_PORT"
    echo -e "   Backend:  http://localhost:$BACKEND_PORT"
    echo ""
}

# ─── Stop ─────────────────────────────────────────────────────────────────────
stop_services() {
    echo -e "${YELLOW}Stopping Services...${NC}"
    echo ""

    FRONTEND_PID=$(port_pid $FRONTEND_PORT)
    if [ -n "$FRONTEND_PID" ]; then
        kill -TERM "$FRONTEND_PID" 2>/dev/null
        sleep 1
        kill -KILL "$FRONTEND_PID" 2>/dev/null
        echo -e "   ${GREEN}OK${NC} - Frontend (Vite) stopped"
    else
        echo -e "   ${YELLOW}SKIP${NC} - Frontend not running"
    fi

    BACKEND_PID=$(port_pid $BACKEND_PORT)
    if [ -n "$BACKEND_PID" ]; then
        kill -TERM "$BACKEND_PID" 2>/dev/null
        sleep 1
        kill -KILL "$BACKEND_PID" 2>/dev/null
        echo -e "   ${GREEN}OK${NC} - Backend (Flask) stopped"
    else
        echo -e "   ${YELLOW}SKIP${NC} - Backend not running"
    fi

    echo ""
    echo -e "${GREEN}Services stopped!${NC}"
    echo ""
}

# ─── Restart ──────────────────────────────────────────────────────────────────
restart_services() {
    echo -e "${YELLOW}Restarting Services...${NC}"
    echo ""
    stop_services
    sleep 2
    start_services
}

# ─── Logs ─────────────────────────────────────────────────────────────────────
show_logs() {
    echo -e "${YELLOW}Recent Logs:${NC}"
    echo ""

    echo -e "${BLUE}=== Backend (Flask) Log ===${NC}"
    if [ -f "$BACKEND_LOG" ]; then
        tail -20 "$BACKEND_LOG"
    else
        echo "No log file found at $BACKEND_LOG"
    fi

    echo ""
    echo -e "${BLUE}=== Frontend (Vite) Log ===${NC}"
    if [ -f "$FRONTEND_LOG" ]; then
        tail -20 "$FRONTEND_LOG"
    else
        echo "No log file found at $FRONTEND_LOG"
    fi

    echo ""
}

# ─── Install ──────────────────────────────────────────────────────────────────
install_deps() {
    echo -e "${YELLOW}Installing Dependencies...${NC}"
    echo ""

    echo -e "   Installing frontend (npm)..."
    cd "$FRONTEND_DIR"
    npm install
    if [ $? -eq 0 ]; then
        echo -e "   ${GREEN}OK${NC} - Frontend deps installed"
    else
        echo -e "   ${RED}ERROR${NC} - Frontend deps failed"
    fi

    echo -e "   Installing backend (pip)..."
    PYTHON_CMD="python3"
    command -v python3 &>/dev/null || PYTHON_CMD="python"
    cd "$BACKEND_DIR"
    $PYTHON_CMD -m pip install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo -e "   ${GREEN}OK${NC} - Backend deps installed"
    else
        echo -e "   ${RED}ERROR${NC} - Backend deps failed"
    fi

    echo ""
    echo -e "${GREEN}Dependencies installed!${NC}"
    echo ""
}

# ─── Rebuild ──────────────────────────────────────────────────────────────────
rebuild() {
    echo -e "${YELLOW}Rebuilding Frontend...${NC}"
    echo ""

    stop_services

    cd "$FRONTEND_DIR"
    echo -e "   Building Vite..."
    npm run build
    if [ $? -eq 0 ]; then
        echo -e "   ${GREEN}OK${NC} - Build successful"
        start_services
    else
        echo -e "   ${RED}ERROR${NC} - Build failed"
    fi
    echo ""
}

# ─── Help ─────────────────────────────────────────────────────────────────────
show_help() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  start    - Start frontend + backend"
    echo "  stop     - Stop frontend + backend"
    echo "  restart  - Restart all services"
    echo "  status   - Check service status"
    echo "  logs     - Show recent logs"
    echo "  install  - Install npm + pip dependencies"
    echo "  rebuild  - Rebuild frontend (vite build)"
    echo "  help     - Show this help"
    echo ""
    echo "Ports:"
    echo "  $FRONTEND_PORT - Frontend (Vite / Vue)"
    echo "  $BACKEND_PORT - Backend  (Flask API)"
    echo ""
}

# ─── Interactive Menu ─────────────────────────────────────────────────────────
show_menu() {
    echo "Select an option:"
    echo "  1) Start services"
    echo "  2) Stop services"
    echo "  3) Restart services"
    echo "  4) Check status"
    echo "  5) Show logs"
    echo "  6) Install dependencies"
    echo "  7) Rebuild frontend"
    echo "  8) Exit"
    echo ""
    read -rp "Enter choice [1-8]: " choice
    case $choice in
        1) start_services ;;
        2) stop_services ;;
        3) restart_services ;;
        4) check_status ;;
        5) show_logs ;;
        6) install_deps ;;
        7) rebuild ;;
        8) exit 0 ;;
        *) echo -e "${RED}Invalid choice${NC}" ;;
    esac
}

# ─── Main ─────────────────────────────────────────────────────────────────────
print_header

case "$1" in
    start)   start_services ;;
    stop)    stop_services ;;
    restart) restart_services ;;
    status)  check_status ;;
    logs)    show_logs ;;
    install) install_deps ;;
    rebuild) rebuild ;;
    help|--help|-h) show_help ;;
    "")
        show_menu
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        echo ""
        show_help
        ;;
esac
