from dependency_injector import containers, providers

from osago.di.bonus_malus.queries import (
    BonusMalusQueriesContainer,
)
from osago.di.mediator import MediatorContainer


class BonusMalusContainer(containers.DeclarativeContainer):
    uow = providers.Dependency()

    queries = providers.Container(
        BonusMalusQueriesContainer,
    )

    mediators = providers.Container(
        MediatorContainer,
        uow_factory=uow,
        query_mapping=queries.query_handlers_mapping.provided,
    )
    mediator = mediators.mediator
