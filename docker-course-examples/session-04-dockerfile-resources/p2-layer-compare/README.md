# P2 - 分層比較實驗

目標：比較「多個 RUN」和「合併 RUN」對 layer 與 image 大小的影響。

## 操作指令

```powershell
docker build -f Dockerfile.many -t layer-test:many .
docker build -f Dockerfile.few -t layer-test:few .

docker images | findstr layer-test
docker history layer-test:many
docker history layer-test:few
```

觀察重點：

- `Dockerfile.many` 會有比較多層。
- `Dockerfile.few` 把 apt 安裝和清理放在同一層，通常更乾淨。

## 執行

```powershell
docker run --rm layer-test:many
docker run --rm layer-test:few
```

## 清理

```powershell
docker rmi layer-test:many layer-test:few
```
