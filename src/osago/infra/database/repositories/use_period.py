from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from osago.app.dto import PeriodUseDTO
from osago.app.interfaces.repository import CoefficientInterface
from osago.infra.database.models import PeriodUse

from .base import SQLAlchemyRepo


class UsePeriodRepository(SQLAlchemyRepo, CoefficientInterface):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_all(self) -> list[PeriodUseDTO]:
        stmt = select(PeriodUse)
        raws = (await self.session.execute(stmt)).scalars().all()
        return [PeriodUseDTO.model_validate(raw) for raw in raws]

    async def get_suitable(
        self,
        max_month: int,
    ) -> None | PeriodUseDTO:
        stmt = select(PeriodUse).filter(PeriodUse.max_month >= max_month)
        raw = (await self.session.execute(stmt)).scalars().first()
        if raw is None:
            stmt = select(PeriodUse).order_by(PeriodUse.max_month.desc())
            raw = (await self.session.execute(stmt)).scalars().first()

        return PeriodUseDTO.model_validate(raw)
