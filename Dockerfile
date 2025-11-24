# 1. Escolhemos a imagem base
FROM python:3.9-slim

# 2. Atualiza e instala ferramentas básicas
# Adicionamos 'ca-certificates' e 'curl' para garantir downloads seguros
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    ca-certificates \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# 3. Instala o Google Chrome (MÉTODO NOVO: Download Direto)
# Baixa o instalador .deb oficial e instala direto
RUN apt-get update && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && rm -rf /var/lib/apt/lists/*

# 4. Cria a pasta de trabalho
WORKDIR /app

# 5. Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia seu código
COPY . .

# 7. Comando de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]