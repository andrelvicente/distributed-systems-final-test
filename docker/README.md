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
- Conhecimento básico de terminal/linha de comando

### Passo 1: Aplicação Simples (Primeiro Contato)

Este é o exemplo mais básico. Vamos criar e rodar nossa primeira aplicação em Docker!

#### O que vamos fazer?
1. Criar uma imagem Docker a partir de um Dockerfile
2. Rodar um container com essa imagem
3. Acessar a aplicação no navegador

#### Passo a passo:

1. **Navegar até a pasta do exemplo:**
   ```bash
   cd docker/app-simples
   ```

2. **Construir a imagem Docker:**
   ```bash
   docker build -t minha-app:latest .
   ```
   **O que isso faz?**
   - Lê o arquivo `Dockerfile`
   - Cria uma imagem chamada `minha-app` com a tag `latest`
   - O ponto (`.`) significa "diretório atual"
   - Isso pode levar alguns minutos na primeira vez

3. **Verificar se a imagem foi criada:**
   ```bash
   docker images
   ```
   Você deve ver `minha-app` na lista!

4. **Executar o container:**
   ```bash
   docker run -d -p 5000:5000 --name minha-app-container minha-app:latest
   ```
   **O que cada parte significa?**
   - `-d`: roda em background (detached)
   - `-p 5000:5000`: mapeia porta 5000 do host para porta 5000 do container
   - `--name`: dá um nome ao container
   - `minha-app:latest`: qual imagem usar

5. **Verificar se o container está rodando:**
   ```bash
   docker ps
   ```
   Você deve ver `minha-app-container` na lista!

6. **Acessar a aplicação:**
   Abra seu navegador e acesse: **http://localhost:5000**
   
   Você deve ver uma mensagem JSON dizendo que está rodando em Docker! 🎉

7. **Ver os logs (o que a aplicação está fazendo):**
   ```bash
   docker logs minha-app-container
   ```

8. **Parar o container:**
   ```bash
   docker stop minha-app-container
   ```

9. **Remover o container (limpar):**
   ```bash
   docker rm minha-app-container
   ```

### Passo 2: Docker Compose (Múltiplos Containers)

Agora vamos aprender a gerenciar vários containers trabalhando juntos!

#### O que vamos fazer?
- Rodar uma aplicação web E um banco de dados ao mesmo tempo
- Ver como eles se comunicam
- Entender o arquivo `docker-compose.yml`

#### Passo a passo:

1. **Navegar até a pasta do exemplo:**
   ```bash
   cd docker/docker-compose-exemplo
   ```

2. **Ver o arquivo docker-compose.yml:**
   ```bash
   cat docker-compose.yml
   ```
   Leia os comentários no arquivo para entender o que cada parte faz!

3. **Iniciar todos os serviços:**
   ```bash
   docker compose up -d
   ```
   **O que isso faz?**
   - Lê o arquivo `docker-compose.yml`
   - Cria e inicia TODOS os containers definidos
   - `-d` roda em background
   - Isso pode levar alguns minutos (baixa imagens, etc)

4. **Verificar os containers criados:**
   ```bash
   docker compose ps
   ```
   Você deve ver 2 containers: `app-web` e `app-db`

5. **Acessar a aplicação web:**
   Abra: **http://localhost:5000**

6. **Ver os logs de todos os serviços:**
   ```bash
   docker compose logs
   ```

7. **Ver logs de um serviço específico:**
   ```bash
   docker compose logs web    # Logs da aplicação web
   docker compose logs db      # Logs do banco de dados
   ```

8. **Parar todos os serviços:**
   ```bash
   docker compose down
   ```
   Isso para E remove os containers, mas mantém os volumes (dados do banco)

9. **Parar e remover TUDO (incluindo volumes):**
   ```bash
   docker compose down -v
   ```
   ⚠️ Cuidado: isso apaga os dados do banco de dados!

## 📁 Estrutura dos Exemplos

- `app-simples/` - Aplicação básica com Dockerfile
- `docker-compose-exemplo/` - Exemplo de orquestração com múltiplos containers

## 🔍 Comandos Úteis (Referência Rápida)

### Comandos Básicos

```bash
# Listar imagens Docker que você tem
docker images

# Listar containers que estão RODANDO
docker ps

# Listar TODOS os containers (rodando e parados)
docker ps -a

# Ver informações detalhadas de um container
docker inspect <container-name>

# Ver uso de recursos (CPU, memória) em tempo real
docker stats
```

### Gerenciamento de Containers

```bash
# Parar um container
docker stop <container-name>

# Iniciar um container parado
docker start <container-name>

# Reiniciar um container
docker restart <container-name>

# Remover um container (deve estar parado)
docker rm <container-name>

# Remover um container mesmo se estiver rodando (força)
docker rm -f <container-name>
```

### Trabalhando Dentro de Containers

```bash
# Entrar dentro de um container (como se fosse um terminal)
docker exec -it <container-name> /bin/bash

# Executar um comando dentro do container (sem entrar)
docker exec <container-name> ls /app

# Ver os logs de um container
docker logs <container-name>

# Ver logs em tempo real (seguir logs)
docker logs -f <container-name>
```

### Limpeza

```bash
# Remover containers parados
docker container prune

# Remover imagens não utilizadas
docker image prune

# Remover TUDO que não está sendo usado (cuidado!)
docker system prune -a
```

### Docker Compose

```bash
# Ver status dos serviços
docker compose ps

# Ver logs
docker compose logs

# Ver logs de um serviço específico
docker compose logs web

# Parar serviços
docker compose stop

# Iniciar serviços
docker compose start

# Recriar e reiniciar serviços
docker compose up -d --force-recreate
```

