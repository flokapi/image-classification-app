import pytest
import time


from tests.utils import UvicornServer, SeleniumDriver
from tests.config import settings


LOCAL_TEST_PORT = settings.local_test_port
DRIVER_PATH_PATH = settings.driver_path_path


@pytest.fixture(scope="module")
def server():
    uv_server = UvicornServer(LOCAL_TEST_PORT)
    uv_server.start()
    time.sleep(0.2)
    yield


@pytest.fixture
def ui_driver(server):
    driver = SeleniumDriver(DRIVER_PATH_PATH)
    yield driver.create()
    driver.quit()
