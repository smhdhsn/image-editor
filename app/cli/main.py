from builders import Editor
from models import Image
from models.filters import (
    AdaptiveThreshold,
    GaussianBlur,
    Morphology,
    GrayScale,
)

# from models.filters import AveragingBlur, MedianBlur, Threshold, Denoise, Smooth, Sharp9
# from models.operations import Brightness, Resize, Rotate, Flip, Crop
# from models.draw import Rectangle, Circle, Line


def main():
    image = Image("./images/image_2.webp")

    e = Editor(image)

    image = e.add_layer(
        GrayScale(),
        GaussianBlur((3, 3)),
        AdaptiveThreshold(255, 3, 5),
        Morphology((2, 2)),
    ).apply()

    image.show()
    image.store()


if __name__ == "__main__":
    main()
