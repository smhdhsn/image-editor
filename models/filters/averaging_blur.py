from typing import Tuple
import cv2
from cv2.typing import MatLike
from models import Layer


class AveragingBlur(Layer):
    def __init__(self, *, ksize: Tuple[int, int] = (25, 25)) -> None:
        self.ksize = ksize

    def apply(self, image: MatLike) -> MatLike:
        return cv2.blur(image, self.ksize)
