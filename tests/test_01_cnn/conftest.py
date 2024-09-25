import pytest

from app.cnn import cnn_prediction


# load the model from the keras file
@pytest.fixture(scope="module")
def cnn_model():
    cnn_prediction.initialize()
