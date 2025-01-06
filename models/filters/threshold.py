import cv2
from cv2.typing import MatLike
from models import Layer


class Threshold(Layer):
    def __init__(
        self,
        max_val: float,
        threshold: float,
        *,
        type: int = cv2.THRESH_TRUNC,
    ) -> None:
        self.threshold = threshold
        self.max_val = max_val
        self.type = type

    def apply(self, image: MatLike) -> MatLike:
        _, image = cv2.threshold(image, self.threshold, self.max_val, self.type)
        return image
