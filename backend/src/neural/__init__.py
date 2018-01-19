import tensorflow as tf
from keras.models import load_model
from .moleimages import MoleImages
from .. import cfg

mimg = MoleImages()
graph = tf.get_default_graph()
model = load_model(cfg.keras_model_path)


def predict_image(path_to_file):
    X = mimg.load_image(path_to_file)
    with graph.as_default():
        y_pred = model.predict(X)[0, 0]
    return y_pred
