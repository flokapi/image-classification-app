from tensorflow.keras.models import load_model
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from tensorflow.keras.models import Sequential
from matplotlib import pyplot as plt
import numpy as np
import imghdr
import cv2
import tensorflow as tf
import os
from pathlib import Path


from app.config import settings


FILES_LOCATION = Path(settings.files_location)
TF_MODEL_PATH = FILES_LOCATION.joinpath(settings.tf_model_file_name)
LOSS_PLOT_PATH = FILES_LOCATION.joinpath(settings.loss_plot_file_name)
ACCURACY_PLOT_PATH = FILES_LOCATION.joinpath(settings.accuracy_plot_file_name)
TF_MODEL_EPOCHS = settings.tf_model_epochs
IMAGE_SIZE_X = settings.image_size_x
IMAGE_SIZE_Y = settings.image_size_y

TRAIN_DATA_DIR = "data"
LOG_DATA_DIR = "log"
SUPPORTED_IMAGES_EXT = ['jpeg', 'jpg', 'bmp', 'png']


def init_hardware():
    # Avoid OOM errors by setting GPU Memory Consumption Growth
    gpus = tf.config.experimental.list_physical_devices('GPU')
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

    tf.config.list_physical_devices('GPU')


def init_data():
    data_dir = TRAIN_DATA_DIR
    images_ext = SUPPORTED_IMAGES_EXT

    def check_data():
        for image_class in os.listdir(data_dir):
            for image in os.listdir(os.path.join(data_dir, image_class)):
                image_path = os.path.join(data_dir, image_class, image)
                try:
                    img = cv2.imread(image_path)
                    tip = imghdr.what(image_path)
                    if tip not in images_ext:
                        print('Image not in ext list {}'.format(image_path))
                        os.remove(image_path)
                except Exception as e:
                    print('Issue with image {}'.format(image_path))
                    # os.remove(image_path)

    def load_data():
        data = tf.keras.utils.image_dataset_from_directory(data_dir)

        data_iterator = data.as_numpy_iterator()

        batch = data_iterator.next()

        # fig, ax = plt.subplots(ncols=4, figsize=(20, 20))
        # for idx, img in enumerate(batch[0][:4]):
        #     ax[idx].imshow(img.astype(int))
        #     ax[idx].title.set_text(batch[1][idx])

        return data

    def scale_data(data):
        data = data.map(lambda x, y: (x/255, y))

        data.as_numpy_iterator().next()

    def split_data(data):

        train_size = int(len(data)*.7)
        val_size = int(len(data)*.2)
        test_size = int(len(data)*.1)

        train_size

        train_data = data.take(train_size)
        validation_data = data.skip(train_size).take(val_size)
        test_data = data.skip(train_size+val_size).take(test_size)

        return train_data, test_data, validation_data

    check_data()
    data = load_data()
    scale_data(data)
    return split_data(data)


def create_model():
    im_size_x = IMAGE_SIZE_X
    im_size_y = IMAGE_SIZE_Y

    model = Sequential()

    model.add(Conv2D(16, (3, 3), 1, activation='relu',
                     input_shape=(im_size_x, im_size_y, 3)))
    model.add(MaxPooling2D())
    model.add(Conv2D(32, (3, 3), 1, activation='relu'))
    model.add(MaxPooling2D())
    model.add(Conv2D(16, (3, 3), 1, activation='relu'))
    model.add(MaxPooling2D())
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile('adam', loss=tf.losses.BinaryCrossentropy(),
                  metrics=['accuracy'])

    model.summary()

    return model


def fit_model(model, train_data, validation_data):
    log_dir = LOG_DATA_DIR
    nb_epochs = TF_MODEL_EPOCHS

    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)
    hist = model.fit(train_data,
                     epochs=nb_epochs,
                     validation_data=validation_data,
                     callbacks=[tensorboard_callback])

    return hist


def evaluate_model_props(hist, test_data, model):
    loss_plot_path = LOSS_PLOT_PATH
    accuracy_plot_path = ACCURACY_PLOT_PATH

    fig, ax = plt.subplots()
    ax.plot(hist.history['loss'], color='teal', label='loss')
    ax.plot(hist.history['val_loss'], color='orange', label='val_loss')
    ax.set_title('Loss', fontsize=20)
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    plt.legend(loc="upper left")
    plt.tight_layout()
    fig.savefig(loss_plot_path)
    # plt.show()

    fig, ax = plt.subplots()
    ax.plot(hist.history['accuracy'], color='teal', label='accuracy')
    ax.plot(hist.history['val_accuracy'], color='orange', label='val_accuracy')
    ax.set_title('Accuracy', fontsize=20)
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Accuracy')
    plt.legend(loc="upper left")
    plt.tight_layout()
    fig.savefig(accuracy_plot_path)
    # plt.show()

    pre = Precision()
    re = Recall()
    acc = BinaryAccuracy()

    for batch in test_data.as_numpy_iterator():
        X, y = batch
        yhat = model.predict(X)
        pre.update_state(y, yhat)
        re.update_state(y, yhat)
        acc.update_state(y, yhat)

    # print(pre.result(), re.result(), acc.result())

    model_properties = {
        "precision": pre.result(),
        "recall": re.result(),
        "accuracy": acc.result()
    }

    return model_properties


def make_prediction(image_path):
    img = cv2.imread(image_path)
    plt.imshow(img)
    plt.show()

    resize = tf.image.resize(img, (256, 256))
    plt.imshow(resize.numpy().astype(int))
    plt.show()

    yhat = model.predict(np.expand_dims(resize/255, 0))

    if yhat > 0.5:
        print(f'Predicted class is Sad')
    else:
        print(f'Predicted class is Happy')


def prepare_model():
    init_hardware()
    train_data, test_data, validation_data = init_data()
    model = create_model()
    hist = fit_model(model, train_data, validation_data)
    evaluate_model_props(hist, test_data, model)
    model.save(TF_MODEL_PATH)
    return model


if __name__ == "__main__":
    prepare_model()
