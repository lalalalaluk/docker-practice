# Session 06 - React + Flask + MySQL Product List

本資料夾是 Docker 第 6 堂的課堂範例，分成學生練習用的 `starter/` 和完整解答 `solution/`。

目標是做出一個可以展示的三層架構 Product List Web App：

- React 前端只列出商品
- Flask backend 提供 `/api/health` 和 `/api/products`
- MySQL 儲存 `Product` table
- Nginx 在 frontend container 內提供靜態檔並 proxy `/api`
- Docker Compose 一次啟動 frontend、backend、db
- GitHub Actions 自動測試、build、啟動整套服務並檢查 API

## Structure

```text
session-06-fullstack-todo/
  ├── starter/
  │   ├── frontend/
  │   ├── backend/
  │   ├── db/
  │   ├── .env.example
  │   └── README.md
  └── solution/
      ├── compose.yaml
      ├── .env.example
      ├── frontend/
      ├── backend/
      ├── db/
      └── .github/workflows/cicd.yml
```

`starter/` 已經放好 React、Flask、測試、前端樣式、package/requirements 和範例資料 SQL。學生不用從 PPT 複製大量程式碼。

`starter/` 刻意不提供這些檔案，留給學生練習：

- `backend/Dockerfile`
- `backend/.dockerignore`
- `frontend/Dockerfile`
- `frontend/.dockerignore`
- `frontend/nginx.conf`
- `compose.yaml`
- `.github/workflows/cicd.yml`

`solution/` 是完整可執行解法，可以給老師示範或課後對答案。

## Student workflow

```powershell
cd starter
```

學生要依照課堂指示補上 Dockerfile、Nginx 設定、Compose 和 GitHub Actions workflow。

## Run solution

```powershell
cd solution
cp .env.example .env
docker compose up -d --build
```

Open:

```text
http://localhost:8080
```

Check:

```powershell
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```

Stop:

```powershell
docker compose down
```

Remove database volume:

```powershell
docker compose down -v
```
