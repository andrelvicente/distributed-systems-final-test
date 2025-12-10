# Hands-on: Kubernetes ☸️

Este diretório contém exemplos práticos para aprender Kubernetes do zero.

## 📚 O que é Kubernetes?

Kubernetes (K8s) é uma plataforma de orquestração de containers open-source que automatiza o deploy, escalonamento e gerenciamento de aplicações containerizadas.

## 🎯 Conceitos Fundamentais

- **Pod**: Menor unidade de deploy no Kubernetes (pode conter um ou mais containers)
- **Deployment**: Gerencia réplicas de Pods e garante que o número desejado esteja rodando
- **Service**: Expõe Pods para comunicação interna ou externa
- **ConfigMap**: Armazena dados de configuração não sensíveis
- **Namespace**: Isolamento lógico de recursos no cluster

## 🚀 Como usar este hands-on

### Pré-requisitos
- Kubernetes instalado (Minikube, Kind, ou cluster local)
- kubectl instalado ([Instruções de instalação](https://kubernetes.io/docs/tasks/tools/))

### Passo 1: Deploy Básico (Primeiro Contato)

Este é o exemplo mais básico. Vamos fazer nosso primeiro deploy no Kubernetes!

#### O que vamos fazer?
1. Criar um namespace (área isolada)
2. Fazer deploy de uma aplicação (Deployment)
3. Expor a aplicação (Service)
4. Acessar a aplicação

#### Passo a passo:

1. **Criar um namespace (área de trabalho isolada):**
   ```bash
   kubectl create namespace hands-on
   ```
   **O que é um namespace?**
   - É como uma "pasta" que organiza seus recursos
   - Evita conflitos de nomes
   - Facilita gerenciamento

2. **Verificar se o namespace foi criado:**
   ```bash
   kubectl get namespaces
   ```
   Você deve ver `hands-on` na lista!

3. **Navegar até a pasta do exemplo:**
   ```bash
   cd k8s/deploy-basico
   ```

4. **Ver o arquivo deployment.yaml:**
   ```bash
   cat deployment.yaml
   ```
   Leia os comentários para entender o que cada parte faz!

5. **Aplicar o deployment (criar a aplicação):**
   ```bash
   kubectl apply -f deployment.yaml
   ```
   **O que isso faz?**
   - Lê o arquivo YAML
   - Cria um Deployment no Kubernetes
   - O Kubernetes vai criar Pods (containers) automaticamente

6. **Verificar se os Pods foram criados:**
   ```bash
   kubectl get pods -n hands-on
   ```
   Você deve ver um Pod com status `Running` ou `ContainerCreating`
   
   **Aguardar até ficar `Running`:**
   ```bash
   kubectl get pods -n hands-on -w
   ```
   Pressione `Ctrl+C` quando o Pod estiver `Running`

7. **Aplicar o service (expor a aplicação):**
   ```bash
   kubectl apply -f service.yaml
   ```
   **O que é um Service?**
   - É como um "endereço fixo" para acessar os Pods
   - Mesmo que os Pods sejam recriados, o Service mantém o mesmo endereço

8. **Verificar o service:**
   ```bash
   kubectl get services -n hands-on
   ```
   Você deve ver `app-service` na lista!

9. **Acessar a aplicação (port-forward):**
   ```bash
   kubectl port-forward -n hands-on service/app-service 8080:80
   ```
   **O que isso faz?**
   - Cria um "túnel" do seu computador para o Service
   - Agora você pode acessar no navegador
   
   **Acesse no navegador:** http://localhost:8080
   
   ⚠️ Deixe este terminal aberto! Quando fechar, o acesso para.

10. **Ver informações detalhadas do Pod:**
    ```bash
    kubectl describe pod <nome-do-pod> -n hands-on
    ```
    Substitua `<nome-do-pod>` pelo nome real que você viu no `kubectl get pods`

### Passo 2: ConfigMap e Variáveis de Ambiente

Agora vamos aprender a usar ConfigMaps para guardar configurações!

#### O que vamos fazer?
- Criar um ConfigMap (arquivo de configuração)
- Usar essas configurações dentro dos Pods
- Ver como as variáveis de ambiente funcionam

#### Passo a passo:

1. **Navegar até a pasta do exemplo:**
   ```bash
   cd k8s/configmap-exemplo
   ```

2. **Ver o arquivo configmap.yaml:**
   ```bash
   cat configmap.yaml
   ```
   Veja como guardamos configurações em formato chave-valor!

3. **Criar o ConfigMap:**
   ```bash
   kubectl apply -f configmap.yaml
   ```

4. **Verificar se o ConfigMap foi criado:**
   ```bash
   kubectl get configmaps -n hands-on
   ```
   Você deve ver `app-config` na lista!

5. **Ver o conteúdo do ConfigMap:**
   ```bash
   kubectl describe configmap app-config -n hands-on
   ```
   Ou de forma mais simples:
   ```bash
   kubectl get configmap app-config -n hands-on -o yaml
   ```

6. **Aplicar o deployment que usa o ConfigMap:**
   ```bash
   kubectl apply -f deployment-with-configmap.yaml
   ```

7. **Aguardar o Pod ficar pronto:**
   ```bash
   kubectl get pods -n hands-on
   ```
   Procure pelo Pod com nome `app-with-configmap-...`

8. **Ver as variáveis de ambiente dentro do Pod:**
   ```bash
   # Primeiro, pegue o nome do Pod
   kubectl get pods -n hands-on
   
   # Depois, veja as variáveis (substitua <pod-name> pelo nome real)
   kubectl exec -n hands-on <pod-name> -- env | grep APP_
   ```
   
   Você deve ver:
   - `APP_NAME=Minha Aplicação Kubernetes`
   - `APP_ENV=production`
   - `LOG_LEVEL=info`

9. **Ver os logs do Pod (ele mostra as variáveis):**
   ```bash
   kubectl logs <pod-name> -n hands-on
   ```
   Você deve ver as variáveis sendo exibidas!

### Passo 3: Escalonamento (Aumentar/Diminuir Réplicas)

Agora vamos aprender a escalar nossa aplicação (criar mais cópias)!

#### O que vamos fazer?
- Aumentar o número de Pods rodando
- Ver como o Kubernetes gerencia múltiplas réplicas
- Entender o conceito de escalonamento

#### Passo a passo:

1. **Ver quantos Pods estão rodando atualmente:**
   ```bash
   kubectl get pods -n hands-on
   ```
   Você deve ver 1 Pod do `app-deployment`

2. **Aumentar para 3 réplicas (3 Pods):**
   ```bash
   kubectl scale deployment app-deployment --replicas=3 -n hands-on
   ```
   **O que isso faz?**
   - Diz ao Kubernetes: "Quero 3 cópias da minha aplicação"
   - O Kubernetes cria 2 Pods adicionais automaticamente

3. **Verificar as réplicas sendo criadas:**
   ```bash
   kubectl get pods -n hands-on -w
   ```
   Você verá os novos Pods sendo criados em tempo real!
   Pressione `Ctrl+C` quando terminar

4. **Ver todos os Pods:**
   ```bash
   kubectl get pods -n hands-on
   ```
   Agora você deve ver 3 Pods do `app-deployment`!

5. **Ver informações do Deployment:**
   ```bash
   kubectl get deployment app-deployment -n hands-on
   ```
   Veja que mostra `3/3` (3 desejados, 3 rodando)

6. **Ver logs de um Pod específico:**
   ```bash
   # Pegue o nome de um Pod
   kubectl get pods -n hands-on
   
   # Veja os logs (substitua <pod-name> pelo nome real)
   kubectl logs <pod-name> -n hands-on
   ```

7. **Diminuir para 1 réplica novamente:**
   ```bash
   kubectl scale deployment app-deployment --replicas=1 -n hands-on
   ```

8. **Ver os Pods sendo removidos:**
   ```bash
   kubectl get pods -n hands-on -w
   ```
   O Kubernetes remove os Pods extras automaticamente!

## 📁 Estrutura dos Exemplos

- `deploy-basico/` - Deployment e Service básicos (comece aqui!)
- `configmap-exemplo/` - Uso de ConfigMap para configuração

## 🔍 Comandos Úteis (Referência Rápida)

### Comandos Básicos de Consulta

```bash
# Listar Pods
kubectl get pods
kubectl get pods -n hands-on  # em um namespace específico

# Listar Services
kubectl get services
kubectl get svc  # forma abreviada

# Listar Deployments
kubectl get deployments
kubectl get deploy  # forma abreviada

# Listar ConfigMaps
kubectl get configmaps
kubectl get cm  # forma abreviada

# Listar tudo de uma vez
kubectl get all -n hands-on
```

### Ver Informações Detalhadas

```bash
# Descrever um Pod (ver todas as informações)
kubectl describe pod <pod-name> -n hands-on

# Descrever um Service
kubectl describe service <service-name> -n hands-on

# Descrever um Deployment
kubectl describe deployment <deployment-name> -n hands-on

# Ver o YAML de um recurso
kubectl get pod <pod-name> -n hands-on -o yaml
```

### Trabalhar com Logs

```bash
# Ver logs de um Pod
kubectl logs <pod-name> -n hands-on

# Ver logs em tempo real (seguir logs)
kubectl logs -f <pod-name> -n hands-on

# Ver logs de todos os Pods de um Deployment
kubectl logs -l app=minha-app -n hands-on
```

### Executar Comandos Dentro de Pods

```bash
# Entrar dentro de um Pod (como um terminal)
kubectl exec -it <pod-name> -n hands-on -- /bin/bash

# Executar um comando específico
kubectl exec <pod-name> -n hands-on -- ls /app

# Ver variáveis de ambiente
kubectl exec <pod-name> -n hands-on -- env
```

### Gerenciar Recursos

```bash
# Aplicar um arquivo YAML
kubectl apply -f arquivo.yaml

# Aplicar todos os arquivos de um diretório
kubectl apply -f <diretorio>/

# Deletar um recurso
kubectl delete deployment <deployment-name> -n hands-on
kubectl delete service <service-name> -n hands-on
kubectl delete configmap <configmap-name> -n hands-on

# Deletar tudo de um namespace (cuidado!)
kubectl delete namespace hands-on
```

### Escalonamento

```bash
# Aumentar/diminuir réplicas
kubectl scale deployment <deployment-name> --replicas=3 -n hands-on

# Ver status do escalonamento
kubectl get deployment <deployment-name> -n hands-on
```

### Acessar Aplicações

```bash
# Port-forward (criar túnel para acessar localmente)
kubectl port-forward -n hands-on service/<service-name> 8080:80

# Port-forward direto para um Pod
kubectl port-forward -n hands-on pod/<pod-name> 8080:80
```

## 🎓 Conceitos Avançados (para exploração futura)

- **HPA (Horizontal Pod Autoscaler)**: Escalonamento automático baseado em métricas
- **Ingress**: Roteamento de tráfego HTTP/HTTPS
- **Secrets**: Armazenamento de dados sensíveis
- **StatefulSets**: Para aplicações com estado
- **DaemonSets**: Para executar um pod em cada nó

