# Practice 8

這題不是找現成 bug，而是練習一次完成一個小功能變更。

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/products
```

## 需求

讓商品資料多回傳一個分類欄位，前端表格也要顯示商品分類。

## 任務

請找出需要一起修改的資料庫、backend 和 frontend 檔案。

## 驗證

```powershell
docker compose down -v
docker compose up -d --build
curl http://localhost:8080/api/products
```
