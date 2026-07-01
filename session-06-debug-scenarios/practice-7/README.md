# Practice 7

這題要把本資料夾內容當成一個 GitHub repo 根目錄來練習。

## 本機驗證

```powershell
copy .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/products
docker compose down -v
```

## 現象

本機可以正常跑，但 CI 會失敗。

## 任務

回答這四件事：

1. 失敗的是哪一個 job？
2. 第一個有用的 error message 是什麼？
3. 是測試失敗、Docker build 失敗，還是檔案路徑錯？
4. 修完後要怎麼重新觸發 workflow？

## 建議檢查

- workflow 的工作目錄
- workflow 裡的相對路徑
- Docker build context
