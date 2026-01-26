from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str
    ADMIN_ID: int
    LOG_LEVEL: str = "DEBUG"
    model_config = SettingsConfigDict(env_file = ".env", env_file_encoding = "utf-8")

config = Settings()
