import os

import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "product_user"),
        password=os.getenv("MYSQL_PASSWORD", "product_password"),
        database=os.getenv("MYSQL_DATABASE", "product_app"),
    )


def fetch_products():
    conn = get_connection()
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
