from fastapi import APIRouter, Request, Header
from fastapi.responses import FileResponse

from app.config import settings


FILES_LOCATION = settings.static_files_location


router = APIRouter(prefix="/files", tags=["Files"])


@router.get("/{file_name}")
async def get_file(file_name: str, request: Request, user_agent: str = Header(None)):
    return FileResponse(
        f"{FILES_LOCATION}/{file_name}",
        media_type="application/octet-stream",
        filename=file_name,
        headers={"X-Custom-Header": "value"}
    )
