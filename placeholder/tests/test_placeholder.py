import pytest
from placeholder import Placeholder


@pytest.mark.parametrize('size', [(300, 300), ('100', '100')])
def test_create_placeholder(size: tuple[int, int]):
    try:
        placeholder = Placeholder(size)

        assert placeholder.width == size[0] and placeholder.height == size[1]
    except Exception as e:
        assert isinstance(e, TypeError)
