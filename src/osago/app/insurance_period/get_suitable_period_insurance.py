from app.abc import QueryHandler
from app.dto import PeriodInsuranceDTO
from app.uow import UoWImpl
from pydantic import BaseModel


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
