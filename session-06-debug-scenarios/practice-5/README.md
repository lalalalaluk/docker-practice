# Practice 5

這題不是找壞掉的設定，而是觀察哪些入口應該對外暴露。

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 現象

- 其中一個對外 port 不能直接打
- 從主要入口呼叫 health API 可以成功
- 從主要入口呼叫 products API 可以成功

## 任務

回答這四件事：

1. 哪個 service 有對外 port？
2. 沒有對外 port 的 service，為什麼仍然能被其他 container 呼叫？
3. 正式部署時通常應該暴露哪一層？
4. 用哪些指令驗證？

## 建議指令

```powershell
docker compose ps
curl -i http://localhost:5000/api/health
curl -i http://localhost:8080/api/health
curl -i http://localhost:8080/api/products
```
