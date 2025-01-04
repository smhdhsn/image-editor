from __future__ import annotations
from typing import List
from models import Operation, Filter, Image


class Editor:
    def __init__(self, image: Image) -> None:
        self.operations: List[Operation] = []
        self.filters: List[Filter] = []
        self.image: Image = image

    def add_operations(self, *operations: Operation) -> Editor:
        self.operations.extend(operations)
        return self

    def add_filters(self, *filters: Filter) -> Editor:
        self.filters.extend(filters)
        return self

    def apply(self) -> Image:
        cv2_image = self.image.load().copy()

        for fltr in self.filters:
            cv2_image = fltr.apply(cv2_image)

        for opr in self.operations:
            cv2_image = opr.apply(cv2_image)

        self.image.reload(cv2_image)
        return self.image
