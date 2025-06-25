from dependency_injector import containers, providers

from osago.di.insurance_rate.queries import (
    InsuranceRateQueriesContainer,
)
from osago.di.mediator import MediatorContainer


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
