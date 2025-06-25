from dependency_injector import containers, providers
from di.horsepower.queries import (
    HorsepowerQueriesContainer,
)
from di.mediator import MediatorContainer


class HorsepowerContainer(containers.DeclarativeContainer):
    uow = providers.Dependency()

    queries = providers.Container(
        HorsepowerQueriesContainer,
    )
    mediators = providers.Container(
        MediatorContainer,
        uow_factory=uow,
        query_mapping=queries.query_handlers_mapping.provided,
    )
    mediator = mediators.mediator
