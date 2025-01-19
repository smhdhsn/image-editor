import cv2
import numpy as np
from models import Layer


class MedianBlur(Layer):
    def __init__(self, kernel_size: int) -> None:
        self.kernel_size = kernel_size

    def apply(self, image: np.ndarray) -> np.ndarray:
        return cv2.medianBlur(image, self.kernel_size)
