from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import PeriodInsuranceDTO
from osago.app.uow import UoWImpl


class GetSuitablePeriodInsuranceQuery(BaseModel):
    max_month: int


class GetSuitablePeriodInsuranceQueryHandler(
    QueryHandler[GetSuitablePeriodInsuranceQuery]
):
    async def handle(
        self, query: GetSuitablePeriodInsuranceQuery, uow: UoWImpl
    ) -> PeriodInsuranceDTO:
        async with uow:
            insurance_period = await uow.period_insurance_repo.get_suitable(
                max_month=query.max_month
            )
            return insurance_period
