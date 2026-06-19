# Session 04 - Dockerfile、映像檔優化與資源配置

這一堂開始把自己的程式打包成 Docker Image，並練習 `.dockerignore`、image 分層、非 root 使用者與容器資源限制。

## 範例列表

- `p1-first-image`：第一個自己 build 的 Python image。
- `p2-layer-compare`：比較多層 Dockerfile 與合併 RUN 的差異。
- `p3-flask-optimized`：把 Flask app 打包並優化 Dockerfile。
- `p4-resource-limits`：用 `--cpus`、`-m` 與 `docker stats` 觀察資源限制。

## 建議順序

1. 先做 `p1-first-image`，理解 `Dockerfile -> Image -> Container`。
2. 再做 `p2-layer-compare`，用 `docker history` 看 layer。
3. 接著做 `p3-flask-optimized`，把前面的 Flask app 變成正式 image。
4. 最後做 `p4-resource-limits`，觀察容器資源使用量。

本課程以 Windows + Docker Desktop + PowerShell 為主要環境。
