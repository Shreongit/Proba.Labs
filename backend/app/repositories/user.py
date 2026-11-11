from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """Database operations for user accounts."""

    @staticmethod
    def get_by_id(db: Session, user_id: UUID) -> User | None:
        return db.get(User, user_id)

    @staticmethod
    def get_by_email(db: Session, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return db.scalar(statement)

    @staticmethod
    def create(
        db: Session,
        *,
        email: str,
        hashed_password: str,
        full_name: str,
    ) -> User:
        user = User(
            email=email,
            hashed_password=hashed_password,
            full_name=full_name,
        )

        db.add(user)
        db.flush()
        db.refresh(user)

        return user