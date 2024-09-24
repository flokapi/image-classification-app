import pytest

from app.cnn import cnn_prediction

from tests.utils import uvicorn_server, selenium_driver
from tests.config import settings


@pytest.fixture(scope="module")
def cnn_model():
    cnn_prediction.initialize()


@pytest.fixture(scope="module")
def server():
    uvicorn_server.start()
    yield
    uvicorn_server.stop()


@pytest.fixture
def driver(server):
    yield selenium_driver.create()
    selenium_driver.stop()
