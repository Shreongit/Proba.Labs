from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """Base schema with shared serialization settings."""

    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
        str_strip_whitespace=True,
    )


class TimestampSchema(BaseSchema):
    """Shared creation and update timestamps."""

    created_at: datetime
    updated_at: datetime