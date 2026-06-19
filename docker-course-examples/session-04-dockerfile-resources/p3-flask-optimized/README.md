# P3 - Flask Image 優化

目標：把 Flask app 打包成 image，並練習 build cache、`.dockerignore`、環境變數與非 root 使用者。

## starter

`starter/` 是基礎版：

```powershell
cd starter
docker build -t flask-basic .
docker run -d --name flask-basic -p 5000:5000 flask-basic
```

## solution

`solution/` 是優化版：

```powershell
cd solution
docker build -t flask-optimized .
docker run -d --name flask-optimized -p 5000:5000 flask-optimized
```

打開：

```text
http://localhost:5000
```

## 檢查容器使用者

```powershell
docker exec -it flask-optimized whoami
```

預期會看到：

```text
appuser
```

## 清理

```powershell
docker rm -f flask-basic flask-optimized
docker rmi flask-basic flask-optimized
```
