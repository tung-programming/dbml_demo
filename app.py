"""Harmless sample app for repository-scanning tests."""

from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({
        "project": "dummy-dependency-analyzer-fixture",
        "purpose": "test dependency extraction and advisory matching",
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
