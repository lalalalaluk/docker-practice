# Practice 1 解答與解題思路

現象：首頁可開，`/api/health` 可能正常，但 `/api/products` 失敗。

解題思路：

1. 先打 API：

   ```powershell
   curl -i http://localhost:8080/api/products
   ```

2. `/api/products` 是 backend 查 DB，所以看 backend logs：

   ```powershell
   docker compose logs backend
   ```

3. 如果看到 MySQL connection refused 或連線到錯誤 host，進 backend container 看環境變數：

   ```powershell
   docker compose exec backend python -c "import os; print(os.getenv('MYSQL_HOST'))"
   ```

修改 `compose.yaml`：

```yaml
MYSQL_HOST: db
```

原因：在 backend container 裡，`localhost` 是 backend 自己，不是 MySQL。跨 service 要用 Compose service name。

驗證：

```powershell
docker compose up -d --build
curl http://localhost:8080/api/products
```
