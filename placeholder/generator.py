from typing import Tuple, Self, Callable
from abc import ABC, abstractmethod

from PIL import ImageDraw, ImageFont

from placeholder import Placeholder


class AbstractGenerator(ABC):
    @abstractmethod
    def generate(self) -> Placeholder:
        raise NotImplementedError()


class BaseGenerator(AbstractGenerator):
    def get_message(self, width: int, height: int) -> str:
        return '{}x{}'.format(width, height)

    def calculate_to_center(
            self, text_size: Tuple[int, int],
            size: Tuple[int, int]) -> Tuple[int, int]:
        tx, ty = text_size
        width, height = size
        return (width - tx) / 2, (height - ty) / 2


class PlaceholderGenerator(BaseGenerator):
    def __init__(self):
        self.placeholder: Placeholder | None

    def set_text(self, message_callback: Callable[[Placeholder], str]) -> Self:
        message = message_callback(self.placeholder)
        font = ImageFont.load_default(size=36)
        text_size = font.getbbox(message)
        text_position = self.calculate_to_center(
            (text_size[2], text_size[3]), (self.placeholder.width,
                                           self.placeholder.height))
        pencil = ImageDraw.Draw(self.placeholder.image)
        pencil.text(text_position, font=font, fill='black',
                    size=36, text=message, align='center')

        return self

    def init(self, size: Tuple[int, int],
             color: float | Tuple[float, ...] = 'gray') -> Self:
        self.placeholder = Placeholder(size, color)
        return self

    def generate(self) -> Placeholder:
        return self.placeholder
