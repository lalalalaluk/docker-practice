# Practice 5 解答與解題思路

現象：某個 service 不能從主機直接連，但主要入口仍可呼叫 API。

解題思路：

1. 先看哪些 service 有對外 port：

   ```powershell
   docker compose ps
   ```

2. 從主機測兩個入口：

   ```powershell
   curl -i http://localhost:5000/api/health
   curl -i http://localhost:8080/api/health
   curl -i http://localhost:8080/api/products
   ```

3. 如果 `localhost:5000` 不能連，但 `localhost:8080/api/...` 可以，代表 backend 沒有對外暴露，但 frontend/Nginx 仍可在 Compose network 內呼叫 backend。

開發時如果要直接連 backend：

```powershell
docker compose -f compose.yaml -f compose.dev.yml up -d --build
curl -i http://localhost:5000/api/health
```

檢查 `compose.yaml`：

```yaml
frontend:
  ports:
    - "8080:80"

backend:
  # 不需要 ports
```

原因：正式部署通常只暴露入口層。backend 和 db 留在內部 network。

`compose.dev.yml` 只給本機除錯用。
