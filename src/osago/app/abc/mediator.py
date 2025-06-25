from abc import abstractmethod
from typing import Any, Protocol, TypeVar

C = TypeVar("C")
RI = TypeVar("RI")


class BaseMediator(Protocol):
    @abstractmethod
    async def send(self, query) -> Any: ...
