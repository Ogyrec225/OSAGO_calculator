from dependency_injector import containers, providers
from di.mediator import MediatorContainer
from di.restriction_coefficient.queries import RestrictionQueryContainer


class RestrictionCoefficientContainer(containers.DeclarativeContainer):
    uow = providers.Dependency()

    queries = providers.Container(
        RestrictionQueryContainer,
    )
    mediators = providers.Container(
        MediatorContainer,
        uow_factory=uow,
        query_mapping=queries.query_handlers_mapping.provided,
    )
    mediator = mediators.mediator
