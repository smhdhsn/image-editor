from builders import Editor
from models import Image
from models.filters import GaussianBlur, MedianBlur, GrayScale
from models.draw import Rectangle, Circle, Line
from models.operations import Rotate


def main():
    image = Image("./images/image_2.webp")
    width, height = image.get_details()

    e = Editor(image)
    e.add_layer(
        GaussianBlur(),
        MedianBlur(),
        GrayScale(),
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
        Rotate(90),
    )

    image = e.apply()
    image.show()
    image.store()


if __name__ == "__main__":
    main()
