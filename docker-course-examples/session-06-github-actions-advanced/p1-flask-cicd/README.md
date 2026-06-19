# P1 - 完整 Flask CI/CD Pipeline

目標：建立 Flask API，push 後自動跑測試，測試通過才 build 並 push Docker Image。

## starter

`starter/` 有 Flask app、測試、Dockerfile 和 `.dockerignore`。請自己建立 workflow。

## solution

`solution/` 是完整解法，包含：

- Flask API
- pytest 測試
- Dockerfile
- `.dockerignore`
- `.github/workflows/cicd.yml`
- README badge 範例

## 本機測試

```powershell
pip install -r requirements.txt
pytest test_app.py -v

docker build -t docker-cicd-demo .
docker run -d --name cicd-test -p 5000:5000 docker-cicd-demo
curl http://localhost:5000/health
docker rm -f cicd-test
```

## GitHub Secrets

在 GitHub Repository 設定：

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
