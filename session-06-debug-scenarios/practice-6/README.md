# Practice 6

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 現象

- `/api/health` 正常
- `/api/products` 失敗

## 先查

```powershell
curl http://localhost:8080/api/health
curl -i http://localhost:8080/api/products
docker compose logs backend
docker compose exec db mysql -u testuser -p testdb
```
