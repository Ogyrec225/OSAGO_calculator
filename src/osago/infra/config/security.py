from pydantic import Field, computed_field
from pydantic_settings import BaseSettings


class SecuritySettings(BaseSettings):
    cors_origins_str: str = Field(validation_alias="CORS_ORIGINS", default="localhost")

    @computed_field
    @property
    def cors_origins(self) -> list[str]:
        return self.cors_origins_str.split()

    cors_allow_methods: list[str] = ["GET", "POST", "PATCH", "PUT", "DELETE"]
    cors_allow_headers: list[str] = [
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ]
    expose_headers: list[str] = ["Content-Disposition"]
