from flask import Flask
from flask import Response
from flask import make_response

from generator import Placeholder

app = Flask(__name__)


@app.route('/<w>x<h>.<e>')
def get_placeholder(w: int, h: int, e: str) -> Response:

    placeholder = Placeholder(int(w), int(h), e)

    response = make_response(placeholder.to_bytes())
    response.headers['Content-Type'] = f'image/{e}'
    response.headers['Content-Length'] = len(placeholder.to_bytes())

    return response


@app.route('/')
def index() -> Response:
    response = make_response("Hello from Placeholder Service!")
    return response
