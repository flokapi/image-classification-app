
from pathlib import Path
import atexit

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


DRIVER_PATH_PATH = Path(".driver_path")

driver = None


def get_or_create_driver_path():
    if not DRIVER_PATH_PATH.exists() or not Path(DRIVER_PATH_PATH.read_text()).exists():
        driver_path = GeckoDriverManager().install()
        DRIVER_PATH_PATH.write_text(driver_path)
    else:
        driver_path = DRIVER_PATH_PATH.read_text()

    return driver_path


def create():
    global driver
    driver_path = get_or_create_driver_path()
    driver = webdriver.Firefox(service=FirefoxService(driver_path))
    return driver


def stop():
    global driver
    if driver:
        driver.quit()
        driver = None


atexit.register(stop)
