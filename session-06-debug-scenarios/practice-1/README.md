# Practice 1

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 現象

- 前端可以開
- `/api/products` 失敗

## 先查

```powershell
docker compose logs backend
docker compose logs db
curl -i http://localhost:8080/api/products
```

找出問題後，修正並重新驗證。
