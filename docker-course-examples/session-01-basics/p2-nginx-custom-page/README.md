# P2 - 啟動 Nginx 並自訂歡迎頁面

## Starter

先進入 starter：

```powershell
cd starter
```

啟動 Nginx，將本機 `my-html` 資料夾掛載到容器的網頁目錄：

```powershell
docker run -d --name course-nginx -p 8080:80 -v "${PWD}\my-html:/usr/share/nginx/html:ro" nginx
```

打開瀏覽器：

```text
http://localhost:8080
```

進入容器確認檔案內容：

```powershell
docker exec -it course-nginx cat /usr/share/nginx/html/index.html
```

清理：

```powershell
docker rm -f course-nginx
```

## Solution

`solution/my-html/index.html` 是完成版，可對照 starter 裡需要修改的地方。
