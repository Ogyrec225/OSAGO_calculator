from app.dto import RestrictionCoefficientDTO
from app.interfaces.repository import CoefficientInterface
from infra.database.models import RestrictionCoefficient
from infra.static.types import OwnerType
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import SQLAlchemyRepo


class RestrictionCoefficientRepository(SQLAlchemyRepo, CoefficientInterface):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_all(self) -> list[RestrictionCoefficientDTO]:
        stmt = select(RestrictionCoefficient)
        raws = (await self.session.execute(stmt)).scalars().all()
        return [RestrictionCoefficientDTO.model_validate(raw) for raw in raws]

    async def get_suitable(
        self, owner_type: OwnerType, limitation_flag: bool
    ) -> RestrictionCoefficientDTO:
        stmt = (
            select(RestrictionCoefficient)
            .filter(
                RestrictionCoefficient.owner_type == owner_type,
                RestrictionCoefficient.limitation_flag == limitation_flag,
            )
            .order_by(RestrictionCoefficient.coefficient.desc())
        )
        raw = (await self.session.execute(stmt)).scalars().first()
        if raw is None:
            stmt = select(RestrictionCoefficient).filter(
                RestrictionCoefficient.coefficient == 1
            )
            raw = (await self.session.execute(stmt)).scalars().first()

        return RestrictionCoefficientDTO.model_validate(raw)
