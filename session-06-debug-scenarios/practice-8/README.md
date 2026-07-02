# Practice 8

這題是小功能修改。

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/products
```

## 需求

商品多一個「分類」欄位，API 和前端都要看得到。

## 驗證

```powershell
docker compose down -v
docker compose up -d --build
curl http://localhost:8080/api/products
```
