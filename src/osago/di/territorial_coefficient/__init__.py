from dependency_injector import containers, providers
from di.mediator import MediatorContainer
from di.territorial_coefficient.queries import (
    TerritorialCoefficientsQueriesContainer,
)


class TerritorialCoefficientContainer(containers.DeclarativeContainer):
    uow = providers.Dependency()

    queries = providers.Container(
        TerritorialCoefficientsQueriesContainer,
    )
    mediators = providers.Container(
        MediatorContainer,
        uow_factory=uow,
        query_mapping=queries.query_handlers_mapping.provided,
    )
    mediator = mediators.mediator
