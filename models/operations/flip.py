import cv2
import numpy as np
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

    def apply(self, image: np.ndarray) -> np.ndarray:
        return cv2.flip(image, self.direction)
