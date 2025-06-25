from dependency_injector import containers, providers
from infra import settings
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import AsyncAdaptedQueuePool


class DataContainer(containers.DeclarativeContainer):
    db_engine = providers.Singleton(
        create_async_engine,
        url=settings.db_dsn,
        poolclass=AsyncAdaptedQueuePool,  # echo=True,
    )
    db_session_factory = providers.Factory(
        async_sessionmaker,
        bind=db_engine,
        expire_on_commit=False,
    )
