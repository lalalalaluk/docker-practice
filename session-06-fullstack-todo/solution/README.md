# Product List Fullstack Docker Solution

![CI](https://github.com/your-name/product-list/actions/workflows/cicd.yml/badge.svg)

這是 Docker 第 6 堂的完整解答。它把 React、Flask、MySQL 用 Docker Compose 串成一個簡單的全端商品清單系統。

前端只負責列出商品，不做新增、修改、刪除。課堂重點放在 Docker Compose、Nginx proxy、MySQL volume、環境變數，以及用 GitHub Actions 做簡單檢查。

如果是課堂練習，請先使用上一層的 `starter/`。這個資料夾可以用來對答案、示範完整流程，或課後提供給學生參考。

## Architecture

```text
Browser
  |
  v
frontend container
React build + Nginx
  |
  | /api proxy
  v
backend container
Flask API
  |
  v
db container
MySQL + product-db-data volume
```

## Run locally

```powershell
cp .env.example .env
docker compose up -d --build
```

Open:

```text
http://localhost:8080
```

Check APIs:

```powershell
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```

## Useful commands

```powershell
docker compose ps
docker compose logs frontend
docker compose logs backend
docker compose logs db
docker compose exec db mysql -u product_user -p product_app
docker compose down
docker compose down -v
```

## CI/CD

`.github/workflows/cicd.yml` 會：

1. 安裝 backend dependencies
2. 執行 pytest
3. build backend image，確認 `backend/Dockerfile` 沒問題
4. build frontend image，確認 `frontend/Dockerfile` 沒問題

這個 workflow 不會 push Docker Hub，也不會在 CI 裡啟動整套 Compose。完整串接檢查留在本機用 `docker compose up -d --build` 驗證。
