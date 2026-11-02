#!/usr/bin/env bash
# AnimalCards Globe — 一键构建镜像并部署到当前 kubectl 上下文
# 用法（仓库根目录）:
#   ./webapp/deploy/k8s/deploy.sh
#   IMAGE=ghcr.io/you/animalcards-globe:k8s ./webapp/deploy/k8s/deploy.sh
#   SKIP_BUILD=1 ./webapp/deploy/k8s/deploy.sh   # 只 apply，不构建
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
IMAGE="${IMAGE:-animalcards-globe:k8s}"
SKIP_BUILD="${SKIP_BUILD:-0}"

cd "$ROOT"

if [[ "$SKIP_BUILD" != "1" ]]; then
  echo "==> Building $IMAGE (self-contained, ~1GB)…"
  docker build -f webapp/Dockerfile.k8s -t "$IMAGE" .
fi

# 若 IMAGE 不是默认名，用 kustomize 覆盖
OVERLAY="$(mktemp -d)"
trap 'rm -rf "$OVERLAY"' EXIT
cp -a webapp/deploy/k8s/. "$OVERLAY/"
# 解析 registry/name:tag
name="${IMAGE%%:*}"
tag="${IMAGE##*:}"
if [[ "$name" == "$tag" ]]; then tag="latest"; fi
cat > "$OVERLAY/kustomization.yaml" <<EOF
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: animalcards
resources:
  - namespace.yaml
  - configmap.yaml
  - deployment.yaml
  - service.yaml
  - ingress.yaml
images:
  - name: animalcards-globe
    newName: ${name}
    newTag: ${tag}
EOF

echo "==> Applying manifests…"
kubectl apply -k "$OVERLAY"
kubectl -n animalcards rollout status deploy/animalcards-globe --timeout=180s

echo
echo "Done. Port-forward:"
echo "  kubectl -n animalcards port-forward svc/animalcards-globe 8000:80"
echo "Then open http://127.0.0.1:8000"
