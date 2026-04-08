# URL Микросервис для сокращения ссылок

Сервис для сокращения ссылок (аналог Bitly). Позволяет создавать короткие ссылки, отслеживать количество переходов и получать статистику.

## Возможности

- **Создание короткой ссылки** — `POST /shorten`
- **Редирект по короткому ID** — `GET /{short_id}`
- **Статистика переходов** — `GET /stats/{short_id}`
- Автоматический счётчик кликов (хранится в PostgreSQL)
- Unit-тесты основной логики

## Стек технологий

- **Python** — основной язык
- **FastAPI** — веб-фреймворк
- **PostgreSQL** — хранение данных
- **Docker / Docker Compose** — контейнеризация
- **pytest** — тестирование

## Быстрый старт (Docker Compose)

```bash
# Клонируйте репозиторий
git clone https://github.com/dev-stefanov/victory_bitly.git
cd victory_bitly

# Запустите сервис и базу данных
docker-compose up --build

# Запустить тесты
docker-compose run test