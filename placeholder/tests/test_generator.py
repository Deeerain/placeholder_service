import pytest
from placeholder.generator import PlaceholderGenerator


@pytest.mark.parametrize('size', [(300, 300), (100, 100), ('99', '88')])
def test_generator(size):
    try:
        placeholder = PlaceholderGenerator().init(size).generate()
        assert placeholder.width == size[0] and placeholder.height == size[1]
    except Exception as e:
        assert isinstance(e, TypeError)
