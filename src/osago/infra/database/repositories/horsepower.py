from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from osago.app.dto import HorsepowerDTO
from osago.app.interfaces.repository import CoefficientInterface
from osago.infra.database.models import Horsepower

from .base import SQLAlchemyRepo


class HorsepowerRepository(SQLAlchemyRepo, CoefficientInterface):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_all(self) -> list[HorsepowerDTO]:
        stmt = select(Horsepower)
        raws = (await self.session.execute(stmt)).scalars().all()
        return [HorsepowerDTO.model_validate(raw) for raw in raws]

    async def get_suitable(self, max_horsepower: int) -> HorsepowerDTO:
        stmt = (
            select(Horsepower)
            .filter(Horsepower.max_horsepower >= max_horsepower)
            .order_by(Horsepower.max_horsepower)
        )
        raw = (await self.session.execute(stmt)).scalars().first()
        if raw is None:
            stmt = select(Horsepower).order_by(Horsepower.max_horsepower.desc())
            raw = (await self.session.execute(stmt)).scalars().first()
        return HorsepowerDTO.model_validate(raw)
