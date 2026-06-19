# Session 03 - MySQL、Docker Compose 與多容器管理

這一堂的範例重點：

- 用 Docker 啟動 MySQL。
- 用 SQL 驗證資料庫真的可用。
- 用 Named Volume 保存 MySQL 資料。
- 用 Docker Compose 管理 Nginx + MySQL。
- 練習多版本 MySQL 並存。
- 挑戰 Nginx + MySQL + Redis 三服務環境。

資料夾：

- `mysql-run`：單一 MySQL 容器與 `Product` SQL 範例。
- `p1-mysql-crud`：練習題 P1，employees CRUD。
- `compose-nginx-mysql`：課堂示範，Nginx + MySQL。
- `p2-nginx-redis-compose`：練習題 P2，從零寫 Nginx + Redis Compose。
- `p3-mysql-versions`：練習題 P3，多版本 MySQL 並存。
- `c1-nginx-mysql-redis`：挑戰題 C1，三服務 Compose。
- `c2-docker-hub-explore`：挑戰題 C2，Docker Hub 探索紀錄模板。
