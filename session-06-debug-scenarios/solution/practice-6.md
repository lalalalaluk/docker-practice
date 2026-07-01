# Practice 6 解答與解題思路

現象：`/api/health` 正常，但 `/api/products` 失敗。

解題思路：

1. 先確認兩支 API 的差異：

   ```powershell
   curl http://localhost:8080/api/health
   curl -i http://localhost:8080/api/products
   ```

2. health 不查 DB，products 會查 DB，所以看 backend logs：

   ```powershell
   docker compose logs backend
   ```

3. 再進 DB container 看實際 schema：

   ```powershell
   docker compose exec db mysql -u product_user -p product_app
   ```

   ```sql
   SHOW TABLES;
   ```

修正方向：讓 `db/init.sql` 建立的 table 名稱和 backend SQL 查詢一致，例如都使用：

```sql
Product
```

本機練習驗證：

```powershell
docker compose down -v
docker compose up -d --build
curl http://localhost:8080/api/products
```

觀念：health check 只能代表部分狀態，不代表 DB schema、SQL query 和完整功能都正常。
