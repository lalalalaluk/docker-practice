# 情境 3：Nginx proxy 寫錯，前端正常但 API 失敗

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 現象

- `http://localhost:8080` 看得到前端
- `/api/products` 失敗
- frontend logs 會出現 upstream 相關錯誤

## 任務

回答這四件事：

1. 哪個 service 壞了？
2. 第一個有用的 error message 是什麼？
3. 要改哪個檔案？
4. 修完後用哪個指令驗證？

## 建議指令

```powershell
docker compose logs frontend
docker compose logs backend
curl -i http://localhost:8080/api/products
```
