from app.abc import QueryHandler
from app.dto import HorsepowerDTO
from app.uow import UoWImpl
from pydantic import BaseModel


class GetSuitableHorsepowerQuery(BaseModel):
    max_horsepower: int


class GetSuitableHorsepowerQueryHandler(QueryHandler[GetSuitableHorsepowerQuery]):
    async def handle(
        self, query: GetSuitableHorsepowerQuery, uow: UoWImpl
    ) -> HorsepowerDTO:
        async with uow:
            horsepower = await uow.horsepower_repo.get_suitable(
                max_horsepower=query.max_horsepower
            )
            return horsepower
