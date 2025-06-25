from dependency_injector import containers, providers

from osago.app.abc.handlers import QueryHandler
from osago.app.restrictions import (
    GetAllRestrictionsQuery,
    GetAllRestrictionsQueryHandler,
    GetSuitableRestrictionsQuery,
    GetSuitableRestrictionsQueryHandler,
)


class RestrictionQueryContainer(containers.DeclarativeContainer):
    get_all_restrictions: providers.Factory[QueryHandler[GetAllRestrictionsQuery]] = (
        providers.Factory(GetAllRestrictionsQueryHandler)
    )

    get_suitable_restrictions: providers.Factory[
        QueryHandler[GetSuitableRestrictionsQuery]
    ] = providers.Factory(GetSuitableRestrictionsQueryHandler)

    query_handlers_mapping: providers.Dict[type, providers.Factory[QueryHandler]] = (
        providers.Dict(
            {
                GetAllRestrictionsQuery: get_all_restrictions,
                GetSuitableRestrictionsQuery: get_suitable_restrictions,
            }
        )
    )
