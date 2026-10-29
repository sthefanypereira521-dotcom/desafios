FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --only main



COPY alembic.ini ./
COPY alembic ./alembic
COPY database ./database
COPY models ./models


CMD ["alembic", "upgrade", "head"]