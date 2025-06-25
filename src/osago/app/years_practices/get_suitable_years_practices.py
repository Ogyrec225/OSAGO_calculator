from app.abc import QueryHandler
from app.dto import YearsPracticeDTO
from app.uow import UoWImpl
from domain.exceptions import NotFoundError
from pydantic import BaseModel


class GetSuitableYearsPracticesQuery(BaseModel):
    max_years: int
    max_practice: int


class GetSuitableYearsPracticesQueryHandler(
    QueryHandler[GetSuitableYearsPracticesQuery]
):
    async def handle(
        self, query: GetSuitableYearsPracticesQuery, uow: UoWImpl
    ) -> YearsPracticeDTO:
        async with uow:
            years_practice = await uow.years_practice_repo.get_suitable(
                max_years=query.max_years, max_practice=query.max_practice
            )

            if years_practice is None:
                raise NotFoundError
            return years_practice
