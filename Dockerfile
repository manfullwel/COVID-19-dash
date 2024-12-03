FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Healthcheck para verificar se a aplicação está rodando
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

EXPOSE ${PORT}

# Comando para iniciar a aplicação com a porta do Railway
CMD python -c "import os; port = int(os.getenv('PORT', '8080')); __import__('dashboard').app.run_server(host='0.0.0.0', port=port, debug=False)"
