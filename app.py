from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from sumit ! zeotap"

@app.route("/health")
def health():
    return {
        "status": "OK",
        "hostname": socket.gethostname()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
