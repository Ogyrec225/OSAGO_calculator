from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import PeriodUseDTO
from osago.app.uow import UoWImpl


class GetAllPeriodsUseQuery(BaseModel):
    pass


class GetAllPeriodsUseQueryHandler(QueryHandler[GetAllPeriodsUseQuery]):
    async def handle(
        self, query: GetAllPeriodsUseQuery, uow: UoWImpl
    ) -> list[PeriodUseDTO]:
        async with uow:
            return await uow.period_use_repo.get_all()
