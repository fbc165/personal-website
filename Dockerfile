# Dockerfile
FROM python:3.12-slim

# Evitar .pyc e buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /code

# Instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . .

# Torna o entrypoint executável
RUN chmod +x ./entrypoint.sh

# Expõe a porta da app
EXPOSE 8000

