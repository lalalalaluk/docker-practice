# Docker 基礎教學

這個 repo 提供 Docker 基礎教學的上課投影片與實作範例程式碼。

## 投影片

| 堂數 | 主題 | 檔案 |
|---|---|---|
| 第 1 堂 | Docker 概念、安裝與第一個容器 | [docker-session1-basics-setup.pptx](slides/docker-session1-basics-setup.pptx) |
| 第 2 堂 | Flask 容器、容器管理與 Volume | [docker-session2-flask-volume.pptx](slides/docker-session2-flask-volume.pptx) |
| 第 3 堂 | MySQL、Docker Compose 與多容器管理 | [docker-session3-mysql-compose.pptx](slides/docker-session3-mysql-compose.pptx) |
| 第 4 堂 | Dockerfile、映像檔優化與資源配置 | [docker-session4-dockerfile-resources.pptx](slides/docker-session4-dockerfile-resources.pptx) |
| 第 5 堂 | CI/CD 概念與 GitHub Actions 入門 | [docker-session5-cicd-github-actions.pptx](slides/docker-session5-cicd-github-actions.pptx) |
| 第 6 堂 | GitHub Actions 進階實作與課程總結 | [docker-session6-github-actions-advanced.pptx](slides/docker-session6-github-actions-advanced.pptx) |

## 範例程式碼

範例程式碼放在 [docker-course-examples](docker-course-examples/)。

目前包含：

- `session-01-basics`：第一堂，Docker 概念、第一個容器、Nginx/Apache 靜態頁。
- `session-02-flask-volume`：第二堂，Flask 容器、容器生命週期、Volume。
- `session-03-mysql-compose`：第三堂，MySQL、Docker Compose、多容器管理。

## 使用方式

1. 先下載或 clone 這個 repo。
2. 打開對應堂數的 PPT。
3. 進入 `docker-course-examples` 的對應資料夾。
4. 依照該資料夾的 `README.md` 操作。

本課程以 Windows + Docker Desktop + PowerShell 為主要環境。
