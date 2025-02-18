from typing import Tuple
import numpy as np
from models import Layer


class Crop(Layer):
    def __init__(self, pt1: Tuple[int, int], pt2: Tuple[int, int]) -> None:
        self.pt1 = pt1
        self.pt2 = pt2

    def apply(self, image: np.ndarray) -> np.ndarray:
        return image[self.pt1[0] : self.pt2[0], self.pt1[1] : self.pt2[1]]
