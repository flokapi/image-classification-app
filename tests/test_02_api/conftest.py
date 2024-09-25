import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport


from app.main import app


@pytest.fixture
def client():
    yield TestClient(app)


@pytest.fixture
def async_client():
    yield AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
