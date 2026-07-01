# Practice 6

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 現象

- `/api/health` 回傳 `{"status":"ok"}`
- `/api/products` 失敗
- backend process 活著，但讀商品資料失敗

## 任務

回答這四件事：

1. 哪個 service 壞了，或是哪兩層之間的合約不一致？
2. 第一個有用的 error message 是什麼？
3. 要改哪個檔案？
4. 修完後用哪個指令驗證？

## 建議指令

```powershell
curl http://localhost:8080/api/health
curl -i http://localhost:8080/api/products
docker compose logs backend
docker compose exec db mysql -u product_user -p product_app
```
