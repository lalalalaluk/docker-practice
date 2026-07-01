# Practice 3

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 現象

- 首頁可以開
- `/api/products` 失敗
- frontend logs 有錯誤訊息

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
