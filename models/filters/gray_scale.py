import cv2
from cv2.typing import MatLike
from models import Layer


class GrayScale(Layer):
    def __init__(self, *, code: int = cv2.COLOR_BGR2GRAY) -> None:
        self.code = code

    def apply(self, image: MatLike) -> MatLike:
        return cv2.cvtColor(image, self.code)
