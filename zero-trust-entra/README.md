# Zero Trust Demo — Entra (Azure AD) + Flask OIDC (Commit-ready)

## Contents
- `app/` — Flask sample app using MSAL for OIDC login and claim-based access control.
- `infra/` — Terraform example to register app and create resources in Azure (skeleton).
- `.github/workflows/ci.yml` — GitHub Actions to run lint/tests.
- `scripts/register_app.sh` — MS Graph / Azure CLI scripted steps to register app (manual/automated).
- `demo-playbook.md` — Steps to run locally and in Azure.

## Quick start (local)
1. Create a Python virtualenv and install requirements: `pip install -r app/requirements.txt`
2. Register an app in your Entra tenant and set redirect URI to `http://localhost:8080/getAToken`.
3. Set env vars: `CLIENT_ID`, `TENANT_ID`, `CLIENT_SECRET`, `FLASK_SECRET`.
4. Run: `python app/app.py` and visit `http://localhost:8080`.

## Notes
- The `scripts/register_app.sh` provides CLI commands using `az` to help automate registration.
