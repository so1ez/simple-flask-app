from pydantic import BaseSettings


class Settings(BaseSettings):
    """Настройки веб-приложения"""
    BIRTHDAY_YEAR: int
    BIRTHDAY_MONTH: int
    BIRTHDAY_DAY: int
    NAME: str

    class Config:
        env_file = '.env'

SETTINGS = Settings()