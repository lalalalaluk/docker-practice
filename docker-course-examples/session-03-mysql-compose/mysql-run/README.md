# MySQL Run - 單一 MySQL 容器

啟動 MySQL：

```powershell
docker run -d ^
  --name my-mysql ^
  -e MYSQL_ROOT_PASSWORD=my-secret-pw ^
  -e MYSQL_DATABASE=testdb ^
  -e MYSQL_USER=testuser ^
  -e MYSQL_PASSWORD=testpass ^
  -p 3306:3306 ^
  -v mysql-data:/var/lib/mysql ^
  mysql:8.0
```

確認啟動：

```powershell
docker ps
docker logs my-mysql
```

看到 `ready for connections` 後進入 MySQL：

```powershell
docker exec -it my-mysql mysql -u root -p
```

登入後可以把 `product.sql` 的內容貼進 MySQL 執行。

清理容器但保留資料：

```powershell
docker rm -f my-mysql
```

連資料也刪除：

```powershell
docker volume rm mysql-data
```
