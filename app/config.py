from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    tf_model_epochs: int
    image_size_x: int
    image_size_y: int
    tf_model_file_name: str = "image_classifier.keras"
    loss_plot_file_name: str = "loss_plot.png"
    accuracy_plot_file_name: str = "accuracy_plot.png"

    model_config = ConfigDict(env_file=".env", extra='allow')


settings = Settings()
