from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class SeleniumDriver:
    driver_path_path: Path
    driver: webdriver.Firefox

    def __init__(self, _driver_path_path: str):
        self.driver_path_path = Path(_driver_path_path)

    def _get_or_create_driver_path(self) -> str:

        if not self.driver_path_path.exists() or not Path(self.driver_path_path.read_text()).exists():
            driver_path = GeckoDriverManager().install()
            self.driver_path_path.write_text(driver_path)
        else:
            driver_path = self.driver_path_path.read_text()

        return driver_path

    def create(self) -> webdriver.Firefox:
        driver_path = self._get_or_create_driver_path()
        self.driver = webdriver.Firefox(service=FirefoxService(driver_path))
        return self.driver

    def quit(self):
        self.driver.quit()
