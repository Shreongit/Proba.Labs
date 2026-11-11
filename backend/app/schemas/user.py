from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, Field

from app.schemas.common import BaseSchema


class UserCreate(BaseSchema):
    """Schema for user registration."""

    email: EmailStr
    password: str = Field(min_length=12, max_length=72)
    full_name: str = Field(min_length=2, max_length=100)


class UserResponse(BaseSchema):
    """Public user information."""

    id: UUID
    email: EmailStr
    full_name: str
    is_active: bool
    is_verified: bool
    created_at: datetime


class UserUpdate(BaseSchema):
    """Schema for updating user profile information."""

    full_name: str | None = Field(default=None, min_length=2, max_length=100)