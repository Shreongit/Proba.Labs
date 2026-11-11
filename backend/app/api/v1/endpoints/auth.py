from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import MessageResponse
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Authentication"])

user_service = UserService()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    data: UserCreate,
    db: Session = Depends(get_db),
) -> UserResponse:
    user = user_service.register_user(db, data)
    return UserResponse.model_validate(user)


@router.get("/status", response_model=MessageResponse)
def auth_status() -> MessageResponse:
    return MessageResponse(message="Authentication service operational.")