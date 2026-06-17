from flask import Flask
import socket
import os

app = Flask(__name__)

# Read values injected by the ConfigMap (envFrom in deployment.yaml).
# Defaults let this same code still run fine outside Kubernetes (e.g. on your laptop).
APP_VERSION = os.environ.get("APP_VERSION", "local-dev")
GREETING_MESSAGE = os.environ.get("GREETING_MESSAGE", "Hello, world!")

@app.route('/')
def home():
    hostname = socket.gethostname()
    return f"""
    <h1>Flask Kubernetes Project</h1>
    <h2>Created by Arsalan</h2>
    <p>{GREETING_MESSAGE}</p>
    <p>This application is running inside Kubernetes.</p>
    <p><b>Pod Name:</b> {hostname}</p>
    <p><b>App Version:</b> {APP_VERSION}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
