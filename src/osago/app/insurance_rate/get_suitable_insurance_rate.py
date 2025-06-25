from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import InsuranceRateDTO
from osago.app.uow import UoWImpl
from osago.domain.exceptions import NotFoundError


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
