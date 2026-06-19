# P2 - Docker Compose 從零開始

目標：不看講義，自己寫一個 `docker-compose.yml`。

要求：

- 一個 Nginx 容器，映射到 port 8080，掛載本機 HTML 資料夾。
- 一個 Redis 容器，使用 `redis:7-alpine`，映射到 port 6379。
- 兩個容器都設定 `restart: unless-stopped`。
- 用 `docker compose up -d` 啟動。
- 用 `docker compose ps` 確認兩個都跑起來。
- 用 `docker compose down` 關閉。

練習流程：

```powershell
cd starter
```

補完 `docker-compose.yml` 後：

```powershell
docker compose up -d
docker compose ps
docker compose down
```

卡住時對照：

```powershell
cd ..\solution
```
