# Practice 5

這題觀察 port。

## 啟動

```powershell
copy .env.example .env
docker compose up -d --build
```

## 先查

```powershell
docker compose ps
curl -i http://localhost:5000/api/health
curl -i http://localhost:8080/api/health
curl -i http://localhost:8080/api/products
```

開發版：

```powershell
docker compose -f compose.yaml -f compose.dev.yml up -d --build
curl -i http://localhost:5000/api/health
```

想一下：哪個 service 真的需要對外？
