from dependency_injector import containers, providers

from osago.app.abc.handlers import QueryHandler
from osago.app.periods_use import (
    GetAllPeriodsUseQuery,
    GetAllPeriodsUseQueryHandler,
    GetSuitablePeriodsUseQuery,
    GetSuitablePeriodsUseQueryHandler,
)


class PeriodUseQueriesContainer(containers.DeclarativeContainer):
    get_all_periods_use: providers.Factory[QueryHandler[GetAllPeriodsUseQuery]] = (
        providers.Factory(GetAllPeriodsUseQueryHandler)
    )

    get_suitable_period_use: providers.Factory[
        QueryHandler[GetSuitablePeriodsUseQuery]
    ] = providers.Factory(GetSuitablePeriodsUseQueryHandler)

    query_handlers_mapping: providers.Dict[type, providers.Factory[QueryHandler]] = (
        providers.Dict(
            {
                GetAllPeriodsUseQuery: get_all_periods_use,
                GetSuitablePeriodsUseQuery: get_suitable_period_use,
            }
        )
    )
