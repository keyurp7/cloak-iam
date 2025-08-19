# Keycloak SCIM Playbook
1. Run `docker-compose up -d`.
2. Install scim-for-keycloak plugin per docs (if required) or use Keycloak distribution with SCIM support.
3. Set SCIM_BASE and SCIM_TOKEN env vars.
4. Run `python client/scim_client.py` to create a user.
