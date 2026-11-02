# AnimalCards Globe — Kubernetes 一键部署

自包含镜像（已打入 1000 张卡片 PNG/PDF），无需挂载宿主机目录。

## 前置条件

- 可用的 Kubernetes 集群（`kubectl` 已配置）
- Docker（或兼容的构建工具）用于构建镜像

## 一键部署

在**仓库根目录**执行：

```bash
# 1. 构建自包含镜像（约 1GB）
docker build -f webapp/Dockerfile.k8s -t animalcards-globe:k8s .

# 2. 若集群节点拿不到本机镜像，先推送到仓库，再改 deploy/k8s/kustomization.yaml 的 images
#    docker tag animalcards-globe:k8s ghcr.io/YOUR_ORG/animalcards-globe:k8s
#    docker push ghcr.io/YOUR_ORG/animalcards-globe:k8s
#
# 本地 kind / minikube 可直接加载：
#    kind load docker-image animalcards-globe:k8s
#    # 或: minikube image load animalcards-globe:k8s

# 3. 一键应用
kubectl apply -k webapp/deploy/k8s/

# 4. 等待就绪并本地访问
kubectl -n animalcards rollout status deploy/animalcards-globe
kubectl -n animalcards port-forward svc/animalcards-globe 8000:80
# 浏览器打开 http://127.0.0.1:8000
```

## 外网域名（Ingress）

编辑 `ingress.yaml`：设置 `host`、按需取消注释 `ingressClassName`，然后重新 `kubectl apply -k webapp/deploy/k8s/`。

## 卸载

```bash
kubectl delete -k webapp/deploy/k8s/
```

## 说明

- 与 `docker compose` 方案不同：K8s 镜像**内含** `动物/`、`植物/`、`真菌/`，更新卡片需重新构建并滚动发布镜像。
- 默认 1 副本、ClusterIP；资源请求约 256Mi 内存。
