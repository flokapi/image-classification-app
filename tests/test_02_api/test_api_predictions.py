import pytest
from pathlib import Path

from tests.config import settings, prediciton_set_1


CWD = settings.workdir


@pytest.mark.parametrize("image_path, exp", prediciton_set_1)
def test_prediction(client, image_path, exp):
    image_path = str(Path(CWD).joinpath(image_path))
    files = {'file': open(image_path, 'rb')}
    res = client.post("/prediction/predict", files=files)

    assert res.json()["result"]["value"] == exp
