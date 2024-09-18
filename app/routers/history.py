from fastapi import APIRouter, Request

import hotmix as hm
from app.operations import plot_predictions as plot


router = APIRouter(prefix="/history", tags=["History"])


@router.get("/")
@hm.htmx("history")
async def hx_get_main(request: Request):
    pass


@router.get("/plot")
@hm.htmx("history_plot")
async def hx_get_plot(request: Request):
    base64_data = plot.plot()
    return {"img": {"base64": base64_data}}
