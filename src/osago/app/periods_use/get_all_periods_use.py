from app.abc import QueryHandler
from app.dto import PeriodUseDTO
from app.uow import UoWImpl
from pydantic import BaseModel


class GetAllPeriodsUseQuery(BaseModel):
    pass


class GetAllPeriodsUseQueryHandler(QueryHandler[GetAllPeriodsUseQuery]):
    async def handle(
        self, query: GetAllPeriodsUseQuery, uow: UoWImpl
    ) -> list[PeriodUseDTO]:
        async with uow:
            return await uow.period_use_repo.get_all()
