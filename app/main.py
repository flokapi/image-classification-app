from fastapi import FastAPI, Request

from .routers import model, prediction, history
from .htmx import htmx


app = FastAPI()

app.include_router(model.router)
app.include_router(prediction.router)
app.include_router(history.router)


@app.get("/")
@htmx("index")
async def index(request: Request):
    pass
