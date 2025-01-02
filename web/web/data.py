import httpx

from functools import lru_cache
from typing import Dict, Optional
from pydantic import BaseModel

from .config import settings

class CloudProvider(BaseModel):
    id: str
    name: str
    description: Optional[str] = None


class CloudProviderRegion(BaseModel):
    id: str
    name: str
    displayName: str


class RegionCode(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    cloudProvider: str
    location: str
    cloudProviderRegion: CloudProviderRegion


class Locations(BaseModel):
    id: str
    name: str
    countryCode: str
    country: str


class ApiData(BaseModel):
    cloudProviders: Dict[str, CloudProvider]
    regionCodes: Dict[str, RegionCode]
    regionsByLocation: Dict[str, Dict[str, CloudProviderRegion]]
    locations: Dict[str, Locations]


# @lru_cache
# def get_api_data():
#     url = "https://raw.githubusercontent.com/agonza05/cloudregioncodes/refs/heads/main/exports/regioncodes.json"
#     response = httpx.get(url)
#     response.raise_for_status()
#     return ApiData.model_validate(response.json())


def get_data(path: str):
    url = settings.cloudregioncodesapi_url + path
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


# api_data = get_api_data()
