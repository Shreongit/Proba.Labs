
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import ProbaLabsException


def register_exception_handlers(app: FastAPI) -> None:
    """Register centralized application exception handlers."""

    @app.exception_handler(ProbaLabsException)
    async def handle_proba_exception(
        request: Request,
        exc: ProbaLabsException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "message": exc.message,
                    "details": exc.details,
                    "path": request.url.path,
                }
            },
        )

    @app.exception_handler(Exception)
    async def handle_unexpected_exception(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "message": "An unexpected internal server error occurred.",
                    "path": request.url.path,
                }
            },
        )
