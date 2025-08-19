# Mock Authentication Module

_USERS = {
    "alice": "correct_password",
    "bob": "viewer_password"
}

_MFA_TOKENS = {}

def authenticate_user(username: str, password: str) -> bool:
    return _USERS.get(username) == password

def generate_mfa_token(username: str) -> str:
    token = "123456"  # mock static token
    _MFA_TOKENS[username] = token
    return token

def verify_mfa_token(username: str, token: str) -> bool:
    return _MFA_TOKENS.get(username) == token
