from dependency_injector import containers, providers

from osago.app.abc.handlers import QueryHandler
from osago.app.insurance_period import (
    GetAllPeriodInsurancesQuery,
    GetAllPeriodInsurancesQueryHandler,
    GetSuitablePeriodInsuranceQuery,
    GetSuitablePeriodInsuranceQueryHandler,
)


class PeriodInsuranceQueriesContainer(containers.DeclarativeContainer):
    get_all_period_insurance: providers.Factory[
        QueryHandler[GetAllPeriodInsurancesQuery]
    ] = providers.Factory(GetAllPeriodInsurancesQueryHandler)

    get_suitable_period_insurance: providers.Factory[
        QueryHandler[GetSuitablePeriodInsuranceQuery]
    ] = providers.Factory(GetSuitablePeriodInsuranceQueryHandler)

    query_handlers_mapping: providers.Dict[type, providers.Factory[QueryHandler]] = (
        providers.Dict(
            {
                GetAllPeriodInsurancesQuery: get_all_period_insurance,
                GetSuitablePeriodInsuranceQuery: get_suitable_period_insurance,
            }
        )
    )
