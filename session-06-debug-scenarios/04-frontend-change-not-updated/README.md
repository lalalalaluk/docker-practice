# 情境 4：前端改了，畫面卻沒有變

這題需要先跑過一次，再修改 React 原始碼，才能重現問題。

## 重現

先啟動原本專案：

```powershell
copy .env.example .env
docker compose up -d --build
```

打開 `http://localhost:8080`，確認標題是 `Product List`。

接著修改 `frontend/src/App.jsx`，把標題改成：

```jsx
<h1>Product Catalog</h1>
```

只重新執行：

```powershell
docker compose up -d
```

## 現象

瀏覽器仍然看到舊標題。

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
