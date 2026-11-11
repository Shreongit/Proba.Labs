from pydantic import EmailStr, Field

from app.schemas.common import BaseSchema


class LoginRequest(BaseSchema):
    """User login credentials."""

    email: EmailStr
    password: str = Field(min_length=1, max_length=72)


class TokenResponse(BaseSchema):
    """Authentication token response."""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseSchema):
    """Request to refresh an access token."""

    refresh_token: str = Field(min_length=1)


class MessageResponse(BaseSchema):
    """Generic success message."""

    message: str