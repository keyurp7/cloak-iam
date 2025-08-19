# IAM Specialist Website

Professional, responsive one-page portfolio tailored for Identity & Access Management specialists.

## Quick start

- Open `index.html` in a browser, or run a simple server:

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.

## Customize

Two easy options:

1) Edit content inline in `index.html` (headings, sections, links)
2) Preferably, edit `assets/resume.json`. The site auto-hydrates name, summary, skills, experience, certifications, projects, and links.

Fields supported in `assets/resume.json`:

```json
{
  "basics": {
    "name": "YOUR NAME",
    "email": "you@example.com",
    "website": "https://example.com",
    "summary": "...",
    "profiles": [
      { "network": "LinkedIn", "username": "your-handle", "url": "https://www.linkedin.com/in/your-handle" },
      { "network": "GitHub", "username": "your-handle", "url": "https://github.com/your-handle" }
    ]
  },
  "stats": { "yearsInIam": "8+", "clouds": ["AWS","Azure","GCP"], "certs": ["CISSP"] },
  "skills": ["Zero Trust", "PAM"],
  "work": [ { "name": "Company", "position": "Role", "startDate": "2021", "endDate": "Present", "highlights": ["Achievement"] } ],
  "certifications": ["CISSP"],
  "projects": [ { "name": "Project", "summary": "...", "url": "https://..." } ],
  "writing": [ { "title": "Post title", "url": "https://..." } ]
}
```

To update the resume PDF, replace `assets/resume.pdf` and the hero download button will use it automatically.

## Theming

- Automatic dark/light based on system; toggle via the moon button
- Colors set via CSS variables in `assets/styles.css`

## Deploy

- GitHub Pages: push this folder; set Pages source to the root
- Netlify: drag-and-drop the folder or `netlify deploy`
- Cloudflare Pages or Vercel: static output, no build step needed

## Accessibility & SEO

- Semantic headings, landmarks, and skip link
- High contrast colors; reduced motion friendly
- JSON-LD Person schema in `index.html`


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
