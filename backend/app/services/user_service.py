from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import ResourceConflictException
from app.core.security import hash_password
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate


class UserService:
    """Business logic for user account operations."""

    def __init__(self, repository: type[UserRepository] = UserRepository):
        self.repository = repository

    def register_user(self, db: Session, data: UserCreate):
        email = str(data.email).lower()

        existing_user = self.repository.get_by_email(db, email)

        if existing_user:
            raise ResourceConflictException(
                "An account with this email already exists."
            )

        hashed_password = hash_password(data.password)

        try:
            user = self.repository.create(
                db,
                email=email,
                hashed_password=hashed_password,
                full_name=data.full_name,
            )
            db.commit()
            db.refresh(user)
            return user

        except IntegrityError as exc:
            db.rollback()
            raise ResourceConflictException(
                "An account with this email already exists."
            ) from exc