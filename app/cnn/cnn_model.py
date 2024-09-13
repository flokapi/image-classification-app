import tensorflow as tf

from app.config import settings


MODEL_PATH = settings.tf_model_path
TF_MODEL_EPOCHS = settings.tf_model_epochs
IMAGE_SIZE_X = settings.image_size_x
IMAGE_SIZE_Y = settings.image_size_y


def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, kernel_size=(
            3, 3), activation='relu', input_shape=(IMAGE_SIZE_X, IMAGE_SIZE_Y, 1)),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


def train_model(model, x_train, y_train, x_test, y_test, epochs=TF_MODEL_EPOCHS):
    model.fit(x_train, y_train, validation_data=(
        x_test, y_test), epochs=epochs)


def init():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]

    print("================== creating model")
    model = create_model()
    train_model(model, x_train, y_train, x_test, y_test)
    model.save(MODEL_PATH)


if __name__ == "__main__":
    init()
