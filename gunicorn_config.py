import os
import multiprocessing

# Configurações do Gunicorn
bind = f"0.0.0.0:{os.getenv('PORT', '8080')}"
workers = 1  # Para aplicações Dash, um worker é suficiente
threads = 4  # Reduzido para inicialização mais rápida
timeout = 60  # Reduzido para falhar mais rápido se necessário
worker_class = 'sync'  # Classe mais simples para inicialização rápida
preload_app = True  # Pré-carrega a aplicação
keepalive = 5
max_requests = 100
max_requests_jitter = 10
graceful_timeout = 30
accesslog = '-'
errorlog = '-'
loglevel = 'info'
