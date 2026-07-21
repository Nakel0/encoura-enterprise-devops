from flask import Flask
import logging
import os

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home():

    logging.info("Home endpoint accessed")

    return {
        "application": "Encoura Enterprise Platform",
        "environment": os.getenv("ENVIRONMENT", "Development"),
        "version": "1.0.0",
        "status": "Running"
    }

@app.route("/health")
def health():

    logging.info("Health check called")

    return {
        "status": "Healthy"
    }

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )