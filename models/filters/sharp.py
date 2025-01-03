from cv2.typing import MatLike
from cv2 import filter2D
from numpy.typing import NDArray
from numpy import array
from models import Filter


class Sharp(Filter):
    def __init__(self, *, ddepth: int = -1, kernel: NDArray = None) -> None:
        self.ddepth = ddepth
        self.kernel = (
            kernel
            if kernel is not None
            else array(
                [
                    [-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1],
                ]
            )
        )

    def apply(self, image: MatLike) -> MatLike:
        return filter2D(image, self.ddepth, self.kernel)
