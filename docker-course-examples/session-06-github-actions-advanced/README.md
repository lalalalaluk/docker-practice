# Session 06 - GitHub Actions 進階實作與課程總結

這一堂把前面學過的 Dockerfile、測試、Docker Hub 與 GitHub Actions 串成完整 CI/CD pipeline。

## 範例列表

- `p1-flask-cicd`：完整 Flask CI/CD pipeline。
- `p2-badge-cache-matrix`：README badge、pip cache、多 Python 版本測試。
- `c1-health-check-before-push`：build 後先在 CI 跑容器並測 `/health`，成功才 push。
- `c2-flask-mysql-compose`：Flask + MySQL + Docker Compose capstone。

## 使用方式

這些 workflow 是給學生複製到自己的 GitHub Repository 根目錄使用。放在課程 repo 的子資料夾裡時，GitHub Actions 不會自動執行。

需要 Docker Hub push 的範例，都要先設定 GitHub Secrets：

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
