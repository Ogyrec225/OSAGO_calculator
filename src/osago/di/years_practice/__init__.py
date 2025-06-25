from dependency_injector import containers, providers
from di.mediator import MediatorContainer
from di.years_practice.queries import (
    PracticeQueriesContainer,
)


class YearsPracticeContainer(containers.DeclarativeContainer):
    uow = providers.Dependency()

    queries = providers.Container(
        PracticeQueriesContainer,
    )
    mediators = providers.Container(
        MediatorContainer,
        uow_factory=uow,
        query_mapping=queries.query_handlers_mapping.provided,
    )
    mediator = mediators.mediator
