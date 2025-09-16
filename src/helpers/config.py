from typing import List, ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    # هنا بنستخدم List بدل list[str] عشان 3.8
    FILE_ALLOWED_TYPES: List[str] = ["pdf", "docx", "txt"]
    FILE_MAX_SIZE: int = 10
    FILE_DEFAULT_CHUNCK_SIZE:int=512000
    MONGODB_URL: str
    MONGODB_DATABASE: str

    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()
