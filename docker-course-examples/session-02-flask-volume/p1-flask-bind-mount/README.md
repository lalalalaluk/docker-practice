# P1 - Flask 容器操作全流程

## Starter

```powershell
cd starter
docker run -it --rm -p 5000:5000 -v "${PWD}:/app" -w /app python:3.11 bash
```

進入容器後：

```bash
pip install -r requirements.txt
python app.py
```

瀏覽器打開：

```text
http://localhost:5000
http://localhost:5000/about
```

修改本機的 `app.py`，停止 Flask 後重新執行 `python app.py`，確認畫面變更。

## Solution

`solution` 版本多了 `/health` 路由，方便確認服務狀態。

可直接執行：

```powershell
cd solution
docker run -it --rm -p 5000:5000 -v "${PWD}:/app" -w /app python:3.11 bash -c "pip install -r requirements.txt && python app.py"
```
