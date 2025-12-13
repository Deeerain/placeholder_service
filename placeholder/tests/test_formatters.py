import io

import pytest

from placeholder import Placeholder
from placeholder.formatter import (
    FormatterFactory,
    JpegFormatter,
    PngFormatter,
    ImageFormat,
    AbstractImageFormater,
    get_default_formatter_factory
)


def test_get_default_formatter_factory():
    formatter_factory = get_default_formatter_factory()

    assert any(formatter_factory.formatters)


@pytest.mark.parametrize(
    'formatters', [{
        ImageFormat.JPEG: JpegFormatter(),
        ImageFormat.PNG: PngFormatter(),
    }])
def test_build_formatter_factory(
        formatters: dict[ImageFormat, AbstractImageFormater]):
    factory = FormatterFactory(formatters)

    assert factory is not None
    assert any(factory.formatters)
    assert isinstance(factory.build(ImageFormat.JPEG), JpegFormatter)


@pytest.mark.parametrize('name', ['png', 'jpeg', 'svg'])
def test_build_formatter_by_str(name: str):
    try:
        factory = get_default_formatter_factory()
        assert factory is not None
        assert any(factory.formatters)
        f = factory.build_by_name(name)
        assert f is not None
        assert isinstance(f, AbstractImageFormater)
    except Exception as e:
        assert isinstance(e, ValueError)


@pytest.mark.parametrize("image_format", [ImageFormat.JPEG, ImageFormat.PNG])
def test_conver_placeholder(image_format: ImageFormat):
    factory = get_default_formatter_factory()
    formatter = factory.build(image_format)
    placeholder = Placeholder((300, 300))

    bytes_image1 = io.BytesIO()
    placeholder.image.save(bytes_image1, image_format.value)
    bytes_image2 = formatter.to_bytes(placeholder)

    assert len(bytes_image1.getvalue()) == len(bytes_image2)
