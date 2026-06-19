# P3 - 多版本 MySQL 並存

目標：同時跑 MySQL 8.0 和 MySQL 9.0，使用不同 host port。

啟動：

```powershell
docker compose up -d
```

確認狀態：

```powershell
docker compose ps
```

查看版本：

```powershell
docker exec -it mysql8 mysql -u root -p -e "SELECT VERSION();"
docker exec -it mysql9 mysql -u root -p -e "SELECT VERSION();"
```

密碼都是：

```text
root123
```

重點：

- 兩個容器內部都是 3306。
- 主機對外 port 要錯開：3306 和 3307。

清理：

```powershell
docker compose down -v
```
