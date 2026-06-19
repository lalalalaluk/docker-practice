# Compose Demo - Nginx + MySQL

這是第三堂課堂示範：用一個 `docker-compose.yml` 同時啟動 Nginx 和 MySQL。

啟動：

```powershell
docker compose up -d
```

確認：

```powershell
docker compose ps
docker compose logs
```

打開網頁：

```text
http://localhost:8080
```

連線 MySQL：

```powershell
docker exec -it demo-mysql mysql -u demo_user -p
```

密碼：

```text
demo_pass
```

MySQL 內測試：

```sql
SHOW DATABASES;
USE demo_db;
CREATE TABLE test (id INT PRIMARY KEY, message VARCHAR(100));
INSERT INTO test VALUES (1, 'Docker Compose works!');
SELECT * FROM test;
EXIT;
```

停止但保留資料：

```powershell
docker compose down
```

停止並刪除資料：

```powershell
docker compose down -v
```
