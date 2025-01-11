import cv2
from cv2.typing import MatLike
from models import Layer

FLIP_VERTICAL = 0
"""
Flip the image along the vertical axis. 
"""

FLIP_HORIZONTAL = 1
"""
Flip the image along the horizontal axis. 
"""


class Flip(Layer):
    def __init__(self, direction: int = FLIP_HORIZONTAL) -> None:
        self.direction = direction

    def apply(self, image: MatLike) -> MatLike:
        return cv2.flip(image, self.direction)
