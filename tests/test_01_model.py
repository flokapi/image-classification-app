import app.cnn.cnn_model as cnn


def test_model_creation():
    model, props = cnn.prepare_model()

    print(props)
    print("#### Model properties")
    print(f"#### Precision: {props['precision']}")
    print(f"#### Accuracy: {props['accuracy']}")
    print(f"#### Recall: {props['recall']}")

    assert props["precision"] > 0.85
    assert props["accuracy"] > 0.85
    assert props["recall"] > 0.85
