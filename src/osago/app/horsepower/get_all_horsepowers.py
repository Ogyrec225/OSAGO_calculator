from app.abc import QueryHandler
from app.dto import HorsepowerDTO
from app.uow import UoWImpl
from pydantic import BaseModel


class GetAllHorsepowerQuery(BaseModel):
    pass


class GetAllHorsepowerQueryHandler(QueryHandler[GetAllHorsepowerQuery]):
    async def handle(
        self, query: GetAllHorsepowerQuery, uow: UoWImpl
    ) -> list[HorsepowerDTO]:
        async with uow:
            return await uow.horsepower_repo.get_all()
