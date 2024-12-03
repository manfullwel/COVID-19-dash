# Use Ubuntu como base
FROM ubuntu:22.04

# Evitar prompts durante a instalação
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Instalar Python e dependências
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip \
    python3.9-dev \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Criar links simbólicos para python3.9
RUN ln -s /usr/bin/python3.9 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip

WORKDIR /app

# Copiar e instalar requirements primeiro
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código
COPY . .

# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV DASH_DEBUG_MODE=false

# Expor a porta
EXPOSE 8080

# Comando para iniciar a aplicação
CMD gunicorn -c gunicorn_config.py wsgi:server
