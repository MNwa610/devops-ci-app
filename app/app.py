"""Flask-приложение для практической работы по DevOps."""

from flask import Flask, jsonify


def create_app():
    """Создание и настройка Flask-приложения."""
    app = Flask(__name__)

    @app.get("/")
    def index():
        """Возвращает информацию о приложении."""
        return jsonify(
            service="devops-ci-app",
            version="1.0.0",
        )

    @app.get("/health")
    def health():
        """Возвращает состояние приложения."""
        return jsonify(status="ok")

    return app


app = create_app()