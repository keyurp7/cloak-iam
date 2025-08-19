# Mock SSO/Federation Module

_SSO_USERS = {
    "alice": {"id_token": "token_alice", "claims": {"role": "admin"}},
    "bob": {"id_token": "token_bob", "claims": {"role": "viewer"}}
}

def sso_login(username: str) -> str:
    """Simulate SSO login; returns id_token."""
    return _SSO_USERS.get(username, {}).get("id_token")

def validate_token(username: str, token: str) -> bool:
    """Check if the token matches the user."""
    return _SSO_USERS.get(username, {}).get("id_token") == token

def get_claims(username: str, token: str) -> dict:
    """Return token claims if valid, else empty dict."""
    if validate_token(username, token):
        return _SSO_USERS[username]["claims"]
    return {}
