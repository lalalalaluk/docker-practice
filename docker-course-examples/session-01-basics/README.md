# Session 01 - Docker 概念、安裝與第一個容器

這一堂的範例重點：

- 用 `docker run hello-world` 理解 Image、Container、Registry。
- 比較 Python Image 大小。
- 用 Nginx 掛載本機 HTML，做出第一個可修改的網頁容器。
- 挑戰題用 Apache/httpd 對照 Nginx。

## 課堂指令

```powershell
docker run hello-world

docker pull python:3.11
docker pull python:3.11-slim
docker pull python:3.11-alpine
docker images | findstr python
```

## 練習

- `p2-nginx-custom-page`：啟動 Nginx 並自訂歡迎頁面。
- `c1-httpd`：挑戰題，改用 Apache/httpd 跑靜態頁面。

## 清理

```powershell
docker rm -f course-nginx course-httpd
docker rmi python:3.11 python:3.11-alpine
```
