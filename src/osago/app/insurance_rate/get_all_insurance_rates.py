from app.abc import QueryHandler
from app.dto import InsuranceRateDTO
from app.uow import UoWImpl
from pydantic import BaseModel


class GetAllInsuranceRatesQuery(BaseModel):
    pass


class GetAllInsuranceRatesQueryHandler(QueryHandler[GetAllInsuranceRatesQuery]):
    async def handle(
        self, query: GetAllInsuranceRatesQuery, uow: UoWImpl
    ) -> list[InsuranceRateDTO]:
        async with uow:
            return await uow.insurance_rate_repo.get_all()
