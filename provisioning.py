# Mock Provisioning Module

_ACTIVE_USERS = set()

def provision_user(username: str) -> None:
    _ACTIVE_USERS.add(username)

def deprovision_user(username: str) -> None:
    _ACTIVE_USERS.discard(username)

def is_active(username: str) -> bool:
    return username in _ACTIVE_USERS
