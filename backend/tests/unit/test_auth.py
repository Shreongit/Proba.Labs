from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_auth_status() -> None:
    response = client.get("/api/v1/auth/status")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Authentication service operational."
    }


def test_register_rejects_invalid_email() -> None:
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "invalid-email",
            "password": "StrongPassword123!",
            "full_name": "Test User",
        },
    )

    assert response.status_code == 422


def test_register_rejects_short_password() -> None:
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "password": "short",
            "full_name": "Test User",
        },
    )

    assert response.status_code == 422