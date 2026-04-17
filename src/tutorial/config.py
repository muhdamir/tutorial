from pydantic_settings import BaseSettings


class Config(BaseSettings):
    async_db_url: str
    # db_url: str


config = Config() # type: ignore