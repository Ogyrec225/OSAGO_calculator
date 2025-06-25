from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import YearsPracticeDTO
from osago.app.uow import UoWImpl


class GetAllYearsPracticesQuery(BaseModel):
    pass


class GetAllYearsPracticesQueryHandler(QueryHandler[GetAllYearsPracticesQuery]):
    async def handle(
        self, query: GetAllYearsPracticesQuery, uow: UoWImpl
    ) -> list[YearsPracticeDTO]:
        async with uow:
            return await uow.years_practice_repo.get_all()
