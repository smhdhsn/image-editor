from __future__ import annotations
from typing import List
from models import Image, Filter


class FilterBuilder:
    def __init__(self, image: Image) -> None:
        self.filters: List[Filter] = []
        self.image: Image = image

    def register(self, *filters: Filter) -> None:
        self.filters.extend(filter() for filter in filters)

    def apply(self) -> Image:
        cv2_image = self.image.load().copy()
        for filter in self.filters:
            cv2_image = filter.apply(cv2_image)

        self.image.reload(cv2_image)
        return self.image
