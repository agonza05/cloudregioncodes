from fastapi import APIRouter

from config import settings


router = APIRouter(
    prefix=settings.app_base_path + "/app",
    tags=["app"],
)


@router.get("/status")
async def get_app_status():
    return {"status": "UP"}


@router.get("/info")
async def get_app_info():
    return {
        "app_name": settings.app_name,
        "app_url": settings.app_url,
        "admin_email": settings.admin_email,
    }
