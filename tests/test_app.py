import pytest

from flask.testing import Client

from app import app


def test_index_page():
    client = Client(app)
    response = client.get('/')

    assert response is not None
    assert response.status_code == 200
    assert response.headers['Content-Type'].startswith('text/html')


@pytest.mark.parametrize(
    'size, format',
    [
        ((100, 100), 'jpeg'),
        ((150, 150), 'svg'),
        (('300', '300'), 'png')
    ])
def test_main_route(size, format):
    client = Client(app)
    response = client.get(f'/{size[0]}x{size[1]}.{format}')

    assert response is not None
    assert response.status_code == 200 or response.status_code == 400

    if response.status_code == 200:
        assert response.headers['Content-Type'] == f'image/{format}'
        assert int(response.headers['Content-Length']) > 0
