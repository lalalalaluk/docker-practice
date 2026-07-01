# Product List Fullstack Docker Starter

這是 Docker 第 6 堂的學生練習版。

React、Flask、測試、前端樣式、package/requirements 和範例資料 SQL 已經先放好。課堂時間請專注在 Docker 相關檔案：

- `backend/Dockerfile`
- `backend/.dockerignore`
- `frontend/Dockerfile`
- `frontend/.dockerignore`
- `frontend/nginx.conf`
- `compose.yaml`
- `.github/workflows/cicd.yml`

## Target architecture

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

## Provided files

```text
starter/
  ├── .env.example
  ├── frontend/
  │   ├── package.json
  │   ├── package-lock.json
  │   ├── index.html
  │   └── src/
  ├── backend/
  │   ├── app.py
  │   ├── requirements.txt
  │   └── test_app.py
  └── db/
      └── init.sql
```

`db/init.sql` 是課堂範例資料，目的是讓本章可以專心練 Docker Compose。正式專案通常會用 migration 或部署流程管理 schema。

## Goal

完成 Docker 相關檔案後，這些指令應該可以成功：

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

Useful commands:

```powershell
docker compose ps
docker compose logs frontend
docker compose logs backend
docker compose logs db
docker compose exec db mysql -u product_user -p product_app
docker compose down
docker compose down -v
```

## CI/CD goal

完成 `.github/workflows/cicd.yml` 後，workflow 應該會：

1. 安裝 backend dependencies
2. 執行 pytest
3. 用 Docker Compose build 並啟動 frontend、backend、db
4. 透過 frontend proxy 檢查 `/api/health`
5. 檢查 `/api/products`
6. push 到 main 時，把 frontend/backend images 推到 Docker Hub
