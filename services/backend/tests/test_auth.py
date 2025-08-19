from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_and_me():
    # default setup uses INITIAL_ADMIN_PASSWORD=changeit!
    response = client.post(
        "/api/auth/token",
        data={"username": "admin@local", "password": "changeit!"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == HTTPStatus.OK, response.text
    token = response.json()["access_token"]

    me = client.get("/api/me", headers={"Authorization": f"Bearer {token}"})
    assert me.status_code == HTTPStatus.OK, me.text
    body = me.json()
    assert body["sub"] == "admin@local"
    assert "admin" in body["roles"]