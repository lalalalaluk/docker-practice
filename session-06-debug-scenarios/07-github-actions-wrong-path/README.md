# 情境 7：CI 在本機正常，GitHub Actions 卻失敗

這題要把本資料夾內容當成一個 GitHub repo 根目錄來練習。

## 本機驗證

```powershell
copy .env.example .env
docker compose up -d --build
curl http://localhost:8080/api/products
docker compose down -v
```

本機可以正常跑，但 `.github/workflows/cicd.yml` 裡故意使用了不符合這個 repo 根目錄的路徑。

## 現象

GitHub Actions 會在找檔案、安裝套件或執行 Compose 時失敗。

## 任務

回答這四件事：

1. 失敗的是哪一個 job？
2. 第一個有用的 error message 是什麼？
3. 是測試失敗、Docker build 失敗，還是檔案路徑錯？
4. 修完後要怎麼重新觸發 workflow？

## 建議檢查

- `.github/workflows/cicd.yml`
- workflow 的 `working-directory`
- `docker compose -f ... --env-file ...` 的路徑
- Docker build context 的路徑
