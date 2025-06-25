from fastapi import FastAPI
from infra import settings
from presentation.api.middlewares.setup import setup_core_middleware
from presentation.api.routers.configure import configure, global_lifespan


def start() -> FastAPI:
    app = FastAPI(
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
        lifespan=global_lifespan,
    )
    setup_core_middleware(app)
    configure(app)

    return app


app = start()
