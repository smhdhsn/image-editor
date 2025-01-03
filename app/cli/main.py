from builders import FilterBuilder
from models import Image
from models.filters import GaussianBlur, MedianBlur, GrayScale


def main():
    image = Image("./images/image_2.webp")

    fb = FilterBuilder(image)
    fb.register(
        GaussianBlur,
        MedianBlur,
        GrayScale,
    )
    image = fb.apply()

    image.show()
    image.store()


if __name__ == "__main__":
    main()
