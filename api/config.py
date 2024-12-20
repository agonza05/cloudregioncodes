from os.path import join, dirname, normpath

from pydantic_settings import BaseSettings, SettingsConfigDict


dotenv_file_local = normpath(join(dirname(__file__), "../.env/.env.local"))
dotenv_file_production = normpath(join(dirname(__file__), "../.env/.env.prod"))

class Settings(BaseSettings):
    app_name: str = "Cloudregion Codes API"
    app_url: str = "http://localhost"
    admin_email: str = "alberto@agonza.net"

    model_config = SettingsConfigDict(env_file=(dotenv_file_local, dotenv_file_production), extra="ignore")

class CodeConfig(BaseSettings):
    app_base_path: str = "/api/v1"

code_config = CodeConfig()
