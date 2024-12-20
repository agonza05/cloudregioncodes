from functools import lru_cache
from typing import Annotated
from fastapi import APIRouter, Depends

from api.config import Settings, code_config

router = APIRouter(
    prefix=code_config.app_base_path + "/app",
    tags=["app"],
)

@lru_cache
def get_settings():
    return Settings()

@router.get("/status")
async def get_app_status():
    return {"status": "UP"}

@router.get("/info")
async def get_app_info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "app_url": settings.app_url,
        "admin_email": settings.admin_email,
    }
