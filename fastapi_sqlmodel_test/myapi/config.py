from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    storage_dir: str

    class Config:
        env_file = ".env"


settings = Settings()
