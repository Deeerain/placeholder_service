from typing import Self

from PIL import Image as ImageT
from PIL import ImageDraw, ImageFont
from PIL.Image import Image


class Generator:
    def __init__(self, w: int, h: int) -> None:
        self.width = w
        self.height = h

    def generate(self) -> Image:
        message = f'{self.width} x {self.height}'

        image: Image = ImageT.new(mode='RGB', size=(
            self.width, self.height), color='gray')
        font = ImageFont.truetype('arial', size=36)
        sx, sy = font.getsize(message)
        pencil = ImageDraw.Draw(image)
        pencil.text(((self.width - sx) / 2, (self.height - sy) / 2),
                    font=font, fill='black', size=36, text=message, align='center')

        return image
