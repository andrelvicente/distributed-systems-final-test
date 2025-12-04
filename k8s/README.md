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

### Passo 1: Deploy Básico

Aprenda a fazer deploy de uma aplicação simples.

1. **Criar o namespace:**
   ```bash
   kubectl create namespace hands-on
   ```

2. **Aplicar o deployment:**
   ```bash
   cd k8s/deploy-basico
   kubectl apply -f deployment.yaml
   ```

3. **Aplicar o service:**
   ```bash
   kubectl apply -f service.yaml
   ```

4. **Verificar o status:**
   ```bash
   kubectl get pods -n hands-on
   kubectl get services -n hands-on
   ```

5. **Acessar a aplicação:**
   ```bash
   # Port-forward para acessar localmente
   kubectl port-forward -n hands-on service/app-service 8080:80
   ```
   Acesse: http://localhost:8080

### Passo 2: ConfigMap e Variáveis de Ambiente

Aprenda a usar ConfigMaps para configuração.

1. **Aplicar o ConfigMap:**
   ```bash
   cd k8s/configmap-exemplo
   kubectl apply -f configmap.yaml
   ```

2. **Aplicar o deployment que usa o ConfigMap:**
   ```bash
   kubectl apply -f deployment-with-configmap.yaml
   ```

3. **Verificar as variáveis de ambiente:**
   ```bash
   kubectl exec -n hands-on <pod-name> -- env | grep APP_
   ```

### Passo 3: Escalonamento

Aprenda a escalar aplicações.

1. **Escalar manualmente:**
   ```bash
   kubectl scale deployment app-deployment --replicas=3 -n hands-on
   ```

2. **Verificar as réplicas:**
   ```bash
   kubectl get pods -n hands-on
   ```

3. **Ver logs de um pod específico:**
   ```bash
   kubectl logs <pod-name> -n hands-on
   ```

## 📁 Estrutura dos Exemplos

- `deploy-basico/` - Deployment e Service básicos
- `configmap-exemplo/` - Uso de ConfigMap para configuração
- `multi-container/` - Pod com múltiplos containers

## 🔍 Comandos Úteis

```bash
# Listar recursos
kubectl get pods
kubectl get services
kubectl get deployments

# Descrever um recurso
kubectl describe pod <pod-name>
kubectl describe service <service-name>

# Ver logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>  # seguir logs em tempo real

# Executar comando em um pod
kubectl exec -it <pod-name> -- /bin/bash

# Deletar recursos
kubectl delete deployment <deployment-name>
kubectl delete service <service-name>
kubectl delete namespace hands-on

# Aplicar todos os arquivos de um diretório
kubectl apply -f <diretorio>/
```

## 🎓 Conceitos Avançados (para exploração futura)

- **HPA (Horizontal Pod Autoscaler)**: Escalonamento automático baseado em métricas
- **Ingress**: Roteamento de tráfego HTTP/HTTPS
- **Secrets**: Armazenamento de dados sensíveis
- **StatefulSets**: Para aplicações com estado
- **DaemonSets**: Para executar um pod em cada nó

