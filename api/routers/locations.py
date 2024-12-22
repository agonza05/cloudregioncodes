from fastapi import APIRouter, HTTPException

from ..config import settings
from ..data import api_data


locations = api_data.locations

router = APIRouter(
    prefix=settings.app_base_path + "/locations",
    tags=["locations"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def list_locations():
    return locations


@router.get("/{location_id}")
async def read_location(location_id: str):
    if location_id not in locations:
        raise HTTPException(status_code=404, detail="ID not found: " + location_id)
    return locations[location_id]
