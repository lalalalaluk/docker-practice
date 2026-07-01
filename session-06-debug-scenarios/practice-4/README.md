# Practice 4

這題需要先跑過一次，再修改前端原始碼，才能重現問題。

## 重現

先啟動原本專案：

```powershell
copy .env.example .env
docker compose up -d --build
```

打開 `http://localhost:8080`，確認畫面正常。

接著修改前端標題，只重新執行：

```powershell
docker compose up -d
```

## 現象

瀏覽器仍然看到舊畫面。

## 任務

回答這四件事：

1. 哪個 image 或 container 還在使用舊內容？
2. logs 為什麼不一定會顯示錯誤？
3. 要改哪個操作指令？
4. 修完後用哪個指令驗證？

## 建議指令

```powershell
docker compose ps
docker compose logs frontend
docker compose build frontend
docker compose up -d frontend
```
