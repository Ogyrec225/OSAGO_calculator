from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import BonusMalusDTO
from osago.app.uow import UoWImpl
from osago.domain.exceptions import NotFoundError


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
