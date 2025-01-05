import cv2
from cv2.typing import MatLike
from models import Layer

VERTICAL = 0
HORIZONTAL = 1


class Flip(Layer):
    def __init__(self, direction: int = HORIZONTAL) -> None:
        self.direction = direction

    def apply(self, image: MatLike) -> MatLike:
        return cv2.flip(image, self.direction)
