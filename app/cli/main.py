import cv2
from cv2.typing import MatLike
from builders import Editor
from models import Image
from models.filters import (
    MedianBlur,
    GrayScale,
    Canny,
)

# from models.filters import (
#     AdaptiveThreshold,
#     AveragingBlur,
#     GaussianBlur,
#     MedianBlur,
#     Morphology,
#     Threshold,
#     Denoise,
#     Smooth,
#     Sharp,
# )

# from models.operations import (
#     Brightness,
#     Resize,
#     Rotate,
#     Flip,
#     Crop,
# )

# from models.draw import (
#     Rectangle,
#     Circle,
#     Line,
# )


def main():
    image = Image("./images/licence_plate_2.jpg")

    e = Editor(image)

    image = e.add_layer(
        MedianBlur(11),
        GrayScale(),
        Canny(22, 222),
    ).apply()

    all_contours, _ = cv2.findContours(
        image.load(),
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_NONE,
    )

    ext_contours, _ = cv2.findContours(
        image.load(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE,
    )

    img = cv2.cvtColor(image.load(), cv2.COLOR_GRAY2BGR)

    for c in all_contours:
        cv2.drawContours(img, c, -1, (255, 0, 0), 2)

    for c in ext_contours:
        cv2.drawContours(img, c, -1, (0, 0, 255), 2)

    image.reload(img)

    image.show()
    image.store()


if __name__ == "__main__":
    main()
