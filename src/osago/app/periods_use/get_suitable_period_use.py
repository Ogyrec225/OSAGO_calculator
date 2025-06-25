from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import PeriodUseDTO
from osago.app.uow import UoWImpl
from osago.domain.exceptions import NotFoundError


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
