# Practice 2

這題需要先跑過一次，再修改範例資料，才能重現問題。

## 重現

先啟動原本專案：

```powershell
copy .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/products
```

接著在範例資料裡新增一筆商品，只重新執行：

```powershell
docker compose up -d --build
curl http://localhost:8080/api/products
```

## 現象

API 回傳結果仍然沒有新增的商品。

## 任務

回答這四件事：

1. 哪個 service 或 Docker 資源讓資料維持舊狀態？
2. 第一個能證明資料沒有更新的地方是什麼？
3. 要改程式碼，還是要處理 Docker 資源？
4. 修完後用哪個指令驗證？

## 建議指令

```powershell
docker compose ps
docker compose exec db mysql -u product_user -p product_app
curl http://localhost:8080/api/products
```
