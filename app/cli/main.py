from builders import Editor
from models import Image
from models.operations import Brightness, Resize, Rotate, Flip, Crop
from models.filters import GaussianBlur, MedianBlur, GrayScale
from models.draw import Rectangle, Circle, Line


def main():
    image = Image("./images/image_2.webp")
    width, height = image.get_details()

    e = Editor(image)
    e.add_layer(
        GaussianBlur(),
        MedianBlur(),
        GrayScale(),
        Crop(
            (int(width * 0.2), int(height * 0.2)),
            (int(width - width * 0.2), int(height - height * 0.2)),
        ),
        Rectangle(
            (int(width * 0.2), int(height * 0.2)),
            (int(width - width * 0.2), int(height - height * 0.2)),
        ),
        Circle(
            (int(width / 2), int(height / 2)),
            int(width if width < height else height * 0.3),
        ),
        Line(
            (int(width * 0.1), int(height * 0.1)),
            (int(width - width * 0.1), int(height - height * 0.1)),
        ),
        Brightness(-100),
        Resize(2),
        Rotate(90),
        Flip(1),
        Flip(1),
    )

    image = e.apply()
    image.show()
    image.store()


if __name__ == "__main__":
    main()
