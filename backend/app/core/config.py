
from functools import lru_cache
from typing import Literal

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration for the Proba Labs application.

    Values are loaded from environment variables or the .env file.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    APP_NAME: str = "Proba Labs"
    APP_VERSION: str = "0.1.0"
    APP_ENV: Literal["development", "testing", "staging", "production"] = (
        "development"
    )
    DEBUG: bool = True

    # API
    API_V1_PREFIX: str = "/api/v1"

    # Security
    SECRET_KEY: SecretStr = Field(
        default=SecretStr("development-only-change-this-secret"),
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, gt=0)
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7, gt=0)

    # Database
    DATABASE_URL: SecretStr = SecretStr(
        "postgresql+psycopg://postgres:postgres@localhost:5432/proba_labs"
    )

    # Redis
    REDIS_URL: SecretStr = SecretStr("redis://localhost:6379/0")

    # Celery
    CELERY_BROKER_URL: SecretStr = SecretStr(
        "redis://localhost:6379/1"
    )
    CELERY_RESULT_BACKEND: SecretStr = SecretStr(
        "redis://localhost:6379/2"
    )

    # Object storage
    STORAGE_ENDPOINT_URL: str = "http://localhost:9000"
    STORAGE_BUCKET: str = "proba-labs"
    STORAGE_ACCESS_KEY: SecretStr = SecretStr("minioadmin")
    STORAGE_SECRET_KEY: SecretStr = SecretStr("minioadmin")
    STORAGE_REGION: str = "us-east-1"

    # Upload restrictions
    MAX_UPLOAD_SIZE_MB: int = Field(default=100, gt=0)
    ALLOWED_MODEL_EXTENSIONS: list[str] = [
        ".onnx",
        ".joblib",
        ".safetensors",
    ]
    ALLOWED_DATASET_EXTENSIONS: list[str] = [
        ".csv",
        ".parquet",
    ]

    # CORS
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    # Logging
    LOG_LEVEL: str = "INFO"

    @property
    def is_development(self) -> bool:
        return self.APP_ENV == "development"

    @property
    def is_production(self) -> bool:
        return self.APP_ENV == "production"


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached application settings instance.
    """
    return Settings()


settings = get_settings()
