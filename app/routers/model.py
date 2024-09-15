from fastapi import APIRouter, Request

from app.templates import templates
from app.operations import plot_predictions as plot

from app.htmx import htmx


router = APIRouter(prefix="/model", tags=["Model"])


@router.get("/")
@htmx("model")
async def get_plot(request: Request):
    pass
