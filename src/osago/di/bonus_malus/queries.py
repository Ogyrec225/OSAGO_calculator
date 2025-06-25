from app.abc.handlers import QueryHandler
from app.bonus_malus import (
    GetAllBonusMalusQuery,
    GetAllBonusMalusQueryHandler,
    GetSuitableBonusMalusQuery,
    GetSuitableBonusMalusQueryHandler,
)
from dependency_injector import containers, providers


class BonusMalusQueriesContainer(containers.DeclarativeContainer):
    get_all_bonus_malus: providers.Factory[QueryHandler[GetAllBonusMalusQuery]] = (
        providers.Factory(GetAllBonusMalusQueryHandler)
    )

    get_suitable_bonus_malus: providers.Factory[
        QueryHandler[GetSuitableBonusMalusQuery]
    ] = providers.Factory(GetSuitableBonusMalusQueryHandler)

    query_handlers_mapping: providers.Dict[type, providers.Factory[QueryHandler]] = (
        providers.Dict(
            {
                GetAllBonusMalusQuery: get_all_bonus_malus,
                GetSuitableBonusMalusQuery: get_suitable_bonus_malus,
            }
        )
    )
