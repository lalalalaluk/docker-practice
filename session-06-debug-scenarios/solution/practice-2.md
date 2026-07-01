# Practice 2 解答與解題思路

現象：修改範例資料後重新啟動，API 回傳仍然沒有新資料。

解題思路：

1. 先確認 API 真的沒有新資料：

   ```powershell
   curl http://localhost:8080/api/products
   ```

2. 進 DB container 看資料表內容：

   ```powershell
   docker compose exec db mysql -u product_user -p product_app
   ```

   ```sql
   SELECT * FROM Product;
   ```

3. 如果 DB 裡也沒有新資料，代表不是 frontend 或 backend 顯示問題，而是 MySQL volume 沿用舊資料。

本機練習解法：

```powershell
docker compose down -v
docker compose up -d --build
curl http://localhost:8080/api/products
```

原因：`init.sql` 只會在 MySQL 資料目錄第一次初始化時執行。volume 已存在時，MySQL 會沿用舊資料，不會重跑初始化 SQL。

注意：`down -v` 會刪掉資料庫 volume，只適合課堂練習，不是正式資料庫更新方式。
