from fastapi import APIRouter, File, UploadFile, Request
from concurrent.futures import ProcessPoolExecutor
import asyncio

from app.htmx import htmx

import app.cnn.cnn_prediction as cnn


router = APIRouter(prefix="/image-classification",
                   tags=["Image Classification"])


async def run(fun, *args, **kwargs):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, fun, *args, **kwargs)


@router.get("/")
@htmx("predict_digit")
async def main(request: Request):
    pass


@router.post("/predict")
@htmx("predict_digit_result")
async def cnn_predict(request: Request, file: UploadFile = File(...)):
    file_content = await file.read()
    result = await run(cnn.predict, file_content)
    return {"result": result}


@router.get("/test")
async def cnn_test():
    return {"result": "it works!"}


executor = ProcessPoolExecutor(
    max_workers=4, initializer=cnn.initialize)
