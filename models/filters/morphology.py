from typing import Tuple
import numpy as np
import cv2
from cv2.typing import MatLike
from models import Layer

MORPHOLOGY_DIALATION = 0
"""
Adds pixels to the boundaries of objects in an image.
"""

MORPHOLOGY_EROSION = 1
"""
Removes pixels at the boundaries of objects in an image.
"""

MORPHOLOGY_OPENING = 2
"""
Erosion followed by dilation.
"""

MORPHOLOGY_CLOSING = 3
"""
Dilation followed by erosion.
"""


class Morphology(Layer):
    def __init__(
        self,
        kernel: Tuple[int, int],
        *,
        mode: int = MORPHOLOGY_EROSION,
        iterations: int = 1,
    ) -> None:
        self.kernel = np.ones(kernel, np.uint8)
        self.iterations = iterations
        self.mode = mode

    def apply(self, image: MatLike) -> MatLike:
        match self.mode:
            case 0:
                return self._dialate(image)

            case 1:
                return self._erode(image)

            case 2:
                return self._open(image)

            case 3:
                return self._close(image)

            case _:
                raise ValueError("Wrong mode.")

    def _dialate(self, image: MatLike) -> MatLike:
        return cv2.dilate(
            image,
            self.kernel,
            iterations=self.iterations,
        )

    def _erode(self, image: MatLike) -> MatLike:
        return cv2.erode(
            image,
            self.kernel,
            iterations=self.iterations,
        )

    def _open(self, image: MatLike) -> MatLike:
        return cv2.morphologyEx(
            image,
            cv2.MORPH_OPEN,
            self.kernel,
            iterations=self.iterations,
        )

    def _close(self, image: MatLike) -> MatLike:
        return cv2.morphologyEx(
            image,
            cv2.MORPH_CLOSE,
            self.kernel,
            iterations=self.iterations,
        )
