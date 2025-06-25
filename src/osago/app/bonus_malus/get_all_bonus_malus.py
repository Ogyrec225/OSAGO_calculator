from app.abc import QueryHandler
from app.dto import BonusMalusDTO
from app.uow import UoWImpl
from pydantic import BaseModel


class GetAllBonusMalusQuery(BaseModel):
    pass


class GetAllBonusMalusQueryHandler(QueryHandler[GetAllBonusMalusQuery]):
    async def handle(
        self, query: GetAllBonusMalusQuery, uow: UoWImpl
    ) -> list[BonusMalusDTO]:
        async with uow:
            return await uow.bonus_malus_repo.get_all()
