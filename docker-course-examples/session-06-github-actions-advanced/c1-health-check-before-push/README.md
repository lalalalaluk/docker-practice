# C1 - Push 前先做容器健康檢查

目標：在 CI 裡先 build Docker Image，跑起來測 `/health`，確認成功後才 push 到 Docker Hub。

請把 `.github/workflows/cicd-health-check.yml` 複製到你的 Flask 專案。

## 流程

```text
test -> build local image -> docker run -> curl /health -> push image
```

## 需要的 Secrets

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
