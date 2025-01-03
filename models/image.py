from cv2.typing import MatLike
import cv2


class Image:
    def __init__(self, file_path: str) -> None:
        self.image_path: str = file_path
        self.image: MatLike = None

    def reload(self, image: MatLike) -> None:
        self.image = image

    def load(self) -> MatLike:
        if self.image is None:
            self.image: MatLike = cv2.imread(self.image_path)

        return self.image

    def show(self, *, show_details: bool = True) -> None:
        image = self._write_on_image() if show_details else self.image
        cv2.imshow(self.get_name(), image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_name(self) -> str:
        return self.image_path.split("/")[-1].split(".")[0]

    def get_type(self) -> str:
        return self.image_path.split(".")[-1]

    def get_details(self) -> None:
        width, height = self.image.shape[0], self.image.shape[1]
        return f"Width:{width}, Height:{height}"

    def _write_on_image(self) -> MatLike:
        return cv2.putText(
            img=self.image.copy(),
            text=self.get_details(),
            org=(
                int(self.image.shape[0] / 100),
                int(self.image.shape[1] - (self.image.shape[1] / 100)),
            ),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,
            color=(0, 0, 0),
            thickness=1,
            lineType=cv2.LINE_AA,
        )

    def store(self) -> None:
        cv2.imwrite(f"./out/{self.get_name()}.{self.get_type()}", self.image)
