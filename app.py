from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
