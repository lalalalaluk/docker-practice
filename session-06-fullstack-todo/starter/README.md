# Product List Starter

## 要完成

- `backend/Dockerfile`
- `backend/.dockerignore`
- `frontend/Dockerfile`
- `frontend/.dockerignore`
- `compose.yaml`
- `compose.dev.yml`

`frontend/nginx.conf` 已提供。

## 啟動

```powershell
cp .env.example .env
docker compose up -d --build
```

## 檢查

```powershell
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```

瀏覽器打開：

```text
http://localhost:8080
```

## 開發版

```powershell
docker compose -f compose.yaml -f compose.dev.yml up -d --build
curl http://localhost:5000/api/health
```

## 常用

```powershell
docker compose ps
docker compose logs backend
docker compose logs frontend
docker compose logs db
docker compose down
```
