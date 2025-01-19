from typing import Tuple
import cv2
import numpy as np
from models import Layer


class Rectangle(Layer):
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
        line1 = (self.pt1, (self.pt2[0], self.pt1[1]))
        line2 = ((self.pt2[0], self.pt1[1]), self.pt2)
        line3 = (self.pt2, (self.pt1[0], self.pt2[1]))
        line4 = ((self.pt1[0], self.pt2[1]), self.pt1)

        image = cv2.line(image, line1[0], line1[1], self.color, self.thickness)
        image = cv2.line(image, line2[0], line2[1], self.color, self.thickness)
        image = cv2.line(image, line3[0], line3[1], self.color, self.thickness)
        image = cv2.line(image, line4[0], line4[1], self.color, self.thickness)

        return image
