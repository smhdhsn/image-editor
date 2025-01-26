import cv2
import numpy as np
from builders import Editor
from models import Image
from models.filters import (
    MedianBlur,
    GrayScale,
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

    e = Editor(image)
    e.add_layer(
        GrayScale(),
        MedianBlur(15),
    ).apply()

    circles = cv2.HoughCircles(image.load(), cv2.HOUGH_GRADIENT, 1.2, 25)

    image.reload()
    for i in np.uint16(np.around(circles[0, :])):
        cv2.circle(image.load(), (i[0], i[1]), i[2], (0, 255, 255), 10)

    image.show()
    image.store()


if __name__ == "__main__":
    main()
