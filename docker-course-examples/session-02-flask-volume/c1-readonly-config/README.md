# C1 - 唯讀掛載挑戰題

目標：用 `:ro` 把設定檔掛進容器，並嘗試在容器內修改它。

啟動 Alpine：

```powershell
docker run -it --rm -v "${PWD}\config:/config:ro" alpine sh
```

容器內執行：

```sh
cat /config/app.conf
echo "debug=true" >> /config/app.conf
```

預期結果：

- `cat` 可以讀檔。
- `echo >>` 會失敗，因為掛載是唯讀。

這個練習對應設定檔場景：容器需要讀設定，但不應該修改主機上的設定檔。
