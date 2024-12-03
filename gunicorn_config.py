import os

# Configurações do Gunicorn
bind = f"0.0.0.0:{os.getenv('PORT', '8080')}"
workers = 1
threads = 8
timeout = 120
worker_class = 'gthread'
keepalive = 5
worker_connections = 1000
accesslog = '-'
errorlog = '-'
loglevel = 'info'
