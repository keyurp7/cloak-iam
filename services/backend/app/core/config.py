import os
from functools import lru_cache
from typing import Any, Dict, List

from jose import jwt
from passlib.context import CryptContext
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CLOAK Backend"
    secret_key: str = "dev-secret-key-change-me"
    access_token_expires_minutes: int = 60
    jwt_algorithm: str = "HS256"

    cors_allow_origins: List[str] = ["*"]

    # Generated at first run for demo admin default password "changeit!" unless overridden
    initial_admin_hashed_password: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    def jwt_decode(self, token: str) -> Dict[str, Any]:
        return jwt.decode(token, self.secret_key, algorithms=[self.jwt_algorithm])


@lru_cache

def get_settings() -> Settings:
    return Settings()


settings = get_settings()

# Initialize password hasher and default admin password hash
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
if settings.initial_admin_hashed_password is None:
    settings.initial_admin_hashed_password = password_context.hash(
        os.getenv("INITIAL_ADMIN_PASSWORD", "changeit!")
    )