# Dockerfile - Instruções para construir a imagem
# Etapa 1: Definir a imagem base
FROM python:3.11-slim

# Etapa 2: Definir o diretório de trabalho dentro do container
WORKDIR /app

# Etapa 3: Copiar o arquivo de dependências
COPY requirements.txt .

# Etapa 4: Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: Copiar o código da aplicação
COPY app.py .

# Etapa 6: Expor a porta que a aplicação usa
EXPOSE 5000

# Etapa 7: Comando para executar quando o container iniciar
CMD ["python", "app.py"]

