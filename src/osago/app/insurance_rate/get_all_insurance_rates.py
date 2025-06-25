from pydantic import BaseModel

from osago.app.abc import QueryHandler
from osago.app.dto import InsuranceRateDTO
from osago.app.uow import UoWImpl


class GetAllInsuranceRatesQuery(BaseModel):
    pass


class GetAllInsuranceRatesQueryHandler(QueryHandler[GetAllInsuranceRatesQuery]):
    async def handle(
        self, query: GetAllInsuranceRatesQuery, uow: UoWImpl
    ) -> list[InsuranceRateDTO]:
        async with uow:
            return await uow.insurance_rate_repo.get_all()
