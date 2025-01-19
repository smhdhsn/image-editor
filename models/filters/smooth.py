import cv2
import numpy as np
from models import Layer


class Smooth(Layer):
    def __init__(
        self,
        diameter: int,
        *,
        sigma_color: int = 75,
        sigma_space: int = 75,
    ) -> None:
        self.sigma_color = sigma_color
        self.sigma_space = sigma_space
        self.diameter = diameter

    def apply(self, image: np.ndarray) -> np.ndarray:
        return cv2.bilateralFilter(
            image,
            self.diameter,
            self.sigma_color,
            self.sigma_space,
        )
