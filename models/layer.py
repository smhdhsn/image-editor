from abc import ABC, abstractmethod
from cv2.typing import MatLike


class Layer(ABC):
    @abstractmethod
    def apply(self, image: MatLike) -> MatLike:
        pass
