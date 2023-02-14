from flask import Flask

app = Flask(__name__)


@app.route('/<w>x<h>.<e>')
def get_placeholder(w: int, h: int, e: str):
    pass