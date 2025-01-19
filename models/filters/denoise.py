import cv2
import numpy as np
from models import Layer


class Denoise(Layer):
    def __init__(
        self,
        h: float,
        h_color: float,
        template_window_size: float,
        search_window_size: float,
    ) -> None:
        self.template_window_size = template_window_size
        self.search_window_size = search_window_size
        self.h_color = h_color
        self.h = h

    def apply(self, image: np.ndarray) -> np.ndarray:
        if len(image.shape) == 3:
            return cv2.fastNlMeansDenoisingColored(
                image,
                None,
                self.h,
                self.h_color,
                self.template_window_size,
                self.search_window_size,
            )

        return cv2.fastNlMeansDenoising(
            image,
            None,
            self.h,
            self.template_window_size,
            self.search_window_size,
        )
