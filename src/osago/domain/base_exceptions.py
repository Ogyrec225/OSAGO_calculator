from dataclasses import dataclass
from typing import ClassVar

from fastapi import status


@dataclass(eq=False)
class AppError(Exception):
    """Base Error."""

    status: ClassVar[int] = status.HTTP_500_INTERNAL_SERVER_ERROR

    @property
    def type(self) -> str:
        return self.__class__.__name__

    @property
    def title(self) -> str:
        return "An app error occurred"


@dataclass(eq=False)
class DomainError(AppError):
    """Base Domain Error."""

    status: ClassVar[int] = status.HTTP_400_BAD_REQUEST

    @property
    def title(self) -> str:
        return "A domain error occurred"


@dataclass(eq=False)
class ApplicationError(AppError):
    """Base Application Exception."""

    status: ClassVar[int] = status.HTTP_404_NOT_FOUND

    @property
    def title(self) -> str:
        return "An application error occurred"
