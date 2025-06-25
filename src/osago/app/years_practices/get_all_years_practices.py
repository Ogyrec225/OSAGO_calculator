from app.abc import QueryHandler
from app.dto import YearsPracticeDTO
from app.uow import UoWImpl
from pydantic import BaseModel


class GetAllYearsPracticesQuery(BaseModel):
    pass


class GetAllYearsPracticesQueryHandler(QueryHandler[GetAllYearsPracticesQuery]):
    async def handle(
        self, query: GetAllYearsPracticesQuery, uow: UoWImpl
    ) -> list[YearsPracticeDTO]:
        async with uow:
            return await uow.years_practice_repo.get_all()
