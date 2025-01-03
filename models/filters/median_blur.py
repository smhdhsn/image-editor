from cv2.typing import MatLike
from cv2 import medianBlur as median_blur
from models import Filter


class MedianBlur(Filter):
    def __init__(self, *, ksize: int = 25) -> None:
        self.ksize = ksize

    def apply(self, image: MatLike) -> MatLike:
        return median_blur(image, self.ksize)
