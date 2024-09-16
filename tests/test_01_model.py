

import app.cnn.cnn_model as cnn


def test_train_data():
    cnn.init_hardware()
    train_data, test_data, validation_data = cnn.init_data()
    model = cnn.create_model()
    hist = cnn.fit_model(model, train_data, validation_data)
    props = cnn.evaluate_model_props(hist, test_data, model)
    print(props)
    # [todo]: extract and check model properties
    assert True
