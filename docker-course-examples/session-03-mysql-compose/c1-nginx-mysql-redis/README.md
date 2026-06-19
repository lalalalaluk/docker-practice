# C1 - Nginx + MySQL + Redis 三服務挑戰

目標：寫一個 `docker-compose.yml` 同時啟動三個服務，並觀察狀態與資源。

服務要求：

- Nginx：提供靜態頁面。
- MySQL：使用 Named Volume 保存資料。
- Redis：使用 `redis:7-alpine`。

練習：

```powershell
cd starter
```

補完 `docker-compose.yml` 後：

```powershell
docker compose up -d
docker compose ps
docker stats --no-stream
docker compose down -v
```

參考解法在 `solution`。
