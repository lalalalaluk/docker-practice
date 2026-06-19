# C1 - Apache/httpd 挑戰題

目標：到 Docker Hub 查看 `httpd` 官方文件，並用 Apache/httpd 跑起一個靜態頁面。

進入完成版資料夾：

```powershell
cd solution
```

啟動 httpd：

```powershell
docker run -d --name course-httpd -p 8081:80 -v "${PWD}\my-html:/usr/local/apache2/htdocs:ro" httpd:2.4
```

打開瀏覽器：

```text
http://localhost:8081
```

觀察重點：

- Nginx 的靜態頁目錄是 `/usr/share/nginx/html`。
- httpd 的靜態頁目錄是 `/usr/local/apache2/htdocs`。
- 兩者都可以用 Bind Mount 掛載本機 HTML。

清理：

```powershell
docker rm -f course-httpd
```
