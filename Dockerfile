FROM python:3.11-alpine3.16

RUN apk add --no-cache mariadb-connector-c-dev build-base

EXPOSE 8000
COPY app /app/
COPY poetry.lock pyproject.toml /app/
COPY .env /app/.env

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
