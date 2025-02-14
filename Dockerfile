# Stage 1: Frontend build
FROM node:lts-alpine as frontend-builder

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY frontend/package.json frontend/pnpm-lock.yaml ./

RUN npm install -g pnpm && \
    pnpm install --frozen-lockfile

COPY frontend/ .
RUN pnpm run build

# Stage 2: Backend build
FROM python:3.10-alpine as backend-builder

RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev \
    mariadb-connector-c-dev \
    jpeg-dev \
    zlib-dev \
    libwebp-dev \
    libffi-dev

WORKDIR /code

COPY backend/pyproject.toml backend/poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi

COPY backend/ .

# Stage 3: Final production image
FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/code \
    STATIC_FILES_ROOT=/code/staticfiles

RUN apk update && apk add --no-cache \
    postgresql-client \
    mariadb-connector-c \
    jpeg \
    zlib \
    libwebp \
    libffi

WORKDIR /code

# Copy backend dependencies
COPY --from=backend-builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=backend-builder /usr/local/bin /usr/local/bin

# Copy application code
COPY backend/manage.py .
COPY backend/madlibs_ai/ ./madlibs_ai/
COPY backend/apps/ ./apps/

# Copy built frontend assets
COPY --from=frontend-builder /app/dist /code/frontend-dist

# Collect static files and set up permissions
RUN python manage.py collectstatic --noinput && \
    adduser -D myuser && \
    chown -R myuser:myuser /code

USER myuser

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "madlibs_ai.wsgi:application"]