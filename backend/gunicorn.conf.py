"""
Gunicorn production configuration
Server: 2 CPU cores, 7.6GB RAM
Target: 500 concurrent users
Strategy: sync workers with threading (compatible with Flask + SQLAlchemy)
  gevent has pre-fork incompatibilities with SQLAlchemy connection pool
  - 4 workers × 4 threads = 16 real concurrent requests
  - nginx keepalive + gunicorn backlog handles burst to 500
"""

import multiprocessing
import os

# ── Workers ──────────────────────────────────────────────────────────────────
# gthread: sync worker with threads (safe with SQLAlchemy connection pooling)
worker_class = "gthread"
workers = multiprocessing.cpu_count() * 2 + 1  # = 5 on 2-core machine
threads = 8              # 8 threads per worker = 40 total concurrent requests
                         # Each thread handles one request; OS schedules I/O

# ── Timeouts ─────────────────────────────────────────────────────────────────
timeout = 120             # AI generation can take up to 60s, give 120s headroom
graceful_timeout = 30     # give in-flight requests 30s to finish during reload
keepalive = 5             # keep connection alive 5s between requests (nginx upstream)

# ── Binding ──────────────────────────────────────────────────────────────────
bind = "127.0.0.1:1001"
backlog = 2048            # OS-level queue for unaccepted connections

# ── Security ─────────────────────────────────────────────────────────────────
limit_request_line = 8190
limit_request_fields = 100
limit_request_field_size = 8190

# ── Process naming ───────────────────────────────────────────────────────────
proc_name = "paper-generator-api"
default_proc_name = "paper-generator-api"

# ── Logging ──────────────────────────────────────────────────────────────────
accesslog = "/home/ubuntu/papergenerator/logs/gunicorn-access.log"
errorlog  = "/home/ubuntu/papergenerator/logs/gunicorn-error.log"
loglevel  = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)sµs'

# ── Performance ──────────────────────────────────────────────────────────────
# NOTE: preload_app disabled — causes issues with gevent/thread workers + SQLAlchemy
preload_app = False
max_requests = 5000       # recycle worker after 5000 requests (prevent memory leaks)
max_requests_jitter = 500 # stagger recycling so not all workers restart at once

# ── Worker tmp heartbeat dir ─────────────────────────────────────────────────
worker_tmp_dir = "/dev/shm"  # use RAM for heartbeat files (faster than disk)
