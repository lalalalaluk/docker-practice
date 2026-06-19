from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(message="Hello from CI/CD!", version="1.0.0")


@app.route("/health")
def health():
    return jsonify(status="healthy")


def add(a, b):
    return a + b


def is_positive(n):
    return n > 0


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
