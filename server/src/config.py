from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent.parent/".env"

class Settings(BaseSettings):
    DB_NAME : str
    DB_PORT : str
    DB_HOST : str
    DB_PASS : str
    DB_USER : str
    @property
    def URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    model_config = SettingsConfigDict(env_file=ENV_FILE)


settings = Settings()