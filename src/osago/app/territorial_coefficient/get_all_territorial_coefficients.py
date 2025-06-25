from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import TerritorialCoefficientDTO
from osago.app.uow import UoWImpl


class GetAllTerritorialCoefficientQuery(BaseModel):
    pass


class GetAllTerritorialCoefficientQueryHandler(
    QueryHandler[GetAllTerritorialCoefficientQuery]
):
    async def handle(
        self, query: GetAllTerritorialCoefficientQuery, uow: UoWImpl
    ) -> list[TerritorialCoefficientDTO]:
        async with uow:
            return await uow.territorial_coefficient_repo.get_all()
