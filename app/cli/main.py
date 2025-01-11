from builders import Editor
from models import Image
from models.filters import (
    MedianBlur,
    GrayScale,
    Canny,
)

# from models.filters import AdaptiveThreshold, AveragingBlur, GaussianBlur, Morphology, Threshold, Denoise, Smooth, Sharp
# from models.operations import Brightness, Resize, Rotate, Flip, Crop
# from models.draw import Rectangle, Circle, Line


def main():
    image = Image("./images/image_2.webp")

    e = Editor(image)

    image = e.add_layer(
        GrayScale(),
        MedianBlur(7),
        Canny(200, 240),
    ).apply()

    image.show()
    image.store()


if __name__ == "__main__":
    main()
