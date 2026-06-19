# P2 - Python CI 自動測試

目標：用 GitHub Actions 在每次 push / pull request 時自動跑 pytest。

## starter

`starter/` 有基本函式與 CI workflow。練習時請新增 `divide(a, b)` 與測試。

## solution

`solution/` 已包含 `divide(a, b)` 與除以 0 的測試。

## 本機測試

```powershell
pip install -r requirements.txt
pytest test_app.py -v
```

## 故意讓 CI 失敗

把 `app.py` 的其中一個函式改錯，push 到 GitHub，觀察 Actions 變紅。修好後再 push，確認變回綠色。
