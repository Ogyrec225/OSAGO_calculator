from abc import ABC, abstractmethod
from typing import Any, TypeVar

from app.dto import DTO

T = TypeVar("T", DTO, None)


class CoefficientInterface(ABC):
    @abstractmethod
    async def get_all(self) -> T:
        raise NotImplementedError

    @abstractmethod
    async def get_suitable(self, col: Any, val: Any) -> T:
        raise NotImplementedError
