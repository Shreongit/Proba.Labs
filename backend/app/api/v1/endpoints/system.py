from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["System"])
async def api_health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "proba-labs-api",
        "api_version": "v1",
    }