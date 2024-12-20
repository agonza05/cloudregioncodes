from fastapi import APIRouter

from api.config import code_config
from api.data import api_data


cloud_providers = api_data.cloudProviders

router = APIRouter(
    prefix=code_config.app_base_path + "/cloudProviders",
    tags=["cloudProviders"],
)

@router.get("/")
async def list_cloud_providers():
    return cloud_providers

@router.get("/{cloud_provider_id}")
async def read_cloud_provider(cloud_provider_id: str):
    return cloud_providers[cloud_provider_id]
