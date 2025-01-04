from typing import Tuple
import cv2
from cv2.typing import MatLike
from models import Operation


class Circle(Operation):
    def __init__(
        self,
        center: Tuple[int, int],
        radius: int,
        *,
        color: Tuple[int, int, int] = (0, 0, 0),
        thickness: int = 5,
    ) -> None:
        self.center = center
        self.radius = radius
        self.thickness = thickness
        self.color = color

    def apply(self, image: MatLike) -> MatLike:
        return cv2.circle(image, self.center, self.radius, self.color, self.thickness)
