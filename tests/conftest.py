
import pytest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


from app.cnn.cnn_prediction import initialize
from . import utils


@pytest.fixture(scope="module")
def cnn_model():
    initialize()


@pytest.fixture
def uvicorn():
    pid = utils.start_uvicorn()
    yield
    utils.stop_uvicorn(pid)


@pytest.fixture
def driver(uvicorn):
    yield webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
