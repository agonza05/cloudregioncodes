# from os.path import join, dirname, normpath
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


# dotenv_file_local = normpath(join(dirname(__file__), "../.env/.env.local"))
# dotenv_file_production = normpath(join(dirname(__file__), "../.env/.env.prod"))
dotenv_file_local = ".env/.env.local"
dotenv_file_production = ".env/.env.prod"



class Settings(BaseSettings):
    app_base_path: str = "/v1"
    app_name: str = "CloudRegion Codes API"
    app_url: str = "http://localhost"
    admin_email: str = "alberto@agonza.net"
    default_error_message: str = "Item not found."

    model_config = SettingsConfigDict(
        env_file=(dotenv_file_local, dotenv_file_production), extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
