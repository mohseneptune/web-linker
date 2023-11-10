from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Envariables(BaseSettings):
    # Application Settings
    BASE_DIRECTORY: Path = Path(__file__).resolve().parent.parent.parent
    DEBUG: bool = True
    APP_NAME: str = "WEBLINKER"

    # PostgreSQL Settings
    POSTGRES_DRIVER: str = "postgresql+psycopg"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5433
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"

    # Redis Settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str = ""

    @property
    def postgres_database_uri(self) -> str:
        url = f"{self.POSTGRES_DRIVER}://\
                {self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@\
                {self.POSTGRES_HOST}:{self.POSTGRES_PORT}/\
                {self.POSTGRES_DB}"
        return url.replace(" ", "")

    @property
    def redis_database_uri(self) -> str:
        return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = SettingsConfigDict(
        env_file=BASE_DIRECTORY / ".env",
        env_file_encoding="utf-8",
    )


ENVARIABLES = Envariables()
