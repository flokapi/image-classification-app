import matplotlib.pyplot as plt
import io
import base64


predictions = []


# --------------------- private

def format_label(text):
    if len(text) > 20:
        return f"{text[:10]}...{text[-6:]}"
    else:
        return text


# --------------------- public


def add_prediction(new_prediction):
    # predictions.append(new_prediction)
    predictions.insert(0, new_prediction)


def plot():
    x = [-i for i in range(len(predictions))]
    y = [p[1] for p in predictions]

    fig, ax = plt.subplots()
    ax.plot(
        x,
        y,
        marker='o',
        linestyle='None',
        markersize=10.0
    )
    ax.set_title('Last evaluations')
    ax.set_xlabel('Images')
    ax.set_ylabel('Prediction')
    ax.set_xlim([-21, 1])
    ax.set_ylim([-0.1, 2])

    ax.set_xticks([-2*i for i in range(11)])
    ax.set_yticks([-0, 1])
    ax.set_yticklabels(["Happy", "Sad"])

    plt.axhline(y=0, color="gray", linestyle='--', linewidth=0.5)
    plt.axhline(y=0.5, color="gray", linestyle='--', linewidth=0.5)
    plt.axhline(y=1, color="gray", linestyle='--', linewidth=0.5)

    for i in range(len(predictions)):
        text = format_label(predictions[i][0])
        ax.annotate(text, (x[i], y[i]+0.1), textcoords="offset points", xytext=(
            5, 0), ha='center', rotation=90)

    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    plt.close(fig)

    return base64.b64encode(img_buffer.read()).decode("utf-8")
