from flask import Flask, request

app = Flask(__name__)


def url_with_param(lbl, val):
    arg_dict = dict(request.args)
    arg_dict[lbl] = val
    return request.path + '?' + '&'.join([f'{k}={v}' for k, v in arg_dict.items()])


app.jinja_env.globals.update(url_with_param=url_with_param)

from frontend.routes import route_calendar  # noqa: E402, F401
