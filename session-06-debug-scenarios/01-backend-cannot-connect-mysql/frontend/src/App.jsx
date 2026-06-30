import { useEffect, useState } from 'react'
import './App.css'

export default function App() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  async function loadProducts() {
    try {
      const response = await fetch('/api/products')
      if (!response.ok) {
        throw new Error('failed to load products')
      }

      const data = await response.json()
      setProducts(data)
    } catch (err) {
      setError('商品資料載入失敗，請檢查 backend 和 db logs。')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    loadProducts()
  }, [])

  return (
    <main className="page">
      <section className="shell">
        <p className="eyebrow">Docker Fullstack Capstone</p>
        <h1>Product List</h1>
        <p className="lead">
          React 透過 Nginx proxy 呼叫 Flask API，Flask 再讀取 MySQL 裡的 Product 資料。
        </p>

        {loading ? (
          <p className="muted">載入中...</p>
        ) : error ? (
          <p className="error">{error}</p>
        ) : (
          <div className="table-wrap">
            <table className="product-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>商品名稱</th>
                  <th>價格</th>
                  <th>庫存</th>
                </tr>
              </thead>
              <tbody>
                {products.map((product) => (
                  <tr key={product.id}>
                    <td>{product.id}</td>
                    <td>{product.name}</td>
                    <td>NT$ {Number(product.price).toLocaleString()}</td>
                    <td>{product.stock}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>
    </main>
  )
}
