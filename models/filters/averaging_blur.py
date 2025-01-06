from typing import Tuple
import cv2
from cv2.typing import MatLike
from models import Layer


class AveragingBlur(Layer):
    def __init__(self, kernel_size: Tuple[int, int]) -> None:
        self.kernel_size = kernel_size

    def apply(self, image: MatLike) -> MatLike:
        return cv2.blur(image, self.kernel_size)
