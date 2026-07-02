# Practice 7

這題看 GitHub Actions。

## 本機先確認

```powershell
copy .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/products
docker compose down -v
```

## 現象

本機正常，CI 失敗。

## 先查

- 失敗的 job
- 失敗的 step
- 第一個 error message
- workflow 的路徑設定
