from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to DevOps Platform",
        "version": VERSION
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)