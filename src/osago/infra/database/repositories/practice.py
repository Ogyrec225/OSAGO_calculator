from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from osago.app.dto import YearsPracticeDTO
from osago.app.interfaces.repository import CoefficientInterface
from osago.infra.database.models import YearsPractice

from .base import SQLAlchemyRepo


class YearsPracticeRepository(SQLAlchemyRepo, CoefficientInterface):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_all(self) -> list[YearsPracticeDTO]:
        stmt = select(YearsPractice)
        raws = (await self.session.execute(stmt)).scalars().all()
        return [YearsPracticeDTO.model_validate(raw) for raw in raws]

    async def get_suitable(self, max_years: int, max_practice: int) -> YearsPracticeDTO:
        stmt = (
            select(YearsPractice)
            .filter(
                YearsPractice.max_years >= max_years,
                YearsPractice.max_practice >= max_practice,
            )
            .order_by(YearsPractice.max_years)
        )
        raw = (await self.session.execute(stmt)).scalars().first()
        if raw is None:
            stmt = select(YearsPractice).order_by(YearsPractice.coefficient)
            raw = (await self.session.execute(stmt)).scalars().first()

        return YearsPracticeDTO.model_validate(raw)
