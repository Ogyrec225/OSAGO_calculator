import uvicorn

from osago.infra import ModeType, settings
from osago.presentation.api.main import app


def start():
    uvicorn.run(
        app="osago.presentation.api.main:app"
        if settings.mode == ModeType.DEBUG
        else app,
        port=settings.port,
        host=settings.host,
        reload=True if settings.mode == ModeType.DEBUG else False,
    )


if __name__ == "__main__":
    start()
