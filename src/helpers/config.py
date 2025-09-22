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

    GENERATION_BACKEND: str
    EMBEDDING_BACKEND : str

    OPENAI_API_KEY:str=None
    COHERE_API_KEY: str=None
    OPENAI_API_URL:str=None

    GENERATION_MODEL_ID: str=None
    EMBEDDING_MODEL_ID: str=None
    EMBEDDING_MODEL_SIZE:int=None

    INPUT_DAFAULT_MAX_CHARACTERS: int=None
    GENERATION_DAFAULT_MAX_TOKENS: int=None
    GENERATION_DAFAULT_TEMPERATURE: float=None
    
    VECTOR_DB_BACKEND:str
    VECTOR_DB_PATH:str
    VECTOR_DB_DISTANCE_METHOD:str=None
    
    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()
