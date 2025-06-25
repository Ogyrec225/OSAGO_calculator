from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from osago.app.dto import PeriodInsuranceDTO
from osago.app.interfaces.repository import CoefficientInterface
from osago.infra.database.models import PeriodInsurance

from .base import SQLAlchemyRepo


class PeriodInsuranceRepository(SQLAlchemyRepo, CoefficientInterface):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_all(self) -> list[PeriodInsuranceDTO]:
        stmt = select(PeriodInsurance)
        raws = (await self.session.execute(stmt)).scalars().all()
        return [PeriodInsuranceDTO.model_validate(raw) for raw in raws]

    async def get_suitable(self, max_month: int) -> PeriodInsuranceDTO:
        stmt = (
            select(PeriodInsurance)
            .filter(PeriodInsurance.max_month >= max_month)
            .order_by(PeriodInsurance.max_month)
        )
        raw = (await self.session.execute(stmt)).scalars().first()
        if raw is None:
            stmt = select(PeriodInsurance).order_by(PeriodInsurance.max_month.desc())
            raw = (await self.session.execute(stmt)).scalars().first()

        return PeriodInsuranceDTO.model_validate(raw)
