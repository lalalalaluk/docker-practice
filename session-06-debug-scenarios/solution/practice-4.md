# Practice 4 解答與解題思路

現象：修改前端原始碼後，瀏覽器仍然看到舊畫面。

解題思路：

1. 先確認 container 正常跑，不一定會有 error：

   ```powershell
   docker compose ps
   docker compose logs frontend
   ```

2. 回想 frontend production 流程：React 原始碼先 build 成 `dist/`，再被包進 Nginx image。

3. 如果只執行 `docker compose up -d`，Compose 可能只重啟舊 image，不會重新 build。

解法：

```powershell
docker compose up -d --build frontend
```

或：

```powershell
docker compose build frontend
docker compose up -d frontend
```

驗證：重新整理 `http://localhost:8080`。
