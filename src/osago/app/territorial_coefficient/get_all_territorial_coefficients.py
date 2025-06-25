from app.abc import QueryHandler
from app.dto import TerritorialCoefficientDTO
from app.uow import UoWImpl
from pydantic import BaseModel


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
