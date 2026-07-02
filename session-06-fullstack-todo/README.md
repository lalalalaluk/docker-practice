# Session 06 - Product List

Docker 第 6 堂範例。

```text
starter/    學生練習
solution/   完整解答
```

## App

```text
Browser
  -> frontend: React + Nginx
  -> backend: Flask API
  -> db: MySQL
```

## Starter 要補

- `backend/Dockerfile`
- `backend/.dockerignore`
- `frontend/Dockerfile`
- `frontend/.dockerignore`
- `compose.yaml`

## Run Solution

```powershell
cd solution
cp .env.example .env
docker compose up -d --build
```

```powershell
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```

```powershell
docker compose down
docker compose down -v
```
