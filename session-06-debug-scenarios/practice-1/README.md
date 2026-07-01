# Practice 1

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 現象

- `http://localhost:8080` 前端可以開
- `/api/health` 可能正常
- `/api/products` 失敗

## 任務

回答這四件事：

1. 哪個 service 或哪一段連線出問題？
2. 第一個有用的 error message 是什麼？
3. 要改哪個檔案？
4. 修完後用哪個指令驗證？

## 建議指令

```powershell
docker compose ps
docker compose logs backend
docker compose logs db
curl -i http://localhost:8080/api/products
```
