# Session 05 - CI/CD 與 GitHub Actions 入門

這一堂練習 GitHub Actions 的基本語法，並把 Python 測試與 Docker build 串進 CI/CD。

## 範例列表

- `p1-hello-actions`：第一個 GitHub Actions workflow。
- `p2-python-ci`：Python 函式與 pytest 自動測試。
- `p3-docker-build-push`：測試通過後 build 並 push Docker Image。

## 使用方式

這些範例的 `.github/workflows/*.yml` 放在範例資料夾裡。實際練習時，請把該範例資料夾內容複製到一個新的 GitHub Repository 根目錄，再 push 到 GitHub。

> 注意：放在這個課程 repo 的子資料夾裡時，workflow 不會自動執行。它們是給你複製到自己的 repo 練習用的。
