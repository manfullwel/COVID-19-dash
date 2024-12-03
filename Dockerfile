# Use Python como base
FROM python:3.9-slim

# Criar diretório de trabalho
WORKDIR /app

# Copiar e instalar requirements primeiro
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código
COPY . .

# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Comando para iniciar a aplicação com a porta do Railway
CMD python -c "import os; port = int(os.getenv('PORT', '8080')); __import__('dashboard').app.run_server(host='0.0.0.0', port=port, debug=False)"
