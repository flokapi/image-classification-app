from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from .templates import templates

from .routers import cnn, plot
from .htmx import htmx


app = FastAPI()

app.include_router(cnn.router)
app.include_router(plot.router)


@app.get("/")
@htmx("index")
def index(request: Request):
    pass
