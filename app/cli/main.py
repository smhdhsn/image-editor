import cv2
from builders import Editor
from models import Image
from models.filters import (
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
    image = Image("./images/shapes_1.jpg")

    e = Editor(image)
    edited_image = e.add_layer(
        GrayScale(),
        Canny(50, 200),
    ).apply()

    contours, _ = cv2.findContours(
        edited_image.load(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE,
    )

    image.apply(
        lambda img: cv2.drawContours(img, contours, -1, (255, 0, 0), 2),
    )

    image.show()
    image.store()


if __name__ == "__main__":
    main()
