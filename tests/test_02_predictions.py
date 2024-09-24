import pytest

from app.cnn.cnn_prediction import predict

from tests.utils.image import load_image_bytes
from tests.config import prediciton_set_1


@pytest.mark.parametrize("image_path, exp", prediciton_set_1)
def test_model_predictions(cnn_model, image_path, exp):
    image_bytes = load_image_bytes(image_path)
    result = predict(image_bytes)
    assert result["value"] == exp
