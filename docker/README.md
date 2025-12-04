# Hands-on: Docker 🐳

Este diretório contém exemplos práticos para aprender Docker do zero.

## 📚 O que é Docker?

Docker é uma plataforma de containerização que permite empacotar aplicações e suas dependências em containers isolados. Isso garante que a aplicação funcione da mesma forma em qualquer ambiente.

## 🎯 Conceitos Fundamentais

- **Container**: Ambiente isolado que contém uma aplicação e suas dependências
- **Imagem**: Template usado para criar containers
- **Dockerfile**: Arquivo de instruções para construir uma imagem
- **Docker Compose**: Ferramenta para orquestrar múltiplos containers

## 🚀 Como usar este hands-on

### Pré-requisitos
- Docker instalado ([Instruções de instalação](https://docs.docker.com/get-docker/))

### Passo 1: Aplicação Simples

Vamos começar com uma aplicação web simples em Python.

1. **Construir a imagem:**
   ```bash
   cd docker/app-simples
   docker build -t minha-app:latest .
   ```

2. **Executar o container:**
   ```bash
   docker run -d -p 5000:5000 --name minha-app-container minha-app:latest
   ```

3. **Acessar a aplicação:**
   Abra o navegador em: http://localhost:5000

4. **Ver logs:**
   ```bash
   docker logs minha-app-container
   ```

5. **Parar e remover:**
   ```bash
   docker stop minha-app-container
   docker rm minha-app-container
   ```

### Passo 2: Docker Compose

Aprenda a orquestrar múltiplos containers com Docker Compose.

1. **Iniciar os serviços:**
   ```bash
   cd docker/docker-compose-exemplo
   docker compose up -d
   ```

2. **Verificar os containers:**
   ```bash
   docker compose ps
   ```

3. **Ver logs:**
   ```bash
   docker compose logs -f
   ```

4. **Parar os serviços:**
   ```bash
   docker compose down
   ```

## 📁 Estrutura dos Exemplos

- `app-simples/` - Aplicação básica com Dockerfile
- `docker-compose-exemplo/` - Exemplo de orquestração com múltiplos containers

## 🔍 Comandos Úteis

```bash
# Listar imagens
docker images

# Listar containers (rodando)
docker ps

# Listar todos os containers
docker ps -a

# Entrar em um container
docker exec -it <container-name> /bin/bash

# Remover imagens não utilizadas
docker image prune -a

# Ver uso de recursos
docker stats
```

