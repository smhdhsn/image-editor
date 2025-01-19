import cv2
import numpy as np
from models import Layer


class Brightness(Layer):
    def __init__(self, brightness: int) -> None:
        self.brightness = brightness

    def apply(self, image: np.ndarray) -> np.ndarray:
        table = np.ones(image.shape, dtype="uint8") * abs(self.brightness)

        if self.brightness < 0:
            return cv2.subtract(image, table)

        return cv2.add(image, table)
