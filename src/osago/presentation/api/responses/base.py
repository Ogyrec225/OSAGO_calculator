from dataclasses import dataclass, field
from datetime import datetime
from typing import Generic, TypeVar
from uuid import UUID

TResult = TypeVar("TResult")
TError = TypeVar("TError")


@dataclass(frozen=True)
class Response:
    pass


@dataclass(frozen=True)
class CreatedResponse(Response, Generic[TResult]):
    id: int | UUID
    status: int = 201


@dataclass(frozen=True)
class OkResponse(Response, Generic[TResult]):
    status: int = 200
    result: TResult | None = None


@dataclass(frozen=True)
class NoContentResponse(Response):
    status: int = 204


@dataclass(frozen=True)
class ErrorData(Generic[TError]):
    detail: str = "Unknown error occurred"
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    type: str | None = None


@dataclass(frozen=True)
class ErrorResponse(Response, Generic[TError]):
    status: int = 500
    error: ErrorData[TError] = field(default_factory=ErrorData)
