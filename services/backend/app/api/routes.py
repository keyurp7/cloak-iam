from typing import Dict, List, TypedDict

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.core.config import settings
from app.core.security import create_access_token, verify_password


class UserRecord(TypedDict):
    username: str
    full_name: str
    hashed_password: str
    roles: List[str]


api_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Demo in-memory user store for scaffolding. Replace with DB later.
_FAKE_USER_DB: Dict[str, UserRecord] = {
    "admin@local": {
        "username": "admin@local",
        "full_name": "Administrator",
        "hashed_password": str(settings.initial_admin_hashed_password or ""),
        "roles": ["admin"],
    },
}


@api_router.post("/auth/token", response_model=Token, tags=["auth"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = _FAKE_USER_DB.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    token = create_access_token(subject=user["username"], roles=user["roles"])    
    return Token(access_token=token)


@api_router.get("/me", tags=["users"])
async def read_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = settings.jwt_decode(token)
    return {"sub": payload.get("sub"), "roles": payload.get("roles", [])}