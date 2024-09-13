from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.templates import templates
from app.operations import plot

from app.htmx import htmx


router = APIRouter(prefix="/plot", tags=["Plot"])


@router.get("/")
@htmx("plot")
def get_plot(request: Request):
    pass


@router.get("/plot")
@htmx("plot_image")
def get_plot(request: Request):
    base64_data = plot.plot()
    return {"img": {"base64": base64_data, "id": "plot-img"}}
