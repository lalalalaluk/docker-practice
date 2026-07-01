# Product List Fullstack Docker Starter

這是 Docker 第 6 堂的學生練習版。

React、Flask、測試、前端樣式和 package/requirements 已經先放好。課堂時間請專注在 Docker 相關檔案：

- `backend/Dockerfile`
- `backend/.dockerignore`
- `frontend/Dockerfile`
- `frontend/.dockerignore`
- `frontend/nginx.conf`
- `compose.yaml`

`.github/workflows/cicd.yml` 已提供簡化版範本。這堂課的 CI 只做測試與 image build 檢查，不 push Docker Hub，也不在 CI 裡啟動整套 Compose。

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
  ├── .github/
  │   └── workflows/
  │       └── cicd.yml
  ├── frontend/
  │   ├── package.json
  │   ├── package-lock.json
  │   ├── index.html
  │   └── src/
  ├── backend/
  │   ├── app.py
  │   ├── requirements.txt
  │   └── test_app.py
```

範例商品資料已經放在 backend 程式裡。本章先專心練 Docker Compose 怎麼把三個服務接起來。

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
3. build backend image，確認 `backend/Dockerfile` 沒問題
4. build frontend image，確認 `frontend/Dockerfile` 沒問題

完整的 Compose 串接檢查先留在本機執行：

```powershell
cp .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```
