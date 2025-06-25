from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import HorsepowerDTO
from osago.app.uow import UoWImpl


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
