import os
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name="Azure Cloud Dashboard",
        environment=os.getenv("APP_ENV", "Production"),
    )


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy",
            "service": "azure-webapp",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    ), 200


@app.route("/api/info")
def info():
    return jsonify(
        {
            "application": "Azure Cloud Dashboard",
            "platform": "Azure App Service",
            "framework": "Flask",
            "cicd": "GitHub Actions",
            "version": "1.0.0",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
