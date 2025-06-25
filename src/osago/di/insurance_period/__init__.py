from dependency_injector import containers, providers

from osago.di.mediator import MediatorContainer
from osago.di.insurance_period.queries import (
    PeriodInsuranceQueriesContainer,
)


class PeriodInsuranceContainer(containers.DeclarativeContainer):
    uow = providers.Dependency()

    queries = providers.Container(
        PeriodInsuranceQueriesContainer,
    )
    mediators = providers.Container(
        MediatorContainer,
        uow_factory=uow,
        query_mapping=queries.query_handlers_mapping.provided,
    )
    mediator = mediators.mediator
