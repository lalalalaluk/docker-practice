# Practice 8 解答與解題思路

現象：需求需要跨 DB、backend、frontend 一起完成。

解題思路：

1. 先看目前 API 回傳格式：

   ```powershell
   curl http://localhost:8080/api/products
   ```

2. 從資料來源往外查：

   ```powershell
   docker compose exec db mysql -u testuser -p testdb
   ```

   ```sql
   DESCRIBE Product;
   ```

3. 接著檢查 backend SQL 是否有 select 新欄位。

4. 最後檢查 frontend table 是否有 render 新欄位。

修改 `backend/app.py` 的建表欄位：

```sql
Category VARCHAR(50) NOT NULL DEFAULT '未分類',
```

並調整 seed data：

```python
("藍牙耳機", 1290.00, "3C", 50),
```

修改 `backend/app.py` 的 SQL：

```sql
Category AS category,
```

修改 `frontend/src/App.jsx`：

```jsx
<th>分類</th>
<td>{product.category}</td>
```

驗證：

```powershell
docker compose down -v
docker compose up -d --build
curl http://localhost:8080/api/products
```

觀念：完整功能變更要一起驗證資料庫、API、UI 和 image rebuild。
