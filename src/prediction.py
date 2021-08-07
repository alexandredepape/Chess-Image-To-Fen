from os.path import join

import numpy as np
import tensorflow.keras
from PIL import Image, ImageOps

from src.config import PIECES_LABEL_MAP, MODELS_DIRECTORY, PIECE_MODEL_FILENAME


class PiecePredictor:
    def __init__(self):
        model_path = join(MODELS_DIRECTORY, PIECE_MODEL_FILENAME)
        self.model = tensorflow.keras.models.load_model(model_path)

    def predict(self, image):
        rgb_im = image.convert('RGB')

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        size = (224, 224)
        fitted_image = ImageOps.fit(rgb_im, size, Image.ANTIALIAS)
        image_array = np.asarray(fitted_image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array

        prediction_array = self.model.predict(data).flatten()
        # print(prediction_array)

        max_prediction_index = np.argmax(prediction_array)
        return PIECES_LABEL_MAP[max_prediction_index], prediction_array[max_prediction_index]

