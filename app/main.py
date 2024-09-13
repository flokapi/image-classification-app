from fastapi import FastAPI


from . import api
from .routers import cnn


app = FastAPI()

app.include_router(cnn.router)
