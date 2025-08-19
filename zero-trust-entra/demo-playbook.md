# Zero Trust Entra Demo — Playbook
1. Register app or run scripts/register_app.sh to create app registration.
2. Set env vars: CLIENT_ID, CLIENT_SECRET, TENANT_ID, FLASK_SECRET.
3. Install deps: pip install -r app/requirements.txt
4. Run: python app/app.py
5. Sign in via Entra, inspect claims and test protected endpoint behaviors.
