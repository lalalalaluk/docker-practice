# P3 - 自動 Build 並 Push Docker Image

目標：測試通過後，自動 build Docker Image 並 push 到 Docker Hub。

## GitHub Secrets

在 GitHub Repository 設定：

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

路徑：

```text
Repository -> Settings -> Secrets and variables -> Actions
```

## 本機測試

```powershell
pip install -r requirements.txt
pytest test_app.py -v

docker build -t docker-cicd-demo .
docker run --rm docker-cicd-demo
```

## Push 後觀察

```powershell
git add .
git commit -m "add Docker build workflow"
git push
```

Actions 順序：

```text
test -> docker
```

`docker` job 有 `needs: test`，所以測試失敗時不會 build/push。
