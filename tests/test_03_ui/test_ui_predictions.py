import pytest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.config import settings, prediciton_set_1


PORT = settings.local_test_port
CWD = settings.workdir


def prediction_test(ui_driver, image_path, exp):
    ui_driver.get(f'http://localhost:{PORT}/prediction/')

    file_input = ui_driver.find_element(By.ID, 'image-upload')
    file_input.send_keys(str(Path(CWD).joinpath(image_path)))

    try:
        upload_complete_element = WebDriverWait(ui_driver, 10).until(
            EC.presence_of_element_located((By.ID, 'prediction-result'))
        )
    except:
        raise Exception("Could not detect the prediction result")

    try:
        text_element = WebDriverWait(ui_driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'prediction-result'), f"Result: {exp}")
        )
    except:
        raise Exception("Could not find the expected result")


@pytest.mark.parametrize("image_path, exp", prediciton_set_1[:2])
def test_single_predictions(ui_driver, image_path, exp):
    prediction_test(ui_driver, image_path, exp)


def test_prediction_row(ui_driver):
    for image_path, exp in prediciton_set_1:
        prediction_test(ui_driver, image_path, exp)
