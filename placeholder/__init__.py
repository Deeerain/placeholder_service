from PIL import Image
from typing import Tuple


class Placeholder:
    def __init__(self, size: Tuple[int, int], color=0):
        self._image: Image = Image.new('RGB', size, color)

    @property
    def image(self) -> Image:
        return self._image

    @property
    def width(self) -> int:
        return self.image.width

    @property
    def height(self) -> int:
        return self.image.height
