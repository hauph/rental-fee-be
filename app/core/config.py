import os
from typing import Any, Dict, List, Optional, Union

from dotenv import load_dotenv
from pydantic import Field, PostgresDsn, field_validator
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    BACKEND_CORS_ORIGINS: list[Any] = Field(
        default_factory=lambda: os.getenv("ALLOW_ORIGINS", "").split(",")
    )

    PROJECT_NAME: str = "Rental Monthly Fee Calculator"

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: Optional[str] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_DB: Optional[str] = None
    SQLALCHEMY_DATABASE_URI: Optional[Union[PostgresDsn, str]] = None

    @field_validator(
        "POSTGRES_SERVER",
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_DB",
        mode="before",
    )
    @classmethod
    def postgres_validation(cls, v: Optional[str], **kwargs):
        if v is None:
            field_name = kwargs["info"].name if "info" in kwargs else "Unknown field"
            raise ValueError(f"{field_name} must be set when not in debug mode.")
        return v

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return str(
            PostgresDsn.build(
                scheme="postgresql",
                username=values.data.get("POSTGRES_USER"),
                password=values.data.get("POSTGRES_PASSWORD"),
                host=values.data.get("POSTGRES_SERVER"),
                path=f"{values.data.get('POSTGRES_DB') or ''}",
            )
        )

    class Config:
        case_sensitive = True


settings = Settings()
