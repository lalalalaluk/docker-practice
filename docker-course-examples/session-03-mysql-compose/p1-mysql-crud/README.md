# P1 - MySQL 完整操作

目標：

1. 用 `docker run` 啟動 MySQL 8.0。
2. 用 `docker exec` 進入 MySQL。
3. 建立 `employees` 表。
4. 插入、查詢、更新、刪除資料。
5. 離開並清理。

啟動 MySQL：

```powershell
docker run -d ^
  --name employees-mysql ^
  -e MYSQL_ROOT_PASSWORD=root123 ^
  -e MYSQL_DATABASE=company ^
  -p 3306:3306 ^
  -v employees-data:/var/lib/mysql ^
  mysql:8.0
```

進入 MySQL：

```powershell
docker exec -it employees-mysql mysql -u root -p
```

密碼是：

```text
root123
```

練習：

- 先看 `starter/employees.sql`，自己補完。
- 完成後對照 `solution/employees.sql`。

清理：

```powershell
docker rm -f employees-mysql
docker volume rm employees-data
```
