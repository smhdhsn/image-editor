import cv2
import numpy as np
from builders import Editor
from models import Image
from models.filters import (
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
    image = Image("./images/road_1.webp")

    e = Editor(image)
    e.add_layer(
        GrayScale(),
        Smooth(6),
        Canny(100, 200),
    ).apply()

    lines = cv2.HoughLines(
        image.load(),
        1,
        np.pi / 180,
        255,
    )

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)

        x0 = a * rho
        y0 = b * rho

        y1 = int(y0 + 1000 * (a))
        x1 = int(x0 + 1000 * (-b))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(image.load(), (x1, y1), (x2, y2), (255, 0, 0), 2)

    image.show()
    image.store()


if __name__ == "__main__":
    main()
