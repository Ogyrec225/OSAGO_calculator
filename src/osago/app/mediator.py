from contextlib import AbstractAsyncContextManager

from osago.app.abc import BaseMediator
from osago.app.abc.handlers import CommandHandler, QueryHandler
from osago.app.abc.uow import BaseUoW


class MediatorImpl(BaseMediator):
    def __init__(
        self,
        uow_factory: AbstractAsyncContextManager[BaseUoW],
        handlers: dict[type, CommandHandler | QueryHandler],
    ):
        self.uow_factory = uow_factory
        self.handlers = handlers

    async def send(self, query):
        handler: CommandHandler | QueryHandler | None = self.handlers.get(type(query))
        if handler is None:
            raise ValueError(f"Handler for query/command: {query} wasn't found")
        result = await handler.handle(query, self.uow_factory)

        return result
