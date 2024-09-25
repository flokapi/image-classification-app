import pytest
from pathlib import Path

from app.main import app

from tests.config import settings, prediciton_set_1


CWD = settings.workdir


@pytest.mark.asyncio
@pytest.mark.parametrize("image_path, exp", prediciton_set_1)
async def test_create_user(async_client, image_path, exp):
    image_path = str(Path(CWD).joinpath(image_path))
    files = {'file': open(image_path, 'rb')}

    # res = await async_client.get("/prediction/")

    res = await async_client.post("/prediction/predict", files=files)
    data = res.json()

    assert data["result"]["value"] == exp


# @pytest.mark.parametrize("image_path, exp", prediciton_set_1)
# def test_create_user(client, image_path, exp):
#     image_path = str(Path(CWD).joinpath(image_path))
#     files = {'file': open(image_path, 'rb')}
#     res = client.post("/prediction/predict", files=files)
#     data = res.json()
#     assert data["result"]["value"] == exp
