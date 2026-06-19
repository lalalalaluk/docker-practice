# P2 - 容器生命週期練習

每一步都用 `docker ps` 或 `docker ps -a` 確認狀態。

```powershell
docker run -d --name lifecycle-test -p 9090:80 nginx
docker ps

docker stop lifecycle-test
docker ps -a

docker start lifecycle-test
docker ps

docker restart lifecycle-test
docker ps

docker rm -f lifecycle-test
docker ps -a
```

觀察重點：

- `docker ps` 只看執行中的容器。
- `docker ps -a` 會看到停止的容器。
- `docker start` 啟動已停止容器。
- `docker restart` 重新啟動容器。
- `docker rm -f` 會強制刪除執行中的容器，開發環境方便，但正式環境要小心。
