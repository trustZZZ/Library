from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from os.path import join, dirname

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=join(dirname(__file__), ".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",)
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    LOG_LEVEL: Literal['INFO', 'DEBUG', 'ERROR']

settings = Settings()
