import pytest
from pathlib import Path

from tests.config import settings, prediciton_set_1


CWD = settings.workdir


def test_create_user(client):
    image_path = str(Path(CWD).joinpath(image_path))
    files = {'file': open(image_path, 'rb')}
    res = client.post("/prediction/predict", files=files)

    print(res.json())
