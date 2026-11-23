"""Тесты Flask-приложения."""

import pytest

from app.app import create_app


@pytest.fixture
def client():
    """Создание тестового клиента."""
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_health(client):
    """Проверка endpoint состояния приложения."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_index(client):
    """Проверка главной страницы."""
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["service"] == "devops-ci-app"
    assert data["version"] == "1.1.0-tseplyaev"