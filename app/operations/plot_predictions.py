import matplotlib.pyplot as plt
import io
import base64
from app.templates import templates
import random


predictions = []


def add_prediction(new_prediction):
    predictions.append(new_prediction)


def plot():
    x = [i for i in range(len(predictions))]
    y = [p[1] for p in predictions]

    fig, ax = plt.subplots()
    ax.plot(
        x,
        y,
        marker='o',
        linestyle='None',
        markersize=10.0
    )
    ax.set_title('Evaluations')
    ax.set_xlabel('Images')
    ax.set_ylabel('Prediction')
    ax.set_ylim([0, 2])

    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Happy", "Sad"])

    for i in range(len(predictions)):
        ax.annotate(predictions[i][0], (x[i], y[i]+0.1), textcoords="offset points", xytext=(
            5, 0), ha='center', rotation=90)

    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    plt.close(fig)

    return base64.b64encode(img_buffer.read()).decode("utf-8")
