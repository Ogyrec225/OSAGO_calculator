from app.abc.handlers import QueryHandler
from app.insurance_rate import (
    GetAllInsuranceRatesQuery,
    GetAllInsuranceRatesQueryHandler,
    GetSuitableInsuranceRatesQuery,
    GetSuitableInsuranceRatesQueryHandler,
)
from dependency_injector import containers, providers


class InsuranceRateQueriesContainer(containers.DeclarativeContainer):
    get_all_insurance_rates: providers.Factory[
        QueryHandler[GetAllInsuranceRatesQuery]
    ] = providers.Factory(GetAllInsuranceRatesQueryHandler)

    get_suitable_insurance_rate: providers.Factory[
        QueryHandler[GetSuitableInsuranceRatesQuery]
    ] = providers.Factory(GetSuitableInsuranceRatesQueryHandler)

    query_handlers_mapping: providers.Dict[type, providers.Factory[QueryHandler]] = (
        providers.Dict(
            {
                GetAllInsuranceRatesQuery: get_all_insurance_rates,
                GetSuitableInsuranceRatesQuery: get_suitable_insurance_rate,
            }
        )
    )
