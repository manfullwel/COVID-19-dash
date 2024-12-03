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
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Expor a porta
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["python", "dashboard.py"]
