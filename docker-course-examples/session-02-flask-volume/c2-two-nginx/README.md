# C2 - 同時跑兩個 Nginx 容器

目標：兩個容器使用不同名稱、不同 host port、不同 HTML 資料夾。

```powershell
docker run -d --name nginx-a -p 8082:80 -v "${PWD}\site-a:/usr/share/nginx/html:ro" nginx
docker run -d --name nginx-b -p 8083:80 -v "${PWD}\site-b:/usr/share/nginx/html:ro" nginx
```

打開瀏覽器：

```text
http://localhost:8082
http://localhost:8083
```

確認狀態：

```powershell
docker ps
```

清理：

```powershell
docker rm -f nginx-a nginx-b
```
