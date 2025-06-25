from collections.abc import AsyncGenerator
from unittest.mock import AsyncMock

import pytest
import pytest_asyncio
from app.mediator_aggregator import MediatorAggregator
from dependency_injector import containers, providers
from httpx import ASGITransport, AsyncClient
from infra import ModeType, settings
from presentation.api.main import app  # Замените на путь к вашему main.py


@pytest_asyncio.fixture(scope="function")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    assert settings.mode == ModeType.TEST
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


@pytest.fixture
def mock_mediator():
    """Фикстура для мокирования MediatorAggregator."""
    mock_mediator = AsyncMock(spec=MediatorAggregator)  # используем AsyncMock
    return mock_mediator


@pytest.fixture
def app_with_mock_mediator(mock_mediator):
    """Фикстура для создания приложения FastAPI с мокированным mediator."""
    container = containers.ApplicationContainer()
    container.mediator.override(providers.Object(mock_mediator))
    app.dependency_overrides = {
        MediatorAggregator: lambda: mock_mediator,
    }
    return app
