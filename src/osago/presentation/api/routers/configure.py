from fastapi import FastAPI

from osago.di import ApplicationContainer
from osago.domain.base_exceptions import ApplicationError, DomainError
from osago.presentation.api.exception_handlers import generic_exception_handler
from osago.presentation.api.routers import v1, v2


def configure(api: FastAPI):
    api.include_router(v1.coefficients_router, prefix="/v1")
    api.include_router(v1.calculate_router, prefix="/v1")
    api.include_router(v2.coefficients_router, prefix="/v2")

    api.add_exception_handler(DomainError, generic_exception_handler)
    api.add_exception_handler(ApplicationError, generic_exception_handler)


async def global_lifespan(app: FastAPI):
    container = ApplicationContainer()
    container.wire(packages=[v1, v2])
    app.container = container

    yield
