import os

import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

SAMPLE_PRODUCTS = [
    ("藍牙耳機", 1290.00, 50),
    ("USB-C 線", 299.00, 150),
    ("27吋螢幕", 5990.00, 20),
    ("無線滑鼠", 590.00, 80),
    ("機械鍵盤", 2490.00, 35),
]


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "testuser"),
        password=os.getenv("MYSQL_PASSWORD", "testpass"),
        database=os.getenv("MYSQL_DATABASE", "testdb"),
    )


def ensure_product_data(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Product (
          Id INT AUTO_INCREMENT PRIMARY KEY,
          Name VARCHAR(100) NOT NULL,
          Price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
          Stock INT NOT NULL DEFAULT 0,
          CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
    )
    cursor.execute("SELECT COUNT(*) FROM Product")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany(
            "INSERT INTO Product (Name, Price, Stock) VALUES (%s, %s, %s)",
            SAMPLE_PRODUCTS,
        )
        conn.commit()
    cursor.close()


def fetch_products():
    conn = get_connection()
    ensure_product_data(conn)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT
          Id AS id,
          Name AS name,
          Price AS price,
          Stock AS stock,
          CreatedAt AS created_at
        FROM Product
        ORDER BY Id
        """
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    for row in rows:
        row["price"] = float(row["price"])
        row["created_at"] = row["created_at"].isoformat()

    return rows


@app.route("/api/health")
def health():
    return jsonify(status="ok")


@app.route("/api/products", methods=["GET"])
def list_products():
    return jsonify(fetch_products())


def add(a, b):
    return a + b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
