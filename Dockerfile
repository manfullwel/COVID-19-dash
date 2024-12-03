FROM python:3.9-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos de requisitos primeiro (para melhor cache de camadas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código
COPY . .

# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV DASH_DEBUG_MODE=false

# Expor a porta (apenas documentação)
EXPOSE 8080

# Comando para iniciar a aplicação
CMD gunicorn -c gunicorn_config.py wsgi:server
