# 情境 8：增加商品欄位，從 DB 到前端一路改

這題不是找現成 bug，而是練習完整變更路徑。

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/products
```

## 需求

在 `Product` table 增加 `Category` 欄位，並讓 `/api/products` 回傳：

```json
{
  "id": 1,
  "name": "藍牙耳機",
  "price": 1290,
  "stock": 50,
  "category": "3C"
}
```

前端表格也要顯示商品分類。

## 任務

請修改：

1. `db/init.sql`
2. `backend/app.py`
3. `frontend/src/App.jsx`
4. 視需要修改 `frontend/src/App.css`

## 驗證

```powershell
docker compose down -v
docker compose up -d --build
curl http://localhost:8080/api/products
```
