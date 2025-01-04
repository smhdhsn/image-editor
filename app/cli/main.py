from builders import Editor
from models import Image
from models.filters import GaussianBlur, MedianBlur, GrayScale
from models.operations import Rectangle, Line


def main():
    image = Image("./images/image_2.webp")
    width, height = image.get_details()

    e = Editor(image)
    e.add_filters(
        GaussianBlur(),
        MedianBlur(),
        GrayScale(),
    ).add_operations(
        Line(
            (int(width * 0.1), int(height * 0.1)),
            (int(width - width * 0.1), int(height - height * 0.1)),
        ),
        Rectangle(
            (int(width * 0.2), int(height * 0.2)),
            (int(width - width * 0.2), int(height - height * 0.2)),
        ),
    )

    image = e.apply()
    image.show()
    image.store()


if __name__ == "__main__":
    main()
