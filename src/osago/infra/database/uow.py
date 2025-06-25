from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from osago.app.abc.uow import BaseUoW, HasID


class SQLAlchemyUoW(BaseUoW):
    def __init__(self, session: AsyncSession):
        self._db_session = session

    @property
    def db_session(self) -> AsyncSession:
        if self._db_session is None:
            raise ValueError("Session is only available within the 'async with' block.")
        return self._db_session

    async def __aenter__(self):
        self._db_session: AsyncSession = self._db_session()
        return self._db_session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                await self.commit()
            else:
                await self.rollback()
        finally:
            await self._db_session.close()

    async def commit(self):
        await self._db_session.commit()

    async def rollback(self):
        await self._db_session.rollback()

    async def flush_id(self, model: HasID) -> int | UUID:
        await self._db_session.flush([model])
        return model.id
