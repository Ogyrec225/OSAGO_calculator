from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import RestrictionCoefficientDTO
from osago.app.uow import UoWImpl
from osago.infra.static.types import OwnerType


class GetSuitableRestrictionsQuery(BaseModel):
    owner_type: OwnerType
    limitation_flag: bool


class GetSuitableRestrictionsQueryHandler(QueryHandler[GetSuitableRestrictionsQuery]):
    async def handle(
        self, query: GetSuitableRestrictionsQuery, uow: UoWImpl
    ) -> RestrictionCoefficientDTO:
        async with uow:
            restriction_coefficient = (
                await uow.restriction_coefficient_repo.get_suitable(
                    owner_type=query.owner_type,
                    limitation_flag=query.limitation_flag,
                )
            )
            return restriction_coefficient
