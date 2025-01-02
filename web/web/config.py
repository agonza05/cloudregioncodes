from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


dotenv_file_local = "web/.env/.env.local"
dotenv_file_production = "web/.env/.env.prod"


class Settings(BaseSettings):
    app_name: str
    app_url: str
    admin_email: str
    cloudregioncodesapi_url: str

    model_config = SettingsConfigDict(
        env_file=(dotenv_file_local, dotenv_file_production), extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
