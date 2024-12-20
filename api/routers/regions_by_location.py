from fastapi import APIRouter, HTTPException

from config import settings
from data import api_data


regions_by_location = api_data.regionsByLocation

router = APIRouter(
    prefix=settings.app_base_path + "/regionsByLocation",
    tags=["regionsByLocation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def list_regions_by_location():
    return regions_by_location


@router.get("/{location_id}")
async def read_regions_by_location(location_id: str):
    if location_id not in regions_by_location:
        raise HTTPException(status_code=404, detail="ID not found: " + location_id)
    return regions_by_location[location_id]


@router.get("/{location_id}/{cloud_provider_id}")
async def read_provider_location(location_id: str, cloud_provider_id: str):
    if location_id not in regions_by_location:
        raise HTTPException(status_code=404, detail="ID not found: " + location_id)
    elif cloud_provider_id not in regions_by_location[location_id]:
        raise HTTPException(
            status_code=404, detail="ID not found: " + cloud_provider_id
        )
    return regions_by_location[location_id][cloud_provider_id]
