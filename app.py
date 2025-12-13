from flask import Flask
from flask import Response, render_template_string
from flask.logging import logging
from flask import make_response

import markdown

from placeholder.generator import PlaceholderGenerator
from placeholder.formatter import FormatterFactory


app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/<int:w>x<int:h>.<e>')
def get_placeholder(w: int, h: int, e: str) -> Response:
    try:
        formatter = FormatterFactory().build_by_name(e)

        placeholder = PlaceholderGenerator(formatter)
        placeholder.generate(w, h, 'gray')
        raw_image = placeholder.to_bytes()

        response = make_response(raw_image)
        response.headers['Content-Type'] = f'image/{e}'
        response.headers['Content-Length'] = len(raw_image)

        return response
    except KeyError as e:
        errmsg = "Formant %s not found" % e
        logger.error(errmsg)
        return Response(errmsg, status=400)


@app.route('/')
def index() -> Response:
    with open('./README.md', mode='r') as file:
        md_html = markdown.markdown(file.read())
        response = make_response(render_template_string(md_html))
        return response
