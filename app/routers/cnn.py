from fastapi import APIRouter, File, UploadFile
from app import api


router = APIRouter(prefix="/cnn", tags=["Cnn"])


print(router.prefix)


@api.register
@router.post("/predict")
async def cnn_predict(file: UploadFile = File(...)):
    file_content = await file.read()
    result = await run(cnn.predict, file_content)
    return {"result": result}


@api.register
@router.get("/test")
async def cnn_test():
    return {"result": "it works!"}
