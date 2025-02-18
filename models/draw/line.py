from typing import Tuple
import cv2
import numpy as np
from models import Layer


class Line(Layer):
    def __init__(
        self,
        pt1: Tuple[int, int],
        pt2: Tuple[int, int],
        *,
        color: Tuple[int, int, int] = (0, 0, 0),
        thickness: int = 5,
    ) -> None:
        self.thickness = thickness
        self.color = color
        self.pt1 = pt1
        self.pt2 = pt2

    def apply(self, image: np.ndarray) -> np.ndarray:
        return cv2.line(image, self.pt1, self.pt2, self.color, self.thickness)
