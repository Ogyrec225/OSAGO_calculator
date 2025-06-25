from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import RestrictionCoefficientDTO
from osago.app.uow import UoWImpl


class GetAllRestrictionsQuery(BaseModel):
    pass


class GetAllRestrictionsQueryHandler(QueryHandler[GetAllRestrictionsQuery]):
    async def handle(
        self, query: QueryHandler, uow: UoWImpl
    ) -> list[RestrictionCoefficientDTO]:
        async with uow:
            return await uow.restriction_coefficient_repo.get_all()
