import numpy as np
import cv2
from cv2.typing import MatLike
from models import Layer


class Sharp(Layer):
    def __init__(self, *, ddepth: int = -1, kernel: np.typing.NDArray = None) -> None:
        self.ddepth = ddepth
        self.kernel = (
            kernel
            if kernel is not None
            else np.array(
                [
                    [-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1],
                ]
            )
        )

    def apply(self, image: MatLike) -> MatLike:
        return cv2.filter2D(image, self.ddepth, self.kernel)
