from fastapi import APIRouter, HTTPException

from api.config import settings
from api.data import api_data


region_codes = api_data.regionCodes

router = APIRouter(
    prefix=settings.app_base_path + "/regionCodes",
    tags=["regionCodes"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def list_region_codes():
    return region_codes


@router.get("/{region_code_id}")
async def read_region_codes(region_code_id: str):
    if region_code_id not in region_codes:
        raise HTTPException(status_code=404, detail="ID not found: " + region_code_id)
    return region_codes[region_code_id]

@router.get("/{region_code_id}/cloudProviderRegion")
async def read_cloud_provider_region(region_code_id: str):
    if region_code_id not in region_codes:
        raise HTTPException(status_code=404, detail="ID not found: " + region_code_id)
    return region_codes[region_code_id].cloudProviderRegion
