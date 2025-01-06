from builders import Editor
from models import Image
from models.filters import (
    AdaptiveThreshold,
    AveragingBlur,
    GaussianBlur,
    MedianBlur,
    GrayScale,
    Threshold,
    Denoise,
    Smooth,
    Sharp,
)
from models.operations import (
    Brightness,
    Resize,
    Rotate,
    Flip,
    Crop,
)
from models.draw import (
    Rectangle,
    Circle,
    Line,
)


def main():
    image = Image("./images/image_2.webp")

    e = Editor(image)
    e.add_layer(
        GrayScale(),
        GaussianBlur(kernel_size=(3, 3)),
        AdaptiveThreshold(255, 3, 5),
    )

    image = e.apply()
    image.show()
    image.store()


if __name__ == "__main__":
    main()
