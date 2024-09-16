import pytest

from app.cnn.cnn_prediction import predict
from .utils import load_image_bytes


@pytest.mark.parametrize("image_path, exp", [
    ("data/happy/happy_1.jpg", "Happy"),
    ("data/happy/happy_2.jpg", "Happy"),
    ("data/happy/happy_3.jpg", "Happy"),
    ("data/sad/sad_1.jpg", "Sad"),
    ("data/sad/sad_2.jpg", "Sad"),
    ("data/sad/sad_3.png", "Sad"),
])
def test_model_predictions(cnn_model, image_path, exp):
    image_bytes = load_image_bytes(image_path)
    result = predict(image_bytes)
    print(exp)
    assert result["value"] == exp
