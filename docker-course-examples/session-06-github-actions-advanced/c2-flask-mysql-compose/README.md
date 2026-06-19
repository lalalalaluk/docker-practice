# C2 - Flask + MySQL + Compose Capstone

目標：建立 Flask + MySQL 專案，使用 Docker Compose 在本機啟動，並搭配 GitHub Actions 跑測試與 build image。

## starter

`starter/` 提供 Flask app、Dockerfile、Compose 與 `.env.example`，請自行補測試與 workflow。

## solution

`solution/` 提供完整參考解法。

## 本機啟動

```powershell
cd solution
copy .env.example .env
docker compose up -d --build
curl http://localhost:5000/health
curl http://localhost:5000/products
docker compose down -v
```

## CI/CD

`solution/.github/workflows/cicd.yml` 會：

1. 安裝 Python 依賴
2. 執行 pytest
3. build Docker Image
4. push 到 Docker Hub
