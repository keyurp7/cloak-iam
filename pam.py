# Mock Privileged Access Module

_ACTIVE_PAM_SESSIONS = {}

def request_elevation(username: str) -> str:
    """Simulate a PAM elevation request."""
    session_id = f"{username}_session"
    _ACTIVE_PAM_SESSIONS[username] = session_id
    return session_id

def end_elevation(username: str) -> None:
    """Revoke PAM access."""
    _ACTIVE_PAM_SESSIONS.pop(username, None)

def get_active_session(username: str) -> str:
    """Return current active session for user, if any."""
    return _ACTIVE_PAM_SESSIONS.get(username)
