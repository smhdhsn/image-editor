from __future__ import annotations
from typing import List
from models import Layer, Image


class Editor:
    def __init__(self, image: Image) -> None:
        self.layers: List[Layer] = []
        self.image: Image = image

    def add_layer(self, *layers: Layer) -> Editor:
        self.layers.extend(layers)
        return self

    def apply(self) -> Image:
        cv2_image = self.image.load()

        for layer in self.layers:
            cv2_image = layer.apply(cv2_image)

        self.image.reload(cv2_image)
        return self.image
