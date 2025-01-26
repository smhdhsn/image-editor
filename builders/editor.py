from __future__ import annotations
from typing import List
from models import Layer, Image


class Editor:
    def __init__(self) -> None:
        self.layers: List[Layer] = []
        self.image: Image = None

    def add_layer(self, *layers: Layer) -> Editor:
        self.layers.extend(layers)
        return self

    def apply(self, image: Image) -> Image:
        cp_image = image.copy()

        cv2_image = cp_image.load()

        for layer in self.layers:
            cv2_image = layer.apply(cv2_image)

        cp_image.reload(cv2_image)

        return cp_image
