# CLOAK: Enterprise Continuous Least-Privilege IAM Platform

This repository contains a secure, production-ready scaffold for the CLOAK platform with a FastAPI backend, CI, linting, tests, Docker, and environment examples.

## Structure

- `services/backend`: FastAPI application with auth scaffolding and tests
- `.github/workflows`: CI pipelines (lint, type-check, tests, image build)
- `docker-compose.yml`: Local orchestration
- `.env.example`: Environment variables template

## Backend (FastAPI)

Prerequisites: Python 3.11+.

Create and activate a virtual environment, then install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r services/backend/requirements.txt
```

Run the app:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir services/backend
```

Health check:
```bash
curl http://localhost:8000/health
```

Run tests and linters:
```bash
source .venv/bin/activate
ruff check services/backend
mypy services/backend/app
pytest -q services/backend/tests
```

## Docker

Build and run locally:
```bash
cp .env.example .env
docker compose up -d --build
```

## Security

- Non-root containers, minimal base image, `.dockerignore` to reduce context
- Secret management via environment variables (`.env.example` provided)
- CI includes static analysis and type checks

## Notes

- The backend includes a demo in-memory user `admin@local` with default password `changeit!` (dev only). Override `INITIAL_ADMIN_PASSWORD` in `.env` for local runs and set `SECRET_KEY` to a strong random value.
- Replace the in-memory store with a real database before production.
