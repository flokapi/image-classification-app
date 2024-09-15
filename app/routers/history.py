from fastapi import APIRouter, Request

from app.templates import templates
from app.operations import plot_predictions as plot

from app.htmx import htmx


router = APIRouter(prefix="/history", tags=["History"])


@router.get("/")
@htmx("history")
async def hx_get_main(request: Request):
    pass


@router.get("/plot")
@htmx("history_plot")
async def hx_get_plot(request: Request):
    base64_data = plot.plot()
    return {"img": {"base64": base64_data}}
