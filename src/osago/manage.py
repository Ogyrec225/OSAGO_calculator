import uvicorn
from infra import ModeType, settings
from presentation.api.main import app


def start():
    uvicorn.run(
        app="presentation.api.main:app" if settings.mode == ModeType.DEBUG else app,
        port=settings.port,
        host=settings.host,
        reload=True if settings.mode == ModeType.DEBUG else False,
    )


if __name__ == "__main__":
    start()
