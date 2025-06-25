from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from osago.app.dto import BonusMalusDTO
from osago.app.interfaces.repository import CoefficientInterface
from osago.infra.database.models import BonusMalus

from .base import SQLAlchemyRepo


class BonusMalusRepository(SQLAlchemyRepo, CoefficientInterface):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_all(self) -> list[BonusMalusDTO]:
        stmt = select(BonusMalus)
        raws = (await self.session.execute(stmt)).scalars().all()
        return [BonusMalusDTO.model_validate(raw) for raw in raws]

    async def get_suitable(self, kbm_class: int) -> None | BonusMalusDTO:
        stmt = select(BonusMalus).filter(BonusMalus.kbm_class == kbm_class)
        raw = (await self.session.execute(stmt)).scalars().first()

        if raw is None:
            stmt = select(BonusMalus).order_by(BonusMalus.coefficient.desc())
            raw = (await self.session.execute(stmt)).scalars().first()
        return BonusMalusDTO.model_validate(raw)
