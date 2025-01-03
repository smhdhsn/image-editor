from cv2.typing import MatLike
from cv2 import cvtColor as cvt_color, COLOR_BGR2GRAY
from models import Filter


class GrayScale(Filter):
    def apply(self, image: MatLike) -> MatLike:
        return cvt_color(image, COLOR_BGR2GRAY)
