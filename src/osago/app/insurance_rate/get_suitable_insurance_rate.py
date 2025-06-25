from app.abc import QueryHandler
from app.dto import InsuranceRateDTO
from app.uow import UoWImpl
from domain.exceptions import NotFoundError
from pydantic import BaseModel


class GetSuitableInsuranceRatesQuery(BaseModel):
    group_id: int


class GetSuitableInsuranceRatesQueryHandler(
    QueryHandler[GetSuitableInsuranceRatesQuery]
):
    async def handle(
        self, query: GetSuitableInsuranceRatesQuery, uow: UoWImpl
    ) -> InsuranceRateDTO:
        async with uow:
            insurance_rate = await uow.insurance_rate_repo.get_suitable(
                group_id=query.group_id
            )

            if insurance_rate is None:
                raise NotFoundError
            return insurance_rate
