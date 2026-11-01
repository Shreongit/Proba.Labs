
from datetime import datetime, timedelta, timezone
from typing import Any

import bcrypt
from jose import JWTError, jwt

from app.core.config import settings

ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    password_bytes = password.encode("utf-8")

    if len(password_bytes) > 72:
        raise ValueError("Password cannot exceed 72 UTF-8 bytes.")

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a password against its stored bcrypt hash."""
    try:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        return False


def create_token(
    subject: str,
    token_type: str,
    expires_delta: timedelta,
) -> str:
    """Create a signed JWT."""
    now = datetime.now(timezone.utc)

    payload: dict[str, Any] = {
        "sub": subject,
        "type": token_type,
        "iat": now,
        "exp": now + expires_delta,
    }

    secret = settings.SECRET_KEY.get_secret_value()

    return jwt.encode(payload, secret, algorithm=ALGORITHM)


def create_access_token(subject: str) -> str:
    """Generate an access token."""
    return create_token(
        subject=subject,
        token_type="access",
        expires_delta=timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        ),
    )


def create_refresh_token(subject: str) -> str:
    """Generate a refresh token."""
    return create_token(
        subject=subject,
        token_type="refresh",
        expires_delta=timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS
        ),
    )


def verify_token(
    token: str,
    expected_type: str = "access",
) -> dict[str, Any] | None:
    """Verify a JWT and validate its token type."""
    try:
        secret = settings.SECRET_KEY.get_secret_value()

        payload = jwt.decode(
            token,
            secret,
            algorithms=[ALGORITHM],
        )

        if payload.get("type") != expected_type:
            return None

        if not payload.get("sub"):
            return None

        return payload

    except JWTError:
        return None
