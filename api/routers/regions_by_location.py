from fastapi import APIRouter

from api.config import code_config
from api.data import api_data


regions_by_location = api_data.regionsByLocation

router = APIRouter(
    prefix=code_config.app_base_path + "/regionsByLocation",
    tags=["regionsByLocation"],
)

@router.get("/")
async def list_regions_by_location():
    return regions_by_location

@router.get("/{location_id}")
async def read_regions_by_location(location_id: str):
    return regions_by_location.get(location_id)

@router.get("/{location_id}/{cloud_provider_id}")
async def read_region_by_location_provider(location_id: str, cloud_provider_id: str):
    return regions_by_location.get(location_id, {}).get(cloud_provider_id)
