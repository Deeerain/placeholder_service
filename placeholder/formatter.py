import io
from typing import Dict
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
    def __init__(self, formatters: Dict[ImageFormat, AbstractImageFormater]):
        self.formatters = formatters

    def build(self, format: ImageFormat) -> AbstractImageFormater:
        return self.formatters.get(format)

    def build_by_name(self, format: str) -> AbstractImageFormater:
        format = ImageFormat(format)
        return self.build(format)


def get_default_formatter_factory():
    factory = FormatterFactory({
        ImageFormat.JPEG: JpegFormatter(),
        ImageFormat.PNG: PngFormatter(),
    })

    return factory
