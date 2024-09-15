from fastapi import APIRouter, Request, Header
from fastapi.responses import FileResponse

from app.templates import templates
from app.operations import plot_predictions as plot

from app.htmx import htmx
from app.config import settings


TF_MODEL_FILE_NAME = settings.tf_model_file_name
LOSS_PLOT_FILE_NAME = settings.loss_plot_file_name
ACCURACY_PLOT_FILE_NAME = settings.accuracy_plot_file_name


router = APIRouter(prefix="/model", tags=["Model"])


@router.get("/")
@htmx("model")
async def hx_get_main(request: Request):
    return {
        "model_file_name": TF_MODEL_FILE_NAME,
        "loss_plot_file_name": LOSS_PLOT_FILE_NAME,
        "accuracy_plot_file_name": ACCURACY_PLOT_FILE_NAME
    }
