import cv2
from cv2.typing import MatLike
from models import Layer


class MedianBlur(Layer):
    def __init__(self, kernel_size: int) -> None:
        self.kernel_size = kernel_size

    def apply(self, image: MatLike) -> MatLike:
        return cv2.medianBlur(image, self.kernel_size)
