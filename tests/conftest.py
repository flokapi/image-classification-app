
import pytest

from app.cnn.cnn_prediction import initialize


@pytest.fixture(scope="module")
def cnn_model():
    initialize()
