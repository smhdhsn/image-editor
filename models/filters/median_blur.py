import cv2
from cv2.typing import MatLike
from models import Filter


class MedianBlur(Filter):
    def __init__(self, *, ksize: int = 25) -> None:
        self.ksize = ksize

    def apply(self, image: MatLike) -> MatLike:
        return cv2.medianBlur(image, self.ksize)
