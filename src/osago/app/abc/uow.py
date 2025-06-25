from abc import abstractmethod
from typing import Protocol, TypeVar
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


class HasID(Protocol):
    id: int | UUID


T = TypeVar("T", bound=HasID)


class BaseUoW(Protocol):
    @abstractmethod
    def __init__(self, session):
        pass

    @property
    def db_session(self) -> AsyncSession:
        pass

    @abstractmethod
    async def __aenter__(self) -> AsyncSession:
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass

    @abstractmethod
    async def flush_id(self, model: T) -> int | UUID:
        pass
