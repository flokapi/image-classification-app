import matplotlib.pyplot as plt
import io
import base64
from app.templates import templates
import random


def plot():
    fig, ax = plt.subplots()
    ax.plot(
        [random.random() for _ in range(100)],
        [random.random() for _ in range(100)],
    )

    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return base64.b64encode(img_buffer.read()).decode("utf-8")
