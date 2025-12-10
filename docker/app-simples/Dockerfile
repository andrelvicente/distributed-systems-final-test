# ============================================
# Dockerfile - Instruções para construir uma imagem Docker
# ============================================
# Este arquivo contém todas as instruções necessárias
# para criar uma imagem que contém nossa aplicação

# ETAPA 1: Escolher a imagem base
# Usamos uma imagem Python oficial (versão leve)
# Isso já vem com Python instalado, não precisamos instalar manualmente
FROM python:3.11-slim

# ETAPA 2: Criar e definir o diretório de trabalho
# Todas as operações seguintes acontecerão dentro desta pasta
WORKDIR /app

# ETAPA 3: Copiar o arquivo de dependências
# Primeiro copiamos só o requirements.txt (otimização: se mudar só o código,
# não precisa reinstalar as dependências)
COPY requirements.txt .

# ETAPA 4: Instalar as dependências Python
# Instala todas as bibliotecas listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ETAPA 5: Copiar o código da aplicação
# Agora copiamos o arquivo Python da nossa aplicação
COPY app.py .

# ETAPA 6: Informar qual porta a aplicação usa
# Isso é apenas documentação, não expõe a porta automaticamente
EXPOSE 5000

# ETAPA 7: Comando que será executado quando o container iniciar
# Quando alguém rodar "docker run", este comando será executado
CMD ["python", "app.py"]

