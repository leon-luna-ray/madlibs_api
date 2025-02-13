FROM python:3.10-alpine

# Environment variables
ENV PYTHONIOENCODING=utf8
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

# Install system dependencies
RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev \
    mariadb-connector-c-dev \
    jpeg-dev \
    zlib-dev \
    libwebp-dev \
    libffi-dev

# Set working directory
WORKDIR /code

# Copy necessary files
COPY ./manage.py ./manage.py
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml
COPY ./madlibs_ai/ ./madlibs_ai/
COPY ./apps/ ./apps/

# Install Python dependencies using Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Expose the application port
EXPOSE 8080

# Run commands to prepare and start the application
CMD set -xe; \
    python manage.py collectstatic --noinput; \
    python manage.py migrate --noinput; \
    gunicorn madlibs_ai.wsgi:application --bind 0.0.0.0:8080


# # Production Dockerfile for Noteworthy project
# # Stage 1: Build the frontend
# FROM node:lts-alpine as frontend
# RUN mkdir /app
# WORKDIR /app

# ENV PATH /app/node_modules/.bin:$PATH

# RUN npm install -g pnpm

# COPY frontend/package.json frontend/pnpm-lock.yaml ./

# RUN pnpm install

# COPY frontend/ ./

# RUN pnpm run build


# ARG PYTHON_VERSION=3.10-slim-bullseye

# FROM python:${PYTHON_VERSION}

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # RUN mkdir -p /app

# WORKDIR /app/backend

# RUN apt-get update && apt-get install -y \
#     curl \
#     && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
#     && apt-get install -y nodejs \
#     && npm install -g yarn

# # WORKDIR /app/frontend
# # ENV VITE_BASE_API_URL=$VITE_BASE_API_URL
# # COPY frontend/package.json frontend/yarn.lock ./
# # COPY frontend/index.html ./
# # COPY frontend/vite.config.js ./
# # COPY frontend/assets/ ./assets/

# # RUN yarn
# # RUN yarn build

# # WORKDIR /app
# RUN pip install poetry
# COPY pyproject.toml poetry.lock /app/
# RUN poetry config virtualenvs.create false
# RUN poetry install --only main --no-root --no-interaction
# COPY . /app



# RUN python manage.py collectstatic --noinput

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "madlibs_ai.wsgi"]
