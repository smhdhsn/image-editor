import cv2
import numpy as np
from builders import Editor
from models import Image
from models.filters import (
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
    e = get_editor()
    main_image = e.apply(Image("./images/waldo_on_beach_1.jpg"))
    tmpl_image = e.apply(Image("./images/waldo_1.jpg"))

    result = cv2.matchTemplate(
        main_image.load(),
        tmpl_image.load(),
        cv2.TM_CCOEFF,
    )

    main_image.reload()

    _, _, _, max_loc = cv2.minMaxLoc(result)

    top_left = max_loc
    cv2.rectangle(
        main_image.load(),
        top_left,
        (top_left[0] + 50, top_left[1] + 50),
        (0, 0, 0),
        5,
    )

    main_image.show()


def get_editor() -> Editor:
    e = Editor()

    return e.add_layer(
        GrayScale(),
    )


if __name__ == "__main__":
    main()
