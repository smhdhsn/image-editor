import cv2
import numpy as np
from models import Layer


class Threshold(Layer):
    def __init__(
        self,
        threshold: float,
        max_val: float,
        *,
        threshold_type: int = cv2.THRESH_TRUNC,
    ) -> None:
        self.threshold = threshold
        self.max_val = max_val
        self.threshold_type = threshold_type

    def apply(self, image: np.ndarray) -> np.ndarray:
        _, image = cv2.threshold(
            image,
            self.threshold,
            self.max_val,
            self.threshold_type,
        )
        return image
