from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import BonusMalusDTO
from osago.app.uow import UoWImpl


class GetAllBonusMalusQuery(BaseModel):
    pass


class GetAllBonusMalusQueryHandler(QueryHandler[GetAllBonusMalusQuery]):
    async def handle(
        self, query: GetAllBonusMalusQuery, uow: UoWImpl
    ) -> list[BonusMalusDTO]:
        async with uow:
            return await uow.bonus_malus_repo.get_all()
