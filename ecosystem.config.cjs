const fs = require('fs');
const path = require('path');

// Read .env file
let env = {};
try {
  const envFile = fs.readFileSync(path.join(__dirname, '.env'), 'utf8');
  envFile.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return;
    const eqIdx = trimmed.indexOf('=');
    if (eqIdx > 0) {
      env[trimmed.slice(0, eqIdx).trim()] = trimmed.slice(eqIdx + 1).trim();
    }
  });
} catch (e) { /* use defaults */ }

const BACKEND_PORT = env.BACKEND_PORT || '1001';
const FRONTEND_PORT = env.FRONTEND_PORT || '1000';

module.exports = {
  apps: [
    {
      // Gunicorn + gevent: 5 workers × 200 greenlets = handles 500+ concurrent users
      // Frontend is served directly by nginx (faster, no node process needed)
      name: 'paper-backend',
      script: path.join(__dirname, 'backend/start.sh'),
      cwd: path.join(__dirname, 'backend'),
      interpreter: '/bin/bash',
      env: {
        FLASK_PORT: BACKEND_PORT,
        FLASK_DEBUG: 'false',
      },
      log_file: path.join(__dirname, 'logs/backend.log'),
      out_file: path.join(__dirname, 'logs/backend-out.log'),
      error_file: path.join(__dirname, 'logs/backend-err.log'),
      max_memory_restart: '1500M',   // gunicorn with 5 workers uses more RAM
      restart_delay: 3000,
      max_restarts: 10,
      min_uptime: '10s',
    }
  ]
};
