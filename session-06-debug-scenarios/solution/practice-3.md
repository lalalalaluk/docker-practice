# Practice 3 解答與解題思路

現象：首頁正常，但 `/api/products` 失敗。

解題思路：

1. 先確認 frontend 是否有 proxy 錯誤：

   ```powershell
   docker compose logs frontend
   ```

2. 再看 backend 是否有收到請求或報錯：

   ```powershell
   docker compose logs backend
   ```

3. 如果 frontend logs 出現 upstream、host not found、connection failed，檢查 `frontend/nginx.conf`。

修改 `frontend/nginx.conf`：

```nginx
proxy_pass http://backend:5000/api/;
```

如果檔案使用變數，也要確認變數值是：

```nginx
set $backend_upstream backend:5000;
```

原因：Nginx 跑在 frontend container 裡，要用 Compose service name `backend` 找 Flask API。

驗證：

```powershell
docker compose up -d --build frontend
curl -i http://localhost:8080/api/products
```
