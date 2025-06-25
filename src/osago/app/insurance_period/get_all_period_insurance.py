from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import PeriodInsuranceDTO
from osago.app.uow import UoWImpl


class GetAllPeriodInsurancesQuery(BaseModel):
    pass


class GetAllPeriodInsurancesQueryHandler(QueryHandler[GetAllPeriodInsurancesQuery]):
    async def handle(
        self, query: GetAllPeriodInsurancesQuery, uow: UoWImpl
    ) -> list[PeriodInsuranceDTO]:
        async with uow:
            return await uow.period_insurance_repo.get_all()
