from app.dto import TerritorialCoefficientDTO
from app.interfaces.repository import CoefficientInterface
from infra.database.models import TerritorialCoefficient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import SQLAlchemyRepo


class TerritorialCoefficientRepository(SQLAlchemyRepo, CoefficientInterface):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_all(self) -> list[TerritorialCoefficientDTO]:
        stmt = select(TerritorialCoefficient)
        raws = (await self.session.execute(stmt)).scalars().all()
        return [TerritorialCoefficientDTO.model_validate(raw) for raw in raws]

    async def get_suitable(
        self, region: int, city_name: str
    ) -> None | TerritorialCoefficientDTO:
        stmt = select(TerritorialCoefficient).filter(
            TerritorialCoefficient.region == region,
            TerritorialCoefficient.city_name.ilike(city_name),
        )
        raw = (await self.session.execute(stmt)).scalars().first()

        if raw is None:
            stmt = select(TerritorialCoefficient).filter(
                TerritorialCoefficient.region == region,
                TerritorialCoefficient.city_name == "Прочие города и населенные пункты",
            )
            raw = (await self.session.execute(stmt)).scalars().first()

        if raw is None:
            return None

        return TerritorialCoefficientDTO.model_validate(raw)
