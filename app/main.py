from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from .routers import model, prediction, history
import hotmix as hm


app = FastAPI()
hm.init("app/templates")

app.mount("/static", StaticFiles(directory="static"))
app.mount("/files", StaticFiles(directory="files"))

app.include_router(model.router)
app.include_router(prediction.router)
app.include_router(history.router)


@app.get("/")
@hm.htmx("index")
async def index(request: Request):
    pass
