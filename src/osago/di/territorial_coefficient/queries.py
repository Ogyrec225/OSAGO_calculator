from app.abc.handlers import QueryHandler
from app.territorial_coefficient import (
    GetAllTerritorialCoefficientQuery,
    GetAllTerritorialCoefficientQueryHandler,
    GetSuitableTerritorialCoefficientQuery,
    GetSuitableTerritorialCoefficientQueryHandler,
)
from dependency_injector import containers, providers


class TerritorialCoefficientsQueriesContainer(containers.DeclarativeContainer):
    get_all_territorial_coefficients: providers.Factory[
        QueryHandler[GetAllTerritorialCoefficientQuery]
    ] = providers.Factory(GetAllTerritorialCoefficientQueryHandler)

    get_suitable_territorial_coefficient: providers.Factory[
        QueryHandler[GetSuitableTerritorialCoefficientQuery]
    ] = providers.Factory(GetSuitableTerritorialCoefficientQueryHandler)

    query_handlers_mapping: providers.Dict[type, providers.Factory[QueryHandler]] = (
        providers.Dict(
            {
                GetAllTerritorialCoefficientQuery: get_all_territorial_coefficients,
                GetSuitableTerritorialCoefficientQuery: get_suitable_territorial_coefficient,
            }
        )
    )
