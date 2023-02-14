from flask import Flask
from flask import make_response
import io

from generator import Placeholder

app = Flask(__name__)


@app.route('/<w>x<h>.<e>')
def get_placeholder(w: int, h: int, e: str):

    g = Placeholder(int(w), int(h), e)

    response = make_response(g.to_bytes())
    response.headers['Content-Type'] = f'image/{e}'
    response.headers['Content-Length'] = len(g.to_bytes())

    return response
