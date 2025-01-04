from typing import Tuple
import cv2
from cv2.typing import MatLike
from models import Layer


class Rotate(Layer):
    def __init__(
        self,
        angle: float,
        *,
        pivot_point: Tuple[int, int] = None,
        scale: float = 1,
    ) -> None:
        self.pivot_point = pivot_point
        self.angle = angle
        self.scale = scale

    def apply(self, image: MatLike) -> MatLike:
        pivot_point = (
            (image.shape[0] / 2, image.shape[1] / 2)
            if self.pivot_point is None
            else self.pivot_point
        )
        rotation_matrix = cv2.getRotationMatrix2D(pivot_point, self.angle, self.scale)

        return cv2.warpAffine(image, rotation_matrix, image.shape[:2])
