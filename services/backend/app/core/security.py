from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List

from jose import jwt

from app.core.config import password_context, settings


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


def create_access_token(*, subject: str, roles: List[str] | None = None, expires_minutes: int | None = None) -> str:
    roles = roles or []
    expires_delta = timedelta(minutes=expires_minutes or settings.access_token_expires_minutes)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode: Dict[str, Any] = {"sub": subject, "roles": roles, "exp": expire}
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.jwt_algorithm)