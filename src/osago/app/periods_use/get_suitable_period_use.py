from app.abc import QueryHandler
from app.dto import PeriodUseDTO
from app.uow import UoWImpl
from domain.exceptions import NotFoundError
from pydantic import BaseModel


class GetSuitablePeriodsUseQuery(BaseModel):
    max_month: int


class GetSuitablePeriodsUseQueryHandler(QueryHandler[GetSuitablePeriodsUseQuery]):
    async def handle(
        self, query: GetSuitablePeriodsUseQuery, uow: UoWImpl
    ) -> PeriodUseDTO:
        async with uow:
            period_use = await uow.period_use_repo.get_suitable(
                max_month=query.max_month
            )

            if period_use is None:
                raise NotFoundError
            return period_use
