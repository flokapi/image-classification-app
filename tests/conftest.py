
import pytest

from app.cnn.cnn_model import prepare_model
from app.cnn.cnn_prediction import initialize


@pytest.fixture(scope="module")
def cnn_model():
    initialize()

# @pytest.fixture(scope="module")
# def cnn_model():
#     model = prepare_model()
#     yield model
