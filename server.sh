#!/bin/bash
#
# Paper Generator Manager
# Script untuk mengelola Paper Generator (Flask API + Vite Frontend)
# Mode produksi: PM2 + Nginx + Certbot
#

# ─── Colors ───────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
GRAY='\033[0;37m'
NC='\033[0m'

# ─── Paths & Ports ────────────────────────────────────────────────────────────
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$APP_DIR/backend"
FRONTEND_DIR="$APP_DIR/frontend"
LOGS_DIR="$APP_DIR/logs"
ECOSYSTEM="$APP_DIR/ecosystem.config.cjs"
NGINX_CONF="$APP_DIR/nginx.conf"
NGINX_SITES="/etc/nginx/sites-available"
NGINX_ENABLED="/etc/nginx/sites-enabled"
DOMAIN="paperfull.app"
BACKEND_PORT=8001
FRONTEND_PORT=8000

# ─── Header ───────────────────────────────────────────────────────────────────
print_header() {
    echo ""
    echo -e "${CYAN}╔════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║      Paper Generator Manager           ║${NC}"
    echo -e "${CYAN}║   Flask:8001  •  Vite:8000  •  PM2    ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════╝${NC}"
    echo ""
}

# ─── Helpers ──────────────────────────────────────────────────────────────────
require_root() {
    if [[ $EUID -ne 0 ]]; then
        echo -e "${RED}ERROR${NC} - This action requires root. Run with sudo."
        exit 1
    fi
}

port_pid() { lsof -ti tcp:"$1" 2>/dev/null | head -1; }

port_listening() {
    if command -v ss &>/dev/null; then
        ss -tlnp 2>/dev/null | grep -q ":$1 "
    elif command -v netstat &>/dev/null; then
        netstat -tlnp 2>/dev/null | grep -q ":$1 "
    else
        lsof -i tcp:"$1" &>/dev/null
    fi
}

pm2_running() { pm2 list 2>/dev/null | grep -q "$1"; }

find_pm2() {
    if command -v pm2 &>/dev/null; then
        echo "pm2"
        return
    fi
    for p in \
        /home/ubuntu/.nvm/versions/node/*/bin/pm2 \
        /root/.nvm/versions/node/*/bin/pm2 \
        /usr/local/bin/pm2 \
        /usr/bin/pm2; do
        local match
        match=$(ls $p 2>/dev/null | head -1)
        if [ -n "$match" ]; then
            echo "$match"
            return
        fi
    done
    echo ""
}

# ─── Status ───────────────────────────────────────────────────────────────────
check_status() {
    echo -e "${YELLOW}Checking Server Status...${NC}"
    echo ""

    echo -e "${YELLOW}PM2 Apps:${NC}"
    if command -v pm2 &>/dev/null; then
        if pm2_running "paper-frontend"; then
            echo -e "   ${GREEN}OK${NC} - Frontend (paper-frontend): RUNNING"
        else
            echo -e "   ${RED}NO${NC} - Frontend (paper-frontend): STOPPED"
        fi
        if pm2_running "paper-backend"; then
            echo -e "   ${GREEN}OK${NC} - Backend  (paper-backend):  RUNNING"
        else
            echo -e "   ${RED}NO${NC} - Backend  (paper-backend):  STOPPED"
        fi
    else
        echo -e "   ${RED}NO${NC} - pm2 not installed"
    fi

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

    echo ""
    echo -e "${YELLOW}Nginx:${NC}"
    if systemctl is-active --quiet nginx 2>/dev/null; then
        echo -e "   ${GREEN}OK${NC} - nginx: ACTIVE"
    else
        echo -e "   ${RED}NO${NC} - nginx: NOT ACTIVE"
    fi
    if [ -L "$NGINX_ENABLED/$DOMAIN" ]; then
        echo -e "   ${GREEN}OK${NC} - Site $DOMAIN: ENABLED"
    else
        echo -e "   ${RED}NO${NC} - Site $DOMAIN: NOT ENABLED (run: setup-nginx)"
    fi

    echo ""
    echo -e "${YELLOW}SSL (Certbot):${NC}"
    if sudo test -f "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" 2>/dev/null; then
        EXPIRY=$(sudo openssl x509 -enddate -noout -in /etc/letsencrypt/live/$DOMAIN/fullchain.pem 2>/dev/null | cut -d= -f2)
        echo -e "   ${GREEN}OK${NC} - Certificate found (expires: $EXPIRY)"
    else
        echo -e "   ${YELLOW}NO${NC} - No certificate yet (run: setup-ssl)"
    fi

    echo ""
    echo -e "${YELLOW}Dependencies:${NC}"
    command -v node    &>/dev/null && echo -e "   ${GREEN}OK${NC} - Node.js: $(node -v)"             || echo -e "   ${RED}NO${NC} - Node.js: Not installed"
    command -v npm     &>/dev/null && echo -e "   ${GREEN}OK${NC} - npm:     $(npm -v)"              || echo -e "   ${RED}NO${NC} - npm:     Not installed"
    command -v pm2     &>/dev/null && echo -e "   ${GREEN}OK${NC} - pm2:     $(pm2 -v)"              || echo -e "   ${RED}NO${NC} - pm2:     Not installed (npm i -g pm2)"
    command -v python3 &>/dev/null && echo -e "   ${GREEN}OK${NC} - Python:  $(python3 --version)"   || echo -e "   ${RED}NO${NC} - Python:  Not installed"
    command -v certbot &>/dev/null && echo -e "   ${GREEN}OK${NC} - certbot: $(certbot --version 2>&1)" || echo -e "   ${YELLOW}WN${NC} - certbot: Not installed"
    command -v nginx   &>/dev/null && echo -e "   ${GREEN}OK${NC} - nginx:   installed"              || echo -e "   ${RED}NO${NC} - nginx:   Not installed"

    echo ""
    echo -e "${YELLOW}Configuration:${NC}"
    if [ -f "$BACKEND_DIR/.env" ]; then
        if grep -qE '^OPENAI_API_KEY\s*=\s*.+' "$BACKEND_DIR/.env" 2>/dev/null; then
            echo -e "   ${GREEN}OK${NC} - backend/.env: OPENAI_API_KEY set"
        else
            echo -e "   ${YELLOW}WN${NC} - backend/.env: OPENAI_API_KEY NOT set"
        fi
    else
        echo -e "   ${RED}NO${NC} - backend/.env: NOT FOUND"
    fi

    echo ""
    echo -e "${YELLOW}API Health:${NC}"
    if command -v curl &>/dev/null; then
        HEALTH=$(timeout 3 curl -s -o /dev/null -w "%{http_code}" http://localhost:$BACKEND_PORT/api/health 2>/dev/null)
        if [ "$HEALTH" = "200" ]; then
            echo -e "   ${GREEN}OK${NC} - Flask API /api/health: OK"
        else
            echo -e "   ${RED}NO${NC} - Flask API /api/health: Not responding ($HEALTH)"
        fi
    fi

    echo ""
    echo -e "${CYAN}Access URLs:${NC}"
    echo -e "   https://$DOMAIN          (Production)"
    echo -e "   http://localhost:$FRONTEND_PORT  (Frontend direct)"
    echo -e "   http://localhost:$BACKEND_PORT  (Backend direct)"
    LOCAL_IP=$(hostname -I 2>/dev/null | awk '{print $1}')
    [ -n "$LOCAL_IP" ] && echo -e "   http://$LOCAL_IP:$FRONTEND_PORT (local network)"
    echo ""
}

# ─── Build ────────────────────────────────────────────────────────────────────
build_frontend() {
    echo -e "${YELLOW}Building Frontend...${NC}"
    cd "$FRONTEND_DIR"
    [ ! -d node_modules ] && npm install
    chmod -R +x node_modules/.bin/ 2>/dev/null || true
    npx vite build
    if [ $? -eq 0 ]; then
        echo -e "   ${GREEN}OK${NC} - Vite build successful → frontend/dist/"
    else
        echo -e "   ${RED}ERROR${NC} - Vite build failed"
        exit 1
    fi
}

# ─── Start ────────────────────────────────────────────────────────────────────
start_services() {
    echo -e "${YELLOW}Starting Services via PM2...${NC}"
    echo ""

    mkdir -p "$LOGS_DIR"

    if ! command -v pm2 &>/dev/null; then
        echo -e "   ${RED}ERROR${NC} - pm2 not found. Install with: npm install -g pm2"
        exit 1
    fi

    build_frontend
    echo ""

    if pm2 list 2>/dev/null | grep -qE "paper-backend|paper-frontend"; then
        echo -e "   ${GRAY}Reloading PM2 apps...${NC}"
        pm2 reload "$ECOSYSTEM" --update-env
    else
        echo -e "   ${GRAY}Starting PM2 apps...${NC}"
        pm2 start "$ECOSYSTEM"
    fi

    pm2 save

    echo ""
    echo -e "${GREEN}Services started!${NC}"
    echo -e "   Frontend: http://localhost:$FRONTEND_PORT"
    echo -e "   Backend:  http://localhost:$BACKEND_PORT"
    echo -e "   Domain:   https://$DOMAIN"
    echo ""
}

# ─── Stop ─────────────────────────────────────────────────────────────────────
stop_services() {
    echo -e "${YELLOW}Stopping Services...${NC}"
    echo ""

    if ! command -v pm2 &>/dev/null; then
        echo -e "   ${RED}ERROR${NC} - pm2 not found."
        exit 1
    fi

    pm2 stop paper-backend  2>/dev/null && echo -e "   ${GREEN}OK${NC} - paper-backend stopped"  || echo -e "   ${YELLOW}SKIP${NC} - paper-backend not running"
    pm2 stop paper-frontend 2>/dev/null && echo -e "   ${GREEN}OK${NC} - paper-frontend stopped" || echo -e "   ${YELLOW}SKIP${NC} - paper-frontend not running"

    echo ""
    echo -e "${GREEN}Services stopped!${NC}"
    echo ""
}

# ─── Restart ──────────────────────────────────────────────────────────────────
restart_services() {
    echo -e "${YELLOW}Restarting Services...${NC}"
    echo ""
    build_frontend
    echo ""
    pm2 restart "$ECOSYSTEM" --update-env
    pm2 save
    echo ""
    echo -e "${GREEN}Services restarted!${NC}"
    echo ""
}

# ─── Logs ─────────────────────────────────────────────────────────────────────
show_logs() {
    if command -v pm2 &>/dev/null; then
        echo -e "${YELLOW}Recent PM2 Logs:${NC}"
        echo ""
        echo -e "${BLUE}=== Backend (paper-backend) ===${NC}"
        pm2 logs paper-backend  --lines 20 --nostream 2>/dev/null || cat "$LOGS_DIR/backend-out.log" 2>/dev/null | tail -20
        echo ""
        echo -e "${BLUE}=== Frontend (paper-frontend) ===${NC}"
        pm2 logs paper-frontend --lines 20 --nostream 2>/dev/null || cat "$LOGS_DIR/frontend-out.log" 2>/dev/null | tail -20
    else
        echo -e "${RED}pm2 not found${NC}"
    fi
    echo ""
}

# ─── Install ──────────────────────────────────────────────────────────────────
install_deps() {
    echo -e "${YELLOW}Installing Dependencies...${NC}"
    echo ""

    echo -e "   Installing frontend npm packages..."
    cd "$FRONTEND_DIR"
    npm install
    [ $? -eq 0 ] && echo -e "   ${GREEN}OK${NC} - Frontend deps installed" || echo -e "   ${RED}ERROR${NC} - Frontend deps failed"

    echo -e "   Installing backend pip packages..."
    cd "$BACKEND_DIR"
    python3 -m pip install -r requirements.txt
    [ $? -eq 0 ] && echo -e "   ${GREEN}OK${NC} - Backend deps installed" || echo -e "   ${RED}ERROR${NC} - Backend deps failed"

    if ! command -v pm2 &>/dev/null; then
        echo -e "   Installing PM2 globally..."
        npm install -g pm2
        [ $? -eq 0 ] && echo -e "   ${GREEN}OK${NC} - pm2 installed" || echo -e "   ${RED}ERROR${NC} - pm2 install failed"
    else
        echo -e "   ${GREEN}OK${NC} - PM2 already installed ($(pm2 -v))"
    fi

    echo ""
    echo -e "${GREEN}Dependencies installed!${NC}"
    echo ""
}

# ─── Setup Nginx ──────────────────────────────────────────────────────────────
setup_nginx() {
    require_root
    echo -e "${YELLOW}Setting up Nginx for $DOMAIN...${NC}"
    echo ""

    if ! command -v nginx &>/dev/null; then
        echo -e "   Installing nginx..."
        apt-get update -qq && apt-get install -y nginx
    fi

    mkdir -p /var/www/certbot

    if [ ! -f "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" ]; then
        echo -e "   ${YELLOW}NOTE${NC} - No SSL cert yet. Deploying HTTP-only config for Certbot challenge."
        cat > "$NGINX_SITES/$DOMAIN" <<HTTPONLY
server {
    listen 80;
    listen [::]:80;
    server_name paperfull.app www.paperfull.app;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location /api/ {
        proxy_pass         http://127.0.0.1:$BACKEND_PORT;
        proxy_set_header   Host \$host;
        proxy_set_header   X-Real-IP \$remote_addr;
        proxy_buffering    off;
        proxy_read_timeout 600s;
        client_max_body_size 50M;
    }

    location / {
        proxy_pass       http://127.0.0.1:$FRONTEND_PORT;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
HTTPONLY
    else
        cp "$NGINX_CONF" "$NGINX_SITES/$DOMAIN"
    fi

    ln -sf "$NGINX_SITES/$DOMAIN" "$NGINX_ENABLED/$DOMAIN"
    rm -f "$NGINX_ENABLED/default"

    nginx -t && systemctl reload nginx
    if [ $? -eq 0 ]; then
        echo -e "   ${GREEN}OK${NC} - Nginx configured and reloaded"
        echo -e "   ${CYAN}Next:${NC} Run 'sudo $0 setup-ssl' to get the SSL certificate"
    else
        echo -e "   ${RED}ERROR${NC} - Nginx config test failed"
        exit 1
    fi
    echo ""
}

# ─── Setup SSL (Certbot) ──────────────────────────────────────────────────────
setup_ssl() {
    require_root
    echo -e "${YELLOW}Setting up SSL with Certbot for $DOMAIN...${NC}"
    echo ""

    if ! command -v certbot &>/dev/null; then
        echo -e "   Installing certbot..."
        apt-get update -qq
        apt-get install -y certbot python3-certbot-nginx
    fi

    certbot --nginx -d "$DOMAIN" -d "www.$DOMAIN" --non-interactive --agree-tos --redirect \
        -m "admin@paperfull.app" --keep-until-expiring

    if [ $? -eq 0 ]; then
        cp "$NGINX_CONF" "$NGINX_SITES/$DOMAIN"
        nginx -t && systemctl reload nginx
        echo ""
        echo -e "   ${GREEN}OK${NC} - SSL certificate issued and nginx reloaded"
        echo -e "   ${GREEN}OK${NC} - Auto-renewal configured via certbot timer"
        echo ""
        echo -e "${CYAN}Site is live at: https://$DOMAIN${NC}"
    else
        echo -e "   ${RED}ERROR${NC} - Certbot failed. Ensure DNS points to this server and port 80 is open."
    fi
    echo ""
}

# ─── PM2 Startup ─────────────────────────────────────────────────────────────
setup_startup() {
    echo -e "${YELLOW}Configuring PM2 startup on boot...${NC}"
    echo ""

    PM2_BIN=$(find_pm2)
    if [ -z "$PM2_BIN" ]; then
        echo -e "   ${RED}ERROR${NC} - pm2 not found. Install with: npm install -g pm2"
        exit 1
    fi

    STARTUP_CMD=$("$PM2_BIN" startup 2>&1 | grep -E "^sudo |^env " | tail -1)
    if [ -n "$STARTUP_CMD" ]; then
        echo -e "   ${GRAY}Running: $STARTUP_CMD${NC}"
        eval "$STARTUP_CMD"
    fi

    if [[ $EUID -eq 0 ]]; then
        su - ubuntu -c "'$PM2_BIN' save" 2>/dev/null || "$PM2_BIN" save
    else
        "$PM2_BIN" save
    fi

    echo -e "   ${GREEN}OK${NC} - PM2 will auto-start on reboot"
    echo ""
}

# ─── Help ─────────────────────────────────────────────────────────────────────
show_help() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  start         - Build frontend then start via PM2"
    echo "  stop          - Stop all PM2 apps"
    echo "  restart       - Rebuild frontend then restart PM2 apps"
    echo "  status        - Check full service status"
    echo "  logs          - Show PM2 logs"
    echo "  install       - Install npm + pip + pm2 dependencies"
    echo "  build         - Build Vite frontend only"
    echo "  setup-nginx   - Install & configure nginx  (requires sudo)"
    echo "  setup-ssl     - Obtain Certbot SSL cert    (requires sudo)"
    echo "  setup-startup - Configure PM2 to auto-start on reboot"
    echo "  help          - Show this help"
    echo ""
    echo "Ports:"
    echo "  $FRONTEND_PORT  - Frontend (Vite preview / npm start)"
    echo "  $BACKEND_PORT  - Backend  (Flask API)"
    echo ""
    echo "Domain: https://$DOMAIN"
    echo ""
}

# ─── Interactive Menu ─────────────────────────────────────────────────────────
show_menu() {
    echo "Select an option:"
    echo "  1)  Start services"
    echo "  2)  Stop services"
    echo "  3)  Restart services"
    echo "  4)  Check status"
    echo "  5)  Show logs"
    echo "  6)  Install dependencies"
    echo "  7)  Build frontend"
    echo "  8)  Setup nginx   (sudo)"
    echo "  9)  Setup SSL     (sudo)"
    echo " 10)  Setup PM2 startup"
    echo " 11)  Exit"
    echo ""
    read -rp "Enter choice [1-11]: " choice
    case $choice in
        1)  start_services ;;
        2)  stop_services ;;
        3)  restart_services ;;
        4)  check_status ;;
        5)  show_logs ;;
        6)  install_deps ;;
        7)  build_frontend ;;
        8)  setup_nginx ;;
        9)  setup_ssl ;;
        10) setup_startup ;;
        11) exit 0 ;;
        *)  echo -e "${RED}Invalid choice${NC}" ;;
    esac
}

# ─── Main ─────────────────────────────────────────────────────────────────────
print_header

case "$1" in
    start)          start_services ;;
    stop)           stop_services ;;
    restart)        restart_services ;;
    status)         check_status ;;
    logs)           show_logs ;;
    install)        install_deps ;;
    build)          build_frontend ;;
    setup-nginx)    setup_nginx ;;
    setup-ssl)      setup_ssl ;;
    setup-startup)  setup_startup ;;
    help|--help|-h) show_help ;;
    "")             show_menu ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        echo ""
        show_help
        ;;
esac
