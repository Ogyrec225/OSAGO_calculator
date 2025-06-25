from dependency_injector import containers, providers
from di.mediator import MediatorContainer
from di.period_use.queries import (
    PeriodUseQueriesContainer,
)


class PeriodUseContainer(containers.DeclarativeContainer):
    uow = providers.Dependency()

    queries = providers.Container(
        PeriodUseQueriesContainer,
    )
    mediators = providers.Container(
        MediatorContainer,
        uow_factory=uow,
        query_mapping=queries.query_handlers_mapping.provided,
    )
    mediator = mediators.mediator
