import cv2
import numpy as np
from builders import Editor
from models import Image
from models.filters import (
    Morphology,
    GrayScale,
    Smooth,
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
    image = Image("./images/coins_and_seeds_1.jpg")

    coin_contours = get_single_coin_contours()

    e = Editor(image)
    e.add_layer(
        GrayScale(),
        Smooth(3),
        Morphology((3, 3)),
        Canny(100, 200),
    ).apply()

    contours, _ = cv2.findContours(
        image.load(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE,
    )

    image.reload()
    for c in contours:
        similarity = cv2.matchShapes(coin_contours, c, 3, 0.0)

        if similarity < 0.15:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image.load(), (x, y), (x + h, y + w), (0, 0, 255), 5)

    image.show()
    image.store()


def get_single_coin_contours() -> np.ndarray:
    image = Image("./images/coin_1.jpg")

    e = Editor(image)
    e.add_layer(
        GrayScale(),
        Smooth(3),
        Morphology((3, 3)),
        Canny(50, 200),
    ).apply()

    contours, _ = cv2.findContours(
        image.load(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE,
    )

    return contours[0]


if __name__ == "__main__":
    main()
