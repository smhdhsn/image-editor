import cv2
import numpy as np
from models import Layer


class Canny(Layer):
    def __init__(self, min_value: int, max_value: int, *, kernel_size: int = 3) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.kernel_size = kernel_size

    def apply(self, image: np.ndarray) -> np.ndarray:
        return cv2.Canny(
            image,
            self.min_value,
            self.max_value,
            apertureSize=self.kernel_size,
        )
