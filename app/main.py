from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from .routers import model, prediction, history
from .htmx import htmx


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"))
app.mount("/files", StaticFiles(directory="files"))

app.include_router(model.router)
app.include_router(prediction.router)
app.include_router(history.router)


@app.get("/")
@htmx("index")
async def index(request: Request):
    pass
