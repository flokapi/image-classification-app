from fastapi import APIRouter, File, UploadFile, Request
from concurrent.futures import ProcessPoolExecutor
import asyncio

from app.htmx import htmx
from app.operations import image


import app.cnn.cnn_prediction as cnn
import app.operations.plot_predictions as plot


router = APIRouter(prefix="/prediction",
                   tags=["Prediction"])


async def run(fun, *args, **kwargs):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, fun, *args, **kwargs)


@router.get("/")
@htmx("prediction")
async def hx_main(request: Request):
    pass


@router.post("/hx-predict")
@htmx("prediction_result")
async def hx_cnn_predict(request: Request, file: UploadFile = File(...)):
    file_content = await file.read()
    base64_image = await run(image.binary_to_base64, file_content)
    result = await run(cnn.predict, file_content)
    plot.add_prediction((file.filename, result["yhat"]))
    result["yhat"] = "{:.3f}".format(result["yhat"])
    return {"result": result, "img": {"base64": base64_image}, "name": file.filename}


@router.post("/predict")
async def cnn_predict(file: UploadFile = File(...)):
    file_content = await file.read()
    result = await run(cnn.predict, file_content)
    plot.add_prediction((file.filename, result["yhat"]))
    return {"result": result, "name": file.filename}


executor = ProcessPoolExecutor(
    max_workers=4, initializer=cnn.initialize)
