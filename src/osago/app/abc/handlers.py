from typing import Any, Generic, Protocol, TypeVar

C = TypeVar("C")


class CommandHandler(Protocol, Generic[C]):
    async def handle(self, command: C, uow) -> Any: ...


class QueryHandler(Protocol, Generic[C]):
    async def handle(self, query: C, uow) -> Any: ...
