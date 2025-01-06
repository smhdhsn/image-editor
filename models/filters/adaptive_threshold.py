import cv2
from cv2.typing import MatLike
from models import Layer


class AdaptiveThreshold(Layer):
    def __init__(
        self,
        max_val: float,
        block_size: int,
        constant_subtract: int,
        *,
        adaptive_method: int = cv2.ADAPTIVE_THRESH_MEAN_C,
        threshold_type: int = cv2.THRESH_BINARY,
    ) -> None:
        self.constant_subtract = constant_subtract
        self.adaptive_method = adaptive_method
        self.block_size = block_size
        self.max_val = max_val
        self.threshold_type = threshold_type

    def apply(self, image: MatLike) -> MatLike:
        return cv2.adaptiveThreshold(
            image,
            self.max_val,
            self.adaptive_method,
            self.threshold_type,
            self.block_size,
            self.constant_subtract,
        )
