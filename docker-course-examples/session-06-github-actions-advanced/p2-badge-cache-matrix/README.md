# P2 - Badge、Cache 與 Matrix

這個資料夾提供可複製的 workflow 片段，練習：

- README 顯示 CI badge
- 快取 pip 套件
- 用 matrix 測試多個 Python 版本

## README badge

把以下內容放到你的 repo `README.md`，並把 `your-name/docker-cicd-demo` 改成你的 repo：

```markdown
![CI](https://github.com/your-name/docker-cicd-demo/actions/workflows/ci-matrix.yml/badge.svg)
```

## Workflow

複製 `.github/workflows/ci-matrix.yml` 到你的 repo 後 push，即可在 Actions 頁面看到多版本測試。
