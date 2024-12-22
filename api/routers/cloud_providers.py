from fastapi import APIRouter, HTTPException

from ..config import settings
from ..data import api_data


cloud_providers = api_data.cloudProviders

router = APIRouter(
    prefix=settings.app_base_path + "/cloudProviders",
    tags=["cloudProviders"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def list_cloud_providers():
    return cloud_providers


@router.get("/{cloud_provider_id}")
async def read_cloud_provider(cloud_provider_id: str):
    if cloud_provider_id not in cloud_providers:
        raise HTTPException(
            status_code=404, detail="ID not found: " + cloud_provider_id
        )
    return cloud_providers[cloud_provider_id]
