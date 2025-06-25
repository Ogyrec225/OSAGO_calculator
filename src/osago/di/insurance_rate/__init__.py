from dependency_injector import containers, providers
from di.insurance_rate.queries import (
    InsuranceRateQueriesContainer,
)
from di.mediator import MediatorContainer


class InsuranceContainer(containers.DeclarativeContainer):
    uow = providers.Dependency()

    queries = providers.Container(
        InsuranceRateQueriesContainer,
    )
    mediators = providers.Container(
        MediatorContainer,
        uow_factory=uow,
        query_mapping=queries.query_handlers_mapping.provided,
    )
    mediator = mediators.mediator
