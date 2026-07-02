# Practice 7 解答與解題思路

現象：本機可以跑，但 GitHub Actions 失敗。

解題思路：

1. 先確認本機真的正常：

   ```powershell
   copy .env.example .env
   docker compose up -d --build
   curl http://localhost:8080/api/products
   docker compose down -v
   ```

2. 到 GitHub Actions 看失敗 job 和失敗 step，找第一個 error message。

3. 如果錯誤是找不到資料夾或找不到 requirements，通常是 working directory 或相對路徑錯。

修正 `.github/workflows/cicd.yml`：

```yaml
defaults:
  run:
    working-directory: backend
```

Docker build context 也使用根目錄下的資料夾：

```yaml
run: docker build -t product-backend:test ./backend
run: docker build -t product-frontend:test ./frontend
```

觀念：CI runner 的工作目錄可能和你本機操作的位置不同。
