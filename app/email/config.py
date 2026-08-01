from pydantic_settings import BaseSettings, SettingsConfigDict


class EmailSettings(BaseSettings):

    MAIL_USERNAME: str

    MAIL_PASSWORD: str

    MAIL_SERVER: str = "smtp.gmail.com"

    MAIL_PORT: int = 587

    MAIL_FROM: str

    MAIL_STARTTLS: bool = True

    MAIL_SSL_TLS: bool = False


    model_config = SettingsConfigDict(

        env_file=".env",

        extra="ignore"

    )



email_settings = EmailSettings()