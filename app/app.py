"""Flask-приложение для практической работы по DevOps."""

from flask import Flask, jsonify


def create_app():
    """Создание и настройка Flask-приложения."""
    flask_app = Flask(__name__)

    @flask_app.get("/")
    def index():
        """Возвращает информацию о приложении."""
        return jsonify(
            service="devops-ci-app",
            version="1.0.0",
        )

    @flask_app.get("/health")
    def health():
        """Возвращает состояние приложения."""
        return jsonify(status="ok")

    return flask_app


app = create_app()