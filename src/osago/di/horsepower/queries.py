from app.abc.handlers import QueryHandler
from app.horsepower import (
    GetAllHorsepowerQuery,
    GetAllHorsepowerQueryHandler,
    GetSuitableHorsepowerQuery,
    GetSuitableHorsepowerQueryHandler,
)
from dependency_injector import containers, providers


class HorsepowerQueriesContainer(containers.DeclarativeContainer):
    get_all_horsepowers: providers.Factory[QueryHandler[GetAllHorsepowerQuery]] = (
        providers.Factory(GetAllHorsepowerQueryHandler)
    )

    get_suitable_horsepower: providers.Factory[
        QueryHandler[GetSuitableHorsepowerQuery]
    ] = providers.Factory(GetSuitableHorsepowerQueryHandler)

    query_handlers_mapping: providers.Dict[type, providers.Factory[QueryHandler]] = (
        providers.Dict(
            {
                GetAllHorsepowerQuery: get_all_horsepowers,
                GetSuitableHorsepowerQuery: get_suitable_horsepower,
            }
        )
    )
