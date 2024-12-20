from fastapi import APIRouter

from api.config import code_config
from api.data import api_data


region_codes = api_data.regionCodes

router = APIRouter(
    prefix=code_config.app_base_path + "/regionCodes",
    tags=["regionCodes"],
)

@router.get("/")
async def list_region_codes():
    return region_codes

@router.get("/{region_code_id}")
async def read_region_codes(region_code_id: str):
    return region_codes[region_code_id]
