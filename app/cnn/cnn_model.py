from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dense, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from app.config import settings


TF_MODEL_PATH = settings.tf_model_path
TF_MODEL_EPOCHS = settings.tf_model_epochs
IMAGE_SIZE_X = settings.image_size_x
IMAGE_SIZE_Y = settings.image_size_y


# Load and prepare data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(
    (x_train.shape[0], IMAGE_SIZE_X, IMAGE_SIZE_Y, 1)).astype('float32') / 255
x_test = x_test.reshape(
    (x_test.shape[0], IMAGE_SIZE_X, IMAGE_SIZE_Y, 1)).astype('float32') / 255
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=False,  # Not applicable for MNIST but can be useful for other datasets
    fill_mode='nearest'
)
datagen.fit(x_train)

# Build the improved CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.25),

    Conv2D(64, (3, 3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.25),

    Conv2D(128, (3, 3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.25),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model with data augmentation
model.fit(datagen.flow(x_train, y_train, batch_size=64),
          epochs=TF_MODEL_EPOCHS,
          validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

model.save(TF_MODEL_PATH)


# import tensorflow as tf

# MODEL_PATH = settings.tf_model_path
# TF_MODEL_EPOCHS = settings.tf_model_epochs
# IMAGE_SIZE_X = settings.image_size_x
# IMAGE_SIZE_Y = settings.image_size_y


# def create_model():
#     model = tf.keras.Sequential([
#         tf.keras.layers.Conv2D(32, kernel_size=(
#             3, 3), activation='relu', input_shape=(IMAGE_SIZE_X, IMAGE_SIZE_Y, 1)),
#         tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
#         tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
#         tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
#         tf.keras.layers.Flatten(),
#         tf.keras.layers.Dense(128, activation='relu'),
#         tf.keras.layers.Dense(10, activation='softmax')
#     ])

#     model.compile(optimizer='adam',
#                   loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#     return model


# def train_model(model, x_train, y_train, x_test, y_test, epochs=TF_MODEL_EPOCHS):
#     model.fit(x_train, y_train, validation_data=(
#         x_test, y_test), epochs=epochs)


# def init():
#     (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
#     x_train, x_test = x_train / 255.0, x_test / 255.0
#     x_train = x_train[..., tf.newaxis]
#     x_test = x_test[..., tf.newaxis]

#     print("================== creating model")
#     model = create_model()
#     train_model(model, x_train, y_train, x_test, y_test)
#     model.save(MODEL_PATH)


# if __name__ == "__main__":
#     init()
