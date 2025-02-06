# Production Dockerfile for Noteworthy project
# Stage 1: Build the frontend
FROM node:lts-alpine as frontend

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install -g pnpm

COPY frontend/package.json frontend/pnpm-lock.yaml ./

RUN pnpm install

COPY frontend/ ./

RUN pnpm run build


ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

RUN apt-get update && apt-get install -y \
    curl \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g yarn

WORKDIR /code/frontend
ENV VITE_BASE_API_URL=$VITE_BASE_API_URL
# COPY frontend/package.json frontend/yarn.lock ./
# COPY frontend/index.html ./
# COPY frontend/vite.config.js ./
# COPY frontend/assets/ ./assets/

# RUN yarn
# RUN yarn build

WORKDIR /code
RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction
COPY . /code



RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "madlibs_api.wsgi"]
