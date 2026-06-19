# Session 02 - Flask 容器、容器管理與 Volume

這一堂的範例重點：

- 用 `python:3.11` 容器跑 Flask。
- 用 Bind Mount 讓本機程式碼和容器同步。
- 練習容器生命週期：start、stop、restart、rm。
- 用 Named Volume 驗證容器刪除後資料仍存在。
- 用 `:ro` 做唯讀掛載。

練習資料夾：

- `p1-flask-bind-mount`：Flask 容器操作全流程。
- `p2-lifecycle-nginx`：Nginx 容器生命週期。
- `p3-volume-persistence`：Named Volume 持久化驗證。
- `c1-readonly-config`：唯讀掛載挑戰題。
- `c2-two-nginx`：同時跑兩個 Nginx。
