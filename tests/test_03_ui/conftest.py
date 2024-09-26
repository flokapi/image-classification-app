import pytest


from tests.utils import uvicorn_server

from tests.utils.uvicorn_server import UvicornServer
from tests.utils.selenium_driver import SeleniumDriver


from tests.config import settings


LOCAL_TEST_PORT = settings.local_test_port
DRIVER_PATH_PATH = settings.driver_path_path


@pytest.fixture(scope="module")
def server():
    uv_server = UvicornServer(LOCAL_TEST_PORT)
    uv_server.start()
    yield


@pytest.fixture
def ui_driver(server):
    driver = SeleniumDriver(DRIVER_PATH_PATH)
    yield driver.create()
    driver.quit()
