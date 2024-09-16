from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    tf_model_file_name: str
    tf_model_epochs: int
    image_size_x: int
    image_size_y: int
    static_files_location: str
    loss_plot_file_name: str
    accuracy_plot_file_name: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
