from typing import Tuple
import cv2
from cv2.typing import MatLike
from models import Layer


class GaussianBlur(Layer):
    def __init__(
        self,
        kernel_size: Tuple[int, int],
        *,
        sigma_x: float = 10,
    ) -> None:
        self.kernel_size = kernel_size
        self.sigma_x = sigma_x

    def apply(self, image: MatLike) -> MatLike:
        return cv2.GaussianBlur(image, self.kernel_size, self.sigma_x)
