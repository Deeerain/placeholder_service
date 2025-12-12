from flask import Flask
from flask import Response, render_template_string
from flask import make_response
import markdown

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
    with open('./README.md', mode='r') as file:
        md_html = markdown.markdown(file.read())
        response = make_response(render_template_string(md_html))
        return response
