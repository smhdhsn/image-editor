from typing import Tuple
import cv2
from cv2.typing import MatLike
from models import Filter


class GaussianBlur(Filter):
    def __init__(
        self, *, ksize: Tuple[int, int] = (25, 25), sigma_x: float = 10
    ) -> None:
        self.ksize = ksize
        self.sigma_x = sigma_x

    def apply(self, image: MatLike) -> MatLike:
        return cv2.GaussianBlur(image, self.ksize, self.sigma_x)
