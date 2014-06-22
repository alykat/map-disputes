#!/usr/bin/env python

import argparse
from flask import Flask, render_template

import app_config
from render_utils import make_context, urlencode_filter
import static

app = Flask(__name__)

app.jinja_env.filters['urlencode'] = urlencode_filter

# Example application views
@app.route('/')
def index():
    """
    Example view demonstrating rendering a simple HTML page.
    """

    return render_template('index.html', **make_context())

@app.route('/dispute/<string:slug>/')
def dispute(slug):
  return render_template('dispute.html', **make_context())

app.register_blueprint(static.static)

# Boilerplate
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()
    server_port = 8000

    if args.port:
        server_port = int(args.port)

    app.run(host='0.0.0.0', port=server_port, debug=app_config.DEBUG)
