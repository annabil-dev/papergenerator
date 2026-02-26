module.exports = {
  apps: [
    {
      name: 'paper-backend',
      script: 'app.py',
      cwd: '/home/ubuntu/papergenerator/backend',
      interpreter: 'python3',
      env: {
        FLASK_PORT: '1001',
        FLASK_DEBUG: 'false'
      },
      watch: false,
      autorestart: true,
      max_restarts: 10,
      restart_delay: 3000,
      error_file: '/home/ubuntu/papergenerator/logs/backend-error.log',
      out_file: '/home/ubuntu/papergenerator/logs/backend-out.log',
      merge_logs: true,
      log_date_format: 'YYYY-MM-DD HH:mm:ss'
    },
    {
      name: 'paper-frontend',
      script: 'npx',
      args: 'vite preview --host 0.0.0.0 --port 1000',
      cwd: '/home/ubuntu/papergenerator/frontend',
      env: {
        NODE_ENV: 'production'
      },
      watch: false,
      autorestart: true,
      max_restarts: 10,
      restart_delay: 3000,
      error_file: '/home/ubuntu/papergenerator/logs/frontend-error.log',
      out_file: '/home/ubuntu/papergenerator/logs/frontend-out.log',
      merge_logs: true,
      log_date_format: 'YYYY-MM-DD HH:mm:ss'
    }
  ]
}
