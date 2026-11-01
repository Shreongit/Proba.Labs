
from typing import Any


class ProbaLabsException(Exception):
    """Base exception for all Proba Labs application errors."""

    def __init__(
        self,
        message: str,
        status_code: int = 500,
        details: dict[str, Any] | None = None,
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.details = details or {}

        super().__init__(message)


class ResourceNotFoundException(ProbaLabsException):
    """Raised when a requested resource does not exist."""

    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(message, status_code=404)


class ResourceConflictException(ProbaLabsException):
    """Raised when a resource conflicts with existing data."""

    def __init__(self, message: str = "Resource already exists") -> None:
        super().__init__(message, status_code=409)


class ValidationException(ProbaLabsException):
    """Raised when application-level validation fails."""

    def __init__(
        self,
        message: str = "Validation failed",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, status_code=422, details=details)


class PermissionDeniedException(ProbaLabsException):
    """Raised when a user lacks permission to perform an action."""

    def __init__(self, message: str = "Permission denied") -> None:
        super().__init__(message, status_code=403)
