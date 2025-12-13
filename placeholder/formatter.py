import io
from enum import Enum
from abc import ABC, abstractmethod

from PIL import Image


class ImageFormat(Enum):
    JPEG = 'jpeg'
    PNG = 'png'


class AbstractImageFormater(ABC):
    @abstractmethod
    def to_bytes(self, image: Image) -> bytes:
        raise NotImplementedError()


class JpegFormatter(AbstractImageFormater):
    def to_bytes(self, image: Image) -> bytes:
        raw_image = io.BytesIO()
        image.save(raw_image, ImageFormat.JPEG.value)
        return raw_image.getvalue()


class PngFormatter(AbstractImageFormater):
    def to_bytes(self, image: Image) -> bytes:
        raw_image = io.BytesIO()
        image.save(raw_image, ImageFormat.PNG.value)
        return raw_image.getvalue()


class FormatterFactory:
    def __init__(self):
        self.jpeg_formmatter = JpegFormatter()
        self.png_formatter = PngFormatter()

    def build(self, format: ImageFormat) -> AbstractImageFormater:
        formatter: AbstractImageFormater

        match format:
            case ImageFormat.JPEG:
                formatter = self.jpeg_formmatter
            case ImageFormat.PNG:
                formatter = self.png_formatter

        return formatter

    def build_by_name(self, format: str) -> AbstractImageFormater:
        format = ImageFormat(format)

        return self.build(format)
