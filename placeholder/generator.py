from typing import Tuple
from abc import ABC, abstractmethod

from PIL import Image as ImageT
from PIL import ImageDraw, ImageFont
from PIL.Image import Image

from .formatter import AbstractImageFormater


class AbstractGenerator(ABC):
    @abstractmethod
    def generate(
            self,
            width: int,
            height: int,
            color: float | tuple[float, ...]) -> Image:
        raise NotImplementedError()

    @abstractmethod
    def to_bytes(self) -> bytes:
        raise NotImplementedError()


class BaseGenerator(AbstractGenerator):
    def get_size(self) -> Tuple[str, str]:
        return self.placeholder_width, self.placeholder_height

    def get_message(self, width: int, height: int) -> str:
        return '{}x{}'.format(width, height)

    def calculate_to_center(
            self, text_size: Tuple[int, int],
            size: Tuple[int, int]) -> Tuple[int, int]:
        tx, ty = text_size
        width, height = size
        return (width - tx) / 2, (height - ty) / 2


class PlaceholderGenerator(BaseGenerator):
    def __init__(self, formatter: AbstractImageFormater):
        self.formatter: AbstractImageFormater = formatter
        self.image: Image

    def generate(
            self, width: int,
            height: int,
            color: float | tuple[float, ...] = 'gray'):
        message = self.get_message(width, height)

        self.image = ImageT.new(
            mode='RGB', size=[width, height], color=color)

        font = ImageFont.load_default(size=36)
        text_size = font.getbbox(message)
        text_position = self.calculate_to_center(
            (text_size[2], text_size[3]), (width, height))
        pencil = ImageDraw.Draw(self.image)
        pencil.text(text_position, font=font, fill='black',
                    size=36, text=message, align='center')

    def to_bytes(self) -> bytes:
        return self.formatter.to_bytes(self.image)
