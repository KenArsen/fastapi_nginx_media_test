from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    API_PORT: int = 8000
    API_HOST: str = "0.0.0.0"

    NGINX_PORT: int = 81

settings = Settings()