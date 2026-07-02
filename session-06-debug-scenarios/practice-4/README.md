# Practice 4

## 重現

```powershell
copy .env.example .env
docker compose up -d --build
```

改 `frontend/src/App.jsx` 的標題後，只執行：

```powershell
docker compose up -d
```

## 現象

畫面還是舊的。

## 先查

```powershell
docker compose ps
docker compose logs frontend
docker compose build frontend
```
