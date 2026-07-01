# 第 6 堂 Docker Compose 練習題

這裡每個 `practice-*` 資料夾都是一題獨立練習。題目資料夾不會在檔名或說明裡直接寫出答案，請先用 logs、curl、exec 和設定檔自行定位問題。

## 建議流程

進入題目資料夾後先執行：

```powershell
copy .env.example .env
docker compose up -d --build
```

再用固定流程查問題：

```powershell
docker compose ps
docker compose logs frontend
docker compose logs backend
docker compose logs db
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```

每題都要回答：

1. 哪個 service 或哪個 Docker 資源出問題？
2. 第一個有用的 error message 或觀察結果是什麼？
3. 要改哪個檔案或哪個操作流程？
4. 修完後用哪個指令驗證？

切換題目前建議先在上一題資料夾執行：

```powershell
docker compose down -v
```

## 題目列表

| 題目 | 資料夾 |
|---|---|
| Practice 1 | [practice-1](practice-1) |
| Practice 2 | [practice-2](practice-2) |
| Practice 3 | [practice-3](practice-3) |
| Practice 4 | [practice-4](practice-4) |
| Practice 5 | [practice-5](practice-5) |
| Practice 6 | [practice-6](practice-6) |
| Practice 7 | [practice-7](practice-7) |
| Practice 8 | [practice-8](practice-8) |

解題思路與解答放在 [solution](solution)，每題一個 markdown 檔，上課練習時不要先打開。
