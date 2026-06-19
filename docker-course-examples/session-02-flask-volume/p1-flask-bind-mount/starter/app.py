from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello Docker!</h1><p>This is running inside a container.</p>"


@app.route("/about")
def about():
    return "<h1>About</h1><p>This is a Flask app running in Docker.</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
