import cv2
from cv2.typing import MatLike
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

    def apply(self, image: MatLike) -> MatLike:
        return cv2.bilateralFilter(
            image,
            self.diameter,
            self.sigma_color,
            self.sigma_space,
        )
