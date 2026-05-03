from pathlib import Path
from pydantic_settings import BaseSettings,SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parent.parent.parent.parent/"envs/.env.bot"

class BotSettings(BaseSettings):
    API_TOKEN : str
    model_config = SettingsConfigDict(env_file=ENV_FILE)

bot_settings = BotSettings()

