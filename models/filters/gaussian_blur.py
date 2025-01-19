from typing import Tuple
import cv2
import numpy as np
from models import Layer


class GaussianBlur(Layer):
    def __init__(
        self,
        kernel_size: Tuple[int, int],
        *,
        sigma_x: float = 0,
    ) -> None:
        self.kernel_size = kernel_size
        self.sigma_x = sigma_x

    def apply(self, image: np.ndarray) -> np.ndarray:
        return cv2.GaussianBlur(image, self.kernel_size, self.sigma_x)
