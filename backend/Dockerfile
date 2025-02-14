FROM python:3.10-alpine

ENV PYTHONIOENCODING=utf8
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev \
    mariadb-connector-c-dev \
    jpeg-dev \
    zlib-dev \
    libwebp-dev \
    libffi-dev

WORKDIR /code

COPY ./manage.py ./manage.py
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml
COPY ./madlibs_ai/ ./madlibs_ai/
COPY ./apps/ ./apps/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

EXPOSE 8080

CMD set -xe; \
    python manage.py collectstatic --noinput; \
    python manage.py migrate --noinput; \
    gunicorn madlibs_ai.wsgi:application --bind 0.0.0.0:8080
    