from app.abc import QueryHandler
from app.dto import RestrictionCoefficientDTO
from app.uow import UoWImpl
from pydantic import BaseModel


class GetAllRestrictionsQuery(BaseModel):
    pass


class GetAllRestrictionsQueryHandler(QueryHandler[GetAllRestrictionsQuery]):
    async def handle(
        self, query: QueryHandler, uow: UoWImpl
    ) -> list[RestrictionCoefficientDTO]:
        async with uow:
            return await uow.restriction_coefficient_repo.get_all()
