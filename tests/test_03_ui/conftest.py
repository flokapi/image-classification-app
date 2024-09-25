import pytest


from tests.utils import uvicorn_server, selenium_driver
from tests.config import settings


@pytest.fixture(scope="module")
def server():
    uvicorn_server.start()
    yield
    uvicorn_server.stop()


@pytest.fixture
def ui_driver(server):
    yield selenium_driver.create()
    selenium_driver.stop()
