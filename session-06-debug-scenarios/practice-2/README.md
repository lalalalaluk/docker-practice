# Practice 2

## 重現

```powershell
copy .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/products
```

修改範例資料後，再跑一次：

```powershell
docker compose up -d --build
curl http://localhost:8080/api/products
```

## 現象

資料沒有變。

## 先查

```powershell
docker compose ps
docker compose exec db mysql -u testuser -p testdb
curl http://localhost:8080/api/products
```
