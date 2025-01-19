import cv2
from builders import Editor
from models import Image
from models.filters import (
    AdaptiveThreshold,
    GaussianBlur,
    Morphology,
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
    image = Image("./images/coins_1.png")

    e = Editor(image)
    edited_image = e.add_layer(
        GrayScale(),
        GaussianBlur((9, 9)),
        AdaptiveThreshold(255, 21, 13),
        Morphology((5, 5), iterations=4),
        Canny(150, 200),
    ).apply()

    contours, _ = cv2.findContours(
        edited_image.load(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE,
    )

    image.reload()
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image.load(), (x, y), (x + h, y + w), (0, 0, 255), 3)

    # image.draw(
    #     lambda img, density: cv2.drawContours(img, contours, -1, (0, 0, 255), density),
    #     draw_on_original=False,
    # )

    image.show()
    image.store()


if __name__ == "__main__":
    main()
