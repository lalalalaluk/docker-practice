# 情境 1：backend 連不到 MySQL

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 現象

- `http://localhost:8080` 前端可以開
- `/api/health` 可能正常
- `/api/products` 失敗
- backend logs 會出現 MySQL connection error

## 任務

回答這四件事：

1. 哪個 service 壞了？
2. 第一個有用的 error message 是什麼？
3. 要改哪個檔案？
4. 修完後用哪個指令驗證？

## 建議指令

```powershell
docker compose ps
docker compose logs backend
docker compose exec backend python -c "import os; print(os.getenv('MYSQL_HOST'))"
curl -i http://localhost:8080/api/products
```
