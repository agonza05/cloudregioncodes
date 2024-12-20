from fastapi import FastAPI

from api.internal import general
from api.routers import region_codes, regions_by_location, cloud_providers

app = FastAPI()

app.include_router(general.router)
app.include_router(cloud_providers.router)
app.include_router(region_codes.router)
app.include_router(regions_by_location.router)
