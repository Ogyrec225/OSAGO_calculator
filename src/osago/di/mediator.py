from app.mediator import MediatorImpl
from dependency_injector import containers, providers
from di.utils import unification_handlers


class MediatorContainer(containers.DeclarativeContainer):
    uow_factory = providers.Dependency()

    query_mapping = providers.Dependency()

    mediator_handlers = providers.Callable(
        unification_handlers,
        query_mapping.provided,
    )

    mediator = providers.Factory(
        MediatorImpl,
        uow_factory=uow_factory,
        handlers=mediator_handlers,
    )
