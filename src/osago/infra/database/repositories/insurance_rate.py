from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from osago.app.dto import InsuranceRateDTO
from osago.app.interfaces.repository import CoefficientInterface
from osago.infra.database.models import InsuranceRate

from .base import SQLAlchemyRepo


class InsuranceRateRepository(SQLAlchemyRepo, CoefficientInterface):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_all(self) -> list[InsuranceRateDTO]:
        stmt = select(InsuranceRate)
        raws = (await self.session.execute(stmt)).scalars().all()
        return [InsuranceRateDTO.model_validate(raw) for raw in raws]

    async def get_suitable(self, group_id: int) -> None | InsuranceRateDTO:
        stmt = select(InsuranceRate).filter(InsuranceRate.id == group_id)
        raw = (await self.session.execute(stmt)).scalars().first()
        if raw is None:
            return None
        return InsuranceRateDTO.model_validate(raw)
