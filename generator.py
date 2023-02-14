from typing import Literal, Tuple
import io

from PIL import Image as ImageT
from PIL import ImageDraw, ImageFont
from PIL.Image import Image


class AbstractPlaceholder(object):
    placeholder_width: int
    placeholder_height: int
    placeholder_format: Literal['jpeg', 'png']

    def __generate(self) -> Image:
        raise NotImplementedError

    def get_size(self) -> Tuple[str, str]:
        return self.placeholder_width, self.placeholder_height

    def get_message(self) -> str:
        w, h = self.get_size()
        return '{}x{}'.format(w, h)

    def calculate_to_center(self, text_size: Tuple[int, int]) -> Tuple[int, int]:
        tx, ty = text_size
        width, height = self.get_size()

        size = (width - tx) / 2, (height - ty) / 2

        return size

    def to_bytes(self) -> bytes:
        raise NotImplementedError

    def __bytes__(self) -> bytes:
        return self.to_bytes()


class Placeholder(AbstractPlaceholder):
    def __init__(self, width: int, height: int, format: Literal['jpeg', 'png']) -> None:
        self.placeholder_width = width
        self.placeholder_height = height
        self.placeholder_format = format

        self.__generate()

    def __generate(self) -> Image:
        message = self.get_message()

        self.placeholder_image = ImageT.new(
            mode='RGB', size=self.get_size(), color='gray')

        font = ImageFont.truetype('arial', size=36)
        pencil = ImageDraw.Draw(self.placeholder_image)

        pencil.text(self.calculate_to_center(font.getsize(message)), font=font,
                    fill='black', size=36, text=message, align='center')

    def to_bytes(self) -> bytes:
        raw_image = io.BytesIO()
        self.placeholder_image.save(raw_image, format=self.placeholder_format)
        return raw_image.getvalue()
