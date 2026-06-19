# P3 - Volume 持久化驗證

目標：證明容器刪掉後，Named Volume 裡的資料仍然存在。

建立 Volume：

```powershell
docker volume create test-data
```

第一次進 Alpine 容器，寫入檔案：

```powershell
docker run -it --rm -v test-data:/data alpine sh
```

容器內執行：

```sh
echo "hello volume" > /data/test.txt
cat /data/test.txt
exit
```

第二次進新容器，確認檔案還在：

```powershell
docker run -it --rm -v test-data:/data alpine sh
```

容器內執行：

```sh
cat /data/test.txt
exit
```

清理：

```powershell
docker volume rm test-data
```
