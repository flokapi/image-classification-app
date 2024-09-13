from fastapi import APIRouter, File, UploadFile


router = APIRouter(prefix="/cnn", tags=["Cnn"])


print(router.prefix)


@router.post("/predict")
async def cnn_predict(file: UploadFile = File(...)):
    file_content = await file.read()
    result = await run(cnn.predict, file_content)
    return {"result": result}


@router.get("/test")
async def cnn_test():
    return {"result": "it works!"}
