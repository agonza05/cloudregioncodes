from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from .config import settings
from .internal import general
from .routers import cloud_providers, region_codes, regions_by_location, locations

app = FastAPI()

app.include_router(general.router)
app.include_router(cloud_providers.router)
app.include_router(region_codes.router)
app.include_router(regions_by_location.router)
app.include_router(locations.router)


@app.get("/", response_class=PlainTextResponse)
async def root():
    return settings.app_name
