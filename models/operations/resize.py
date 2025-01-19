from typing import Tuple
import cv2
import numpy as np
from models import Layer


class Resize(Layer):
    def __init__(
        self,
        shape: Tuple[int, int] | int,
        *,
        method: int = cv2.INTER_AREA,
    ) -> None:
        self.method = method
        self.shape = shape

    def apply(self, image: np.ndarray) -> np.ndarray:
        if isinstance(self.shape, int):
            return self._resize_using_factor(image)

        return self._resize_exact(image)

    def _resize_using_factor(self, image: np.ndarray) -> np.ndarray:
        return cv2.resize(
            image,
            None,
            self.method,
            fx=self.shape,
            fy=self.shape,
            interpolation=self.method,
        )

    def _resize_exact(self, image: np.ndarray) -> np.ndarray:
        return cv2.resize(
            image,
            self.shape,
            self.method,
            interpolation=self.method,
        )
