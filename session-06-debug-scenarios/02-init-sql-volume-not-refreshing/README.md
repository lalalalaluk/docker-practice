# 情境 2：改了 init.sql，商品資料卻沒有變

這題需要先跑過一次，再修改 `db/init.sql`，才能重現問題。

## 重現

先啟動原本專案：

```powershell
copy .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/products
```

接著修改 `db/init.sql`，在最後新增一筆商品，例如：

```sql
('筆記型電腦', 32900.00, 8)
```

只重新執行：

```powershell
docker compose up -d --build
curl http://localhost:8080/api/products
```

## 現象

新商品沒有出現在 API 回傳結果。

## 任務

回答這四件事：

1. 哪個 service 或 Docker 資源讓資料維持舊狀態？
2. 第一個能證明資料沒有更新的地方是什麼？
3. 要改程式碼，還是要處理 volume？
4. 修完後用哪個指令驗證？

## 建議指令

```powershell
docker compose ps
docker compose exec db mysql -u product_user -p product_app
curl http://localhost:8080/api/products
```
