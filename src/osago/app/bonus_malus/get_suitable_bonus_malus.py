from app.abc import QueryHandler
from app.dto import BonusMalusDTO
from app.uow import UoWImpl
from domain.exceptions import NotFoundError
from pydantic import BaseModel


class GetSuitableBonusMalusQuery(BaseModel):
    kbm_class: int


class GetSuitableBonusMalusQueryHandler(QueryHandler[GetSuitableBonusMalusQuery]):
    async def handle(
        self, query: GetSuitableBonusMalusQuery, uow: UoWImpl
    ) -> BonusMalusDTO:
        async with uow:
            bonus_malus = await uow.bonus_malus_repo.get_suitable(
                kbm_class=query.kbm_class
            )

            if bonus_malus is None:
                raise NotFoundError
            return bonus_malus
