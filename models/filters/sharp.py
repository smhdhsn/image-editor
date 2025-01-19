import cv2
import numpy as np
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

    def apply(self, image: np.ndarray) -> np.ndarray:
        return cv2.filter2D(image, self.ddepth, self.kernel)
