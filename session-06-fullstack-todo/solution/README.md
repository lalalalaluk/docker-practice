# Product List Solution

完整解答。

```text
frontend  React + Nginx
backend   Flask API
db        MySQL + volume
```

## Run

```powershell
cp .env.example .env
docker compose up -d --build
```

```powershell
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```

## Dev Ports

```powershell
docker compose -f compose.yaml -f compose.dev.yml up -d --build
```

```text
backend  http://localhost:5000
mysql    localhost:3307
```

## 常用指令

```powershell
docker compose ps
docker compose logs frontend
docker compose logs backend
docker compose logs db
docker compose down
docker compose down -v
```

## CI

`.github/workflows/cicd.yml`：

- backend pytest
- build backend image
- build frontend image
