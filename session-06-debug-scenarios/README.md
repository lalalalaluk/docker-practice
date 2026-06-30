# 第 6 堂 Docker Compose 除錯情境題

這裡每個資料夾都是一題獨立練習。學生可以只下載其中一個資料夾，也可以 clone 整個 repo。

## 建議流程

進入題目資料夾後先執行：

```powershell
copy .env.example .env
docker compose up -d --build
```

再用固定流程查問題：

```powershell
docker compose ps
docker compose logs frontend
docker compose logs backend
docker compose logs db
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```

每題都要回答：

1. 哪個 service 壞了？
2. 第一個有用的 error message 是什麼？
3. 要改哪個檔案？
4. 修完後用哪個指令驗證？

切換題目前建議先在上一題資料夾執行：

```powershell
docker compose down -v
```

## 題目列表

| 題目 | 資料夾 | 重點 |
|---|---|---|
| 1 | [01-backend-cannot-connect-mysql](01-backend-cannot-connect-mysql) | container 裡的 localhost 不是 db |
| 2 | [02-init-sql-volume-not-refreshing](02-init-sql-volume-not-refreshing) | init.sql 與 named volume |
| 3 | [03-nginx-proxy-typo](03-nginx-proxy-typo) | Nginx upstream service name |
| 4 | [04-frontend-change-not-updated](04-frontend-change-not-updated) | React production build 需要重建 image |
| 5 | [05-backend-port-hidden](05-backend-port-hidden) | backend 不對外暴露也能透過 frontend proxy 使用 |
| 6 | [06-health-ok-products-fail](06-health-ok-products-fail) | health check 不等於完整功能正常 |
| 7 | [07-github-actions-wrong-path](07-github-actions-wrong-path) | GitHub Actions working directory 和檔案路徑 |
| 8 | [08-add-category-field](08-add-category-field) | DB schema 到 frontend UI 的完整變更 |
