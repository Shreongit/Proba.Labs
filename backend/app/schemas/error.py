from pydantic import Field

from app.schemas.common import BaseSchema


class ErrorDetail(BaseSchema):
    """Standard API error details."""

    message: str
    details: dict[str, object] = Field(default_factory=dict)
    path: str | None = None


class ErrorResponse(BaseSchema):
    """Consistent API error response envelope."""

    error: ErrorDetail