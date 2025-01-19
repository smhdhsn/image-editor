from typing import Tuple
import cv2
import numpy as np
from models import Layer


class AveragingBlur(Layer):
    def __init__(self, kernel_size: Tuple[int, int]) -> None:
        self.kernel_size = kernel_size

    def apply(self, image: np.ndarray) -> np.ndarray:
        return cv2.blur(image, self.kernel_size)
