# syntax=docker/dockerfile:1.7
FROM python:3.11-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    UVICORN_WORKERS=2

# Install security updates and minimal runtime deps
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create non-root user
RUN groupadd -r app && useradd -r -g app app

COPY services/backend/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY services/backend /app

# Drop privileges
USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]