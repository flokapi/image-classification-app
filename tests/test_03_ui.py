import time
import pytest


def test_ui(driver):
    driver.get('http://localhost:8000/prediction')
    time.sleep(10)
    driver.quit()
