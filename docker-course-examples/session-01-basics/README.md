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

觀察重點：

- 只要先看 `docker images` 的 `SIZE` 欄位。
- `python:3.11`、`python:3.11-slim`、`python:3.11-alpine` 是同一個 Python 版本的不同 Image 變體。
- 大小差異主要來自底層系統與預裝工具不同；第一堂只需要理解這件事，不需要看懂每個 layer。

## 練習

- `p2-nginx-custom-page`：啟動 Nginx 並自訂歡迎頁面。
- `c1-httpd`：挑戰題，改用 Apache/httpd 跑靜態頁面。

## 清理

```powershell
docker rm -f course-nginx course-httpd
docker rmi python:3.11 python:3.11-slim python:3.11-alpine
```
