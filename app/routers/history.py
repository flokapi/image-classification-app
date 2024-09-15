from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.templates import templates
from app.operations import plot_predictions as plot

from app.htmx import htmx


router = APIRouter(prefix="/history", tags=["History"])


@router.get("/")
@htmx("plot")
async def get_plot(request: Request):
    pass


@router.get("/plot")
@htmx("plot_image")
async def get_plot(request: Request):
    base64_data = plot.plot()
    return {"img": {"base64": base64_data}}
