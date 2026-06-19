# P1 - 從零建構自己的 Image

目標：建立一個最小 Python 程式，寫 Dockerfile，build 成 image 並執行。

## starter

`starter/` 只有 Python 程式，請自己補上：

- `Dockerfile`
- `.dockerignore`

## solution

`solution/` 是參考解法。

## 操作指令

```powershell
cd solution
docker build -t my-first-image .
docker run --rm my-first-image
docker history my-first-image
```

預期輸出：

```text
Hello from my image!
```

## 清理

```powershell
docker rmi my-first-image
```
