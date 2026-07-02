# Practice 3

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 現象

- 首頁可以開
- `/api/products` 失敗

## 先查

```powershell
docker compose logs frontend
docker compose logs backend
curl -i http://localhost:8080/api/products
```
