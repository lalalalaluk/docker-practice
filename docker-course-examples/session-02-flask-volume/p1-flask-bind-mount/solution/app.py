from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return """
    <h1>Hello Docker!</h1>
    <p>This Flask app is running inside a Python container.</p>
    <p>Try <a href="/about">/about</a> and <a href="/health">/health</a>.</p>
    """


@app.route("/about")
def about():
    return "<h1>About</h1><p>Bind Mount lets local file changes appear inside the container.</p>"


@app.route("/health")
def health():
    return jsonify(
        status="ok",
        service="session-02-flask-volume",
        checked_at=datetime.now(timezone.utc).isoformat(),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
