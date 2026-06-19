# Flask CI/CD Demo

![CI/CD](https://github.com/your-name/docker-cicd-demo/actions/workflows/cicd.yml/badge.svg)

## 本機執行

```powershell
pip install -r requirements.txt
pytest test_app.py -v

docker build -t docker-cicd-demo .
docker run -d --name cicd-test -p 5000:5000 docker-cicd-demo
curl http://localhost:5000/health
docker rm -f cicd-test
```

把 badge 裡的 `your-name/docker-cicd-demo` 改成你的 GitHub repo。
