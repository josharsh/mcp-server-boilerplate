import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="VAR_",
        env_file=".env",
        extra="ignore"
    )

    api_key: str = os.getenv("AZURE_OPENAI_API_KEY", "")
    api_base_url: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    deployment: str = os.getenv("AZURE_OPENAI_DEPLOYMENT", "")
    api_version: str = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

settings = ApiSettings()