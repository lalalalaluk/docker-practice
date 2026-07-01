# Docker 基礎教學

這個 repo 提供 Docker 基礎教學的上課投影片、第 6 堂全端專題練習檔，以及第 6 堂除錯情境題。

第 6 堂不要求從投影片複製完整 React / Flask 程式碼，請直接使用 `session-06-fullstack-todo/starter` 當練習起點。

## 投影片

| 堂數 | 主題 | 檔案 |
|---|---|---|
| 第 1 堂 | 安裝 Docker、理解概念與第一個容器 | [docker-session1-basics-setup.pptx](slides/docker-session1-basics-setup.pptx) |
| 第 2 堂 | Flask 容器、容器管理與 Volume | [docker-session2-flask-volume.pptx](slides/docker-session2-flask-volume.pptx) |
| 第 3 堂 | MySQL、Docker Compose 與多容器管理 | [docker-session3-mysql-compose.pptx](slides/docker-session3-mysql-compose.pptx) |
| 第 4 堂 | Dockerfile、映像檔優化與資源配置 | [docker-session4-dockerfile-resources.pptx](slides/docker-session4-dockerfile-resources.pptx) |
| 第 5 堂 | CI/CD 與 GitHub Actions 實戰 | [docker-session5-cicd-github-actions.pptx](slides/docker-session5-cicd-github-actions.pptx) |
| 第 6 堂 | Docker Compose 全端專題：React + Flask + MySQL | [docker-session6-fullstack-todo.pptx](slides/docker-session6-fullstack-todo.pptx) |

## 使用方式

1. 先下載或 clone 這個 repo。
2. 打開對應堂數的 PPT。
3. 第 1 到 5 堂依照投影片操作。
4. 第 6 堂請搭配 `session-06-fullstack-todo/starter` 練習，完成後可參考 `solution`。

本課程以 Windows + Docker Desktop + PowerShell 為主要環境。

## 第 6 堂全端專題

第 6 堂範例放在 [session-06-fullstack-todo](session-06-fullstack-todo)。

```text
session-06-fullstack-todo/
  ├── starter/   # 學生練習用，已提供 React / Flask / SQL
  └── solution/  # 完整解答
```

學生請從 `starter` 開始：

```powershell
cd session-06-fullstack-todo\starter
```

需要練習完成的檔案包含：

- `backend/Dockerfile`
- `backend/.dockerignore`
- `frontend/Dockerfile`
- `frontend/.dockerignore`
- `frontend/nginx.conf`
- `compose.yaml`
- `.github/workflows/cicd.yml`

## 第 6 堂除錯情境題

每一題都是一個獨立資料夾，放在 [session-06-debug-scenarios](session-06-debug-scenarios)。

學生可以進入任一題資料夾後執行：

```powershell
copy .env.example .env
docker compose up -d --build
```

除錯時建議固定先看：

```powershell
docker compose ps
docker compose logs frontend
docker compose logs backend
docker compose logs db
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```
