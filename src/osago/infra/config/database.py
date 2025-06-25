from pydantic import Field, computed_field
from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    db_host: str = Field(validation_alias="DB_HOST", default="localhost")
    db_port: int = Field(validation_alias="DB_PORT", default=5432)
    db_user: str = Field(validation_alias="DB_USER")
    db_password: str = Field(validation_alias="DB_PASSWORD")
    db_name: str = Field(validation_alias="DB_NAME")
    db_echo: bool = False

    @computed_field(return_type=str)
    @property
    def db_dsn(self):
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
            + f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )
