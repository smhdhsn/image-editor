from typing import Tuple
from cv2.typing import MatLike
from cv2 import GaussianBlur as gaussian_blur
from models import Filter


class GaussianBlur(Filter):
    def __init__(
        self, *, ksize: Tuple[int, int] = (25, 25), sigmaX: float = 10
    ) -> None:
        self.ksize = ksize
        self.sigmaX = sigmaX

    def apply(self, image: MatLike) -> MatLike:
        return gaussian_blur(image, self.ksize, self.sigmaX)
