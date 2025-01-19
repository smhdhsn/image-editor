import cv2
import numpy as np
from models import Layer


class GrayScale(Layer):
    def __init__(self, *, code: int = cv2.COLOR_BGR2GRAY) -> None:
        self.code = code

    def apply(self, image: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(image, self.code)
