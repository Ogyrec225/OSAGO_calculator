from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import HorsepowerDTO
from osago.app.uow import UoWImpl


class GetAllHorsepowerQuery(BaseModel):
    pass


class GetAllHorsepowerQueryHandler(QueryHandler[GetAllHorsepowerQuery]):
    async def handle(
        self, query: GetAllHorsepowerQuery, uow: UoWImpl
    ) -> list[HorsepowerDTO]:
        async with uow:
            return await uow.horsepower_repo.get_all()
