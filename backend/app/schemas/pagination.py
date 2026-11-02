from typing import Generic, TypeVar

from pydantic import Field

from app.schemas.common import BaseSchema

T = TypeVar("T")


class PaginationParams(BaseSchema):
    """Standard pagination parameters for API requests."""

    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size


class PaginatedResponse(BaseSchema, Generic[T]):
    """Generic paginated API response."""

    items: list[T]
    total: int = Field(ge=0)
    page: int = Field(ge=1)
    page_size: int = Field(ge=1)
    total_pages: int = Field(ge=0)
    has_next: bool
    has_previous: bool