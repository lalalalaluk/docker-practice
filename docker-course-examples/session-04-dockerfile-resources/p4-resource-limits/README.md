# P4 - 資源限制實驗

目標：用 `--cpus`、`-m` 限制容器資源，並用 `docker stats` 觀察差異。

## 啟動兩個容器

```powershell
docker run -d --name no-limit nginx:alpine
docker run -d --name limited --cpus=0.5 -m 128m nginx:alpine
```

## 觀察資源

```powershell
docker stats --no-stream
```

觀察重點：

- `limited` 的記憶體上限會顯示 128MiB 左右。
- `--cpus=0.5` 表示最多使用半個 CPU 核心的運算能力。

## 動態調整限制

```powershell
docker update --cpus=1 -m 256m limited
docker stats --no-stream
```

## 清理

```powershell
docker rm -f no-limit limited
```
