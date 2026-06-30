# 情境 5：移除 backend 對外 port

這題不是壞掉的設定，而是要觀察哪些入口應該對外暴露。

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 預期現象

- `localhost:5000` 不能直接打 backend
- `localhost:8080/api/health` 可以
- `localhost:8080/api/products` 可以

## 任務

回答這四件事：

1. 哪個 service 有對外 port？
2. backend 沒有 ports 時，frontend 為什麼還能呼叫它？
3. 正式部署時通常應該暴露 frontend、backend 還是 db？
4. 用哪些指令驗證？

## 建議指令

```powershell
docker compose ps
curl -i http://localhost:5000/api/health
curl -i http://localhost:8080/api/health
curl -i http://localhost:8080/api/products
```
