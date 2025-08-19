# Mock Authorization Module

_ROLE_ACCESS = {
    "alice": ["admin_panel", "dashboard"],
    "bob": ["dashboard"]
}

def check_access(username: str, resource: str) -> bool:
    return resource in _ROLE_ACCESS.get(username, [])
