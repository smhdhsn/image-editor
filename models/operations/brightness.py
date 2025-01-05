import numpy as np
import cv2
from cv2.typing import MatLike
from models import Layer


class Brightness(Layer):
    def __init__(self, brightness: int) -> None:
        self.brightness = brightness

    def apply(self, image: MatLike) -> MatLike:
        table = np.ones(image.shape, dtype="uint8") * abs(self.brightness)

        if self.brightness < 0:
            return cv2.subtract(image, table)

        return cv2.add(image, table)
