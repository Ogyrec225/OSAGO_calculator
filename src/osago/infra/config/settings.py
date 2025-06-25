import sys
from enum import Enum

from dotenv import load_dotenv
from loguru import logger
from pydantic import Field

from .database import PostgresSettings
from .security import SecuritySettings


class ModeType(str, Enum):
    DEPLOY = "DEPLOY"
    DEBUG = "DEBUG"
    TEST = "TEST"


class Settings(SecuritySettings, PostgresSettings):
    host: str = Field(validation_alias="HOST", default="127.0.0.1")
    domain: str = Field(validation_alias="DOMAIN", default="127.0.0.1")
    port: int = Field(validation_alias="PORT", default=5100)
    mode: ModeType = Field(validation_alias="MODE", default=ModeType.DEPLOY)

    docs_url: None | str = None
    redoc_url: None | str = None

    date_format: str = "%d.%m.%Y"
    date_time_format: str = "%d.%m.%Y %H:%M:%S"
    time_format: str = "%H:%M:%S"

    def __init__(self, **data):
        super().__init__(**data)
        if self.mode == ModeType.DEBUG:
            self.docs_url = "/docs"
            self.redoc_url = "/redoc"
            self.db_echo = True


def _generate() -> Settings:
    """Generate settings of app."""
    load_dotenv(override=True)
    try:
        settings = Settings()
        return settings
    except Exception as e:
        logger.critical(f"Settings generated with error: {e}")
        sys.exit()


settings = _generate()
