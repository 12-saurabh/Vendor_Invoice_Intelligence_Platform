from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Vendor Invoice Intelligence Platform"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str

    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()