from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    tf_model_path: str
    tf_model_epochs: int
    image_size_x: int
    image_size_y: int

    model_config = ConfigDict(env_file=".env")


settings = Settings()
