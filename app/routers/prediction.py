from fastapi import APIRouter, File, UploadFile, Request
from concurrent.futures import ProcessPoolExecutor
import asyncio
import hotmix as hm
import atexit

from app.operations import image
import app.cnn.cnn_prediction as cnn
import app.operations.plot_predictions as plot


import multiprocessing
multiprocessing.set_start_method('spawn')


router = APIRouter(prefix="/prediction", tags=["Prediction"])

executor = ProcessPoolExecutor(max_workers=2, initializer=cnn.initialize)
atexit.register(executor.shutdown)


async def run(fun, *args, **kwargs):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, fun, *args, **kwargs)


@router.get("/")
@hm.htmx("prediction")
async def hx_get_main(request: Request):
    pass


@router.post("/hx-predict")
@hm.htmx("prediction_result")
async def hx_post_predict(request: Request, file: UploadFile = File(...)):
    file_content = await file.read()
    base64_image = await run(image.binary_to_base64, file_content)
    result = await run(cnn.predict, file_content)
    plot.add_prediction((file.filename, result["yhat"]))
    result["yhat"] = "{:.3f}".format(result["yhat"])
    return {"result": result, "img": {"base64": base64_image}, "name": file.filename}


@router.post("/predict")
async def post_predict(file: UploadFile = File(...)):
    file_content = await file.read()
    result = await run(cnn.predict, file_content)
    plot.add_prediction((file.filename, result["yhat"]))
    return {"result": result, "name": file.filename}
