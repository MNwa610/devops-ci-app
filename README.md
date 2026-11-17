# DevOps CI App

Учебное Flask-приложение для практической работы № 10.

## Endpoints

- `GET /` — информация о приложении.
- `GET /health` — проверка состояния приложения.

## CI pipeline

GitHub Actions выполняет последовательность:

1. Pylint — статический анализ.
2. pytest — модульные тесты.
3. Docker build — сборка образа.
4. Smoke-test — запуск контейнера и проверка `/health`.
5. GHCR — публикация образа после успешных проверок в main.

## Container

Образ публикуется в GitHub Container Registry (GHCR).

Теги:
- полный SHA коммита;
- latest.