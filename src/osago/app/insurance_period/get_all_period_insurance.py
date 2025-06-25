from app.abc import QueryHandler
from app.dto import PeriodInsuranceDTO
from app.uow import UoWImpl
from pydantic import BaseModel


class GetAllPeriodInsurancesQuery(BaseModel):
    pass


class GetAllPeriodInsurancesQueryHandler(QueryHandler[GetAllPeriodInsurancesQuery]):
    async def handle(
        self, query: GetAllPeriodInsurancesQuery, uow: UoWImpl
    ) -> list[PeriodInsuranceDTO]:
        async with uow:
            return await uow.period_insurance_repo.get_all()
