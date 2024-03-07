from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str = "localhost"
    db_name: str


settings = Settings()
