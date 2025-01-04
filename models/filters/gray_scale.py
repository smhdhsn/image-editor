import cv2
from cv2.typing import MatLike
from models import Layer


class GrayScale(Layer):
    def apply(self, image: MatLike) -> MatLike:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
