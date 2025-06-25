from app.abc import QueryHandler
from app.dto import TerritorialCoefficientDTO
from app.uow import UoWImpl
from domain.exceptions import NotFoundError
from pydantic import BaseModel


class GetSuitableTerritorialCoefficientQuery(BaseModel):
    region: int
    city_name: str


class GetSuitableTerritorialCoefficientQueryHandler(
    QueryHandler[GetSuitableTerritorialCoefficientQuery]
):
    async def handle(
        self, query: GetSuitableTerritorialCoefficientQuery, uow: UoWImpl
    ) -> TerritorialCoefficientDTO:
        async with uow:
            territorial_coefficient = (
                await uow.territorial_coefficient_repo.get_suitable(
                    region=query.region, city_name=query.city_name
                )
            )
            if territorial_coefficient is None:
                raise NotFoundError
            return territorial_coefficient
