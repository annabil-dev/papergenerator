#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# Google OAuth Quick Setup Script for PaperGenerator
# ─────────────────────────────────────────────────────────────────────────────
# Usage: bash setup-oauth.sh
# Or run directly: chmod +x setup-oauth.sh && ./setup-oauth.sh
# ─────────────────────────────────────────────────────────────────────────────

set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$DIR/.env"

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║        PaperGenerator — Google OAuth Setup                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Buka: https://console.cloud.google.com/apis/credentials"
echo ""
echo "Langkah:"
echo "  1. Klik [+ Create Credentials] → OAuth 2.0 Client ID"
echo "  2. Application type: Web Application"
echo "  3. Name: PaperGenerator (bebas)"
echo "  4. Authorized JavaScript origins:"
echo "       https://paper.otomasi.app"
echo "  5. Authorized redirect URIs:"
echo "       https://paper.otomasi.app/api/auth/google/callback"
echo "  6. Klik [Create] → Copy Client ID dan Client Secret"
echo ""

read -rp "Paste Google Client ID: " CLIENT_ID
read -rp "Paste Google Client Secret: " CLIENT_SECRET

if [[ -z "$CLIENT_ID" || -z "$CLIENT_SECRET" ]]; then
    echo "❌ Client ID atau Client Secret kosong. Batalkan."
    exit 1
fi

# Update .env
sed -i "s|^GOOGLE_CLIENT_ID=.*|GOOGLE_CLIENT_ID=$CLIENT_ID|" "$ENV_FILE"
sed -i "s|^GOOGLE_CLIENT_SECRET=.*|GOOGLE_CLIENT_SECRET=$CLIENT_SECRET|" "$ENV_FILE"

echo ""
echo "✅ .env diperbarui!"
echo ""
echo "Restart backend..."
cd "$DIR"
pm2 restart paper-backend --update-env

echo ""
echo "⏳ Tunggu 3 detik..."
sleep 3

echo ""
echo "Test koneksi OAuth..."
RESP=$(curl -s http://localhost:1001/api/auth/google/login -w "\n%{http_code}" -o /dev/null)
HTTP_CODE=$(echo "$RESP" | tail -1)

if [[ "$HTTP_CODE" == "302" ]]; then
    echo "✅ OAuth berhasil dikonfigurasi! (HTTP $HTTP_CODE — redirect ke Google)"
else
    echo "⚠️  HTTP $HTTP_CODE — cek log: pm2 logs paper-backend --lines 20"
fi

echo ""
echo "Website siap di: https://paper.otomasi.app"
echo "Login dengan Gmail: https://paper.otomasi.app/login"
