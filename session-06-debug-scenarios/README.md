# 第 6 堂除錯練習

每個 `practice-*` 是一題。先不要看 `solution/`。

## 基本流程

```powershell
copy .env.example .env
docker compose up -d --build
```

常用檢查：

```powershell
docker compose ps
docker compose logs frontend
docker compose logs backend
docker compose logs db
curl http://localhost:8080/api/health
curl http://localhost:8080/api/products
```

換下一題前：

```powershell
docker compose down -v
```

## 題目

- [practice-1](practice-1)
- [practice-2](practice-2)
- [practice-3](practice-3)
- [practice-4](practice-4)
- [practice-5](practice-5)
- [practice-6](practice-6)
- [practice-7](practice-7)
- [practice-8](practice-8)
