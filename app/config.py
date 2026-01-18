from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file = ".env", env_file_encoding = "utf-8")

config = Settings()
