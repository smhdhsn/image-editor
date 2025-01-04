from abc import ABC, abstractmethod
from cv2.typing import MatLike


class Operation(ABC):
    @abstractmethod
    def apply(self, image: MatLike) -> MatLike:
        pass
