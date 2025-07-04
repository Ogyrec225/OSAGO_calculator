from app.abc.handlers import QueryHandler
from app.years_practices import (
    GetAllYearsPracticesQuery,
    GetAllYearsPracticesQueryHandler,
    GetSuitableYearsPracticesQuery,
    GetSuitableYearsPracticesQueryHandler,
)
from dependency_injector import containers, providers


class PracticeQueriesContainer(containers.DeclarativeContainer):
    get_all_years_practices: providers.Factory[
        QueryHandler[GetAllYearsPracticesQuery]
    ] = providers.Factory(GetAllYearsPracticesQueryHandler)

    get_suitable_years_practices: providers.Factory[
        QueryHandler[GetSuitableYearsPracticesQuery]
    ] = providers.Factory(GetSuitableYearsPracticesQueryHandler)

    query_handlers_mapping: providers.Dict[type, providers.Factory[QueryHandler]] = (
        providers.Dict(
            {
                GetAllYearsPracticesQuery: get_all_years_practices,
                GetSuitableYearsPracticesQuery: get_suitable_years_practices,
            }
        )
    )
