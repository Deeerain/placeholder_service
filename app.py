from flask import Flask
from flask import make_response
import io

from generator import Generator

app = Flask(__name__)


@app.route('/<w>x<h>.<e>')
def get_placeholder(w: int, h: int, e: str):

    g = Generator(int(w), int(h))
    placeholder = g.generate()

    raw_image = io.BytesIO()
    placeholder.save(raw_image, format=e)
    raw_image = raw_image.getvalue()

    response = make_response(raw_image)
    response.headers['Content-Type'] = f'image/{e}'
    response.headers['Content-Length'] = len(raw_image)
    response.data = raw_image

    return response
