import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="VAR_",
        env_file=".env",
        extra="ignore"
    )

    api_key: str
    api_base_url: str = ""

settings = ApiSettings()
