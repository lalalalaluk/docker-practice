# Docker Course Examples

這個資料夾放 Docker 基礎教學前三堂的可操作範例。

使用方式：

1. 安裝 Docker Desktop，確認 `docker --version` 可以執行。
2. 用 PowerShell 進入某個範例資料夾。
3. 依照該資料夾的 `README.md` 操作。
4. 練習題通常分成 `starter` 和 `solution`：
   - `starter`：上課或練習時先從這裡開始。
   - `solution`：卡住時對照參考解法。

目前包含：

- `session-01-basics`：第一堂，Docker 概念、第一個容器、Nginx/Apache 靜態頁。
- `session-02-flask-volume`：第二堂，Flask 容器、容器生命週期、Volume。
- `session-03-mysql-compose`：第三堂，MySQL、Docker Compose、多容器管理。

注意事項：

- 本課程以 Windows + Docker Desktop + PowerShell 為主要環境。
- 指令中的 `${PWD}` 是 PowerShell 的目前資料夾路徑。
- 如果 port 已經被占用，請先停掉舊容器，或把左邊的 host port 換掉。
- `Dockerfile` 會從第 4 堂正式開始，因此前三堂不把 Dockerfile 放進核心範例。
