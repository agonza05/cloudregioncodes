from os.path import join, dirname, normpath
from functools import lru_cache
from typing import Dict, Optional
from pydantic import BaseModel


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


class ApiData(BaseModel):
    cloudProviders: Dict[str, CloudProvider]
    regionCodes: Dict[str, RegionCode]
    regionsByLocation: Dict[str, Dict[str, CloudProviderRegion]]


data_file = normpath(join(dirname(__file__), "../data/data.json"))


@lru_cache
def get_api_data():
    return ApiData.parse_file(data_file)


api_data = get_api_data()
