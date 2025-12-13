from flask import Flask
from flask import Response, render_template_string
from flask.logging import logging
from flask import make_response

import markdown

from placeholder.generator import PlaceholderGenerator as pg
from placeholder.formatter import get_default_formatter_factory


app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/<int:w>x<int:h>.<e>')
def get_placeholder(w: int, h: int, e: str) -> Response:
    try:
        formatter = get_default_formatter_factory().build_by_name(e)

        placeholder = pg().init((w, h)).set_text(
            lambda p: "{}x{}".format(p.width, p.height)).generate()
        raw_image = formatter.to_bytes(placeholder)

        return Response(
            raw_image,
            status=200,
            headers={
                'Content-Length': len(raw_image),
                'Content-Type': f'image/{e}'
            })
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
